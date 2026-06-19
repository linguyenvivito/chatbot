import os
import sys
from pathlib import Path

# Make backend/src importable for tests (so `import main` works).
BACKEND_SRC = Path(__file__).resolve().parents[1] / "src"
if str(BACKEND_SRC) not in sys.path:
    sys.path.insert(0, str(BACKEND_SRC))

# Prevent OpenAI client initialization errors during import.
os.environ.setdefault("OPENAI_API_KEY", "test-key")
