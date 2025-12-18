"""Ollama client for local LLM chat completion."""
import ollama
from typing import Dict, Any
from .config import settings


class OllamaService:
    """Service for generating chat responses using local Ollama models."""

    def __init__(self):
        """Initialize Ollama service."""
        self.client = ollama.Client(host=settings.ollama_base_url)
        self.model = settings.ollama_model

    def check_model_available(self) -> bool:
        """
        Check if the configured model is available.

        Returns:
            True if model is available, False otherwise
        """
        try:
            models = self.client.list()
            available_models = [model['name'] for model in models.get('models', [])]
            return self.model in available_models
        except Exception as e:
            print(f"Error checking model availability: {e}")
            return False

    def pull_model(self):
        """
        Pull the model if it's not available.
        """
        try:
            print(f"Pulling model {self.model}... This may take a few minutes.")
            self.client.pull(self.model)
            print(f"Model {self.model} pulled successfully!")
        except Exception as e:
            print(f"Error pulling model: {e}")
            raise

    def generate_response(self, system_prompt: str, user_prompt: str) -> str:
        """
        Generate a chat response using Ollama.

        Args:
            system_prompt: System instructions
            user_prompt: User query with context

        Returns:
            Generated response text
        """
        try:
            response = self.client.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                options={
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "num_predict": 500  # Max tokens in response
                }
            )

            return response['message']['content']

        except Exception as e:
            return f"Error generating response: {str(e)}"

    def ensure_model_ready(self):
        """
        Ensure the model is downloaded and ready to use.
        """
        if not self.check_model_available():
            print(f"Model {self.model} not found locally.")
            self.pull_model()
        else:
            print(f"Model {self.model} is ready!")


# Singleton instance
ollama_service = OllamaService()
