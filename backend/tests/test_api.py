from fastapi.testclient import TestClient

import backend.src.main
from features.chat import chat_api


def test_read_root_returns_hello_world() -> None:
    client = TestClient(backend.src.main.app)

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_chat_endpoint_returns_model_message(monkeypatch) -> None:
    client = TestClient(backend.src.main.app)

    class _Message:
        content = "Mocked assistant reply"

    class _Choice:
        message = _Message()

    class _Response:
        choices = [_Choice()]

    def fake_create(*, model: str, messages: list[dict[str, str]]):
        assert model == "gpt-4o-mini"
        assert messages == [{"role": "user", "content": "Hello"}]
        return _Response()

    monkeypatch.setattr(chat_api.client.chat.completions, "create", fake_create)

    response = client.post("/api/chat", json={"message": "Hello"})

    assert response.status_code == 200
    assert response.json() == {"message": "Mocked assistant reply"}


def test_chat_endpoint_returns_502_when_openai_fails(monkeypatch) -> None:
    client = TestClient(backend.src.main.app)

    def fake_create(*, model: str, messages: list[dict[str, str]]):
        raise RuntimeError("OpenAI failure")

    monkeypatch.setattr(chat_api.client.chat.completions, "create", fake_create)

    response = client.post("/api/chat", json={"message": "Hello"})

    assert response.status_code == 502
    assert response.json() == {"detail": "Failed to generate chat response"}


def test_chat_endpoint_validates_request_body() -> None:
    client = TestClient(backend.src.main.app)

    response = client.post("/api/chat", json={})

    assert response.status_code == 422
