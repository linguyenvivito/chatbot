import axios from 'axios';
import type { ChatRequest, ChatResponse } from '../types/chat.types';

// 1. Base URL config - pointing to your Python backend (e.g., FastAPI, Flask, Django)
const BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api';

const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// 3. API Calling Functions
export const chatClient = {
    sendMessage: async (chatRequest: ChatRequest): Promise<ChatResponse> => {
        try {
            const response = await api.post('/chat', { message: chatRequest.message });
            return response.data; // Assuming the backend returns the bot's response in the data field
        }
        catch (error) {
            console.error('Error sending message:', error);
            throw error;
        }   
    }
};