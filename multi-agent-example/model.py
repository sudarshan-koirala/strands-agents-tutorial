
# Function to create and return an Ollama model
from strands.models.ollama import OllamaModel

def get_ollama_model(host: str = "http://localhost:11434", model_id: str = "llama3.1") -> OllamaModel:
    """
    Returns an OllamaModel instance.
    Args:
        host (str): Ollama server host URL.
        model_id (str): Model ID to use.
    """
    return OllamaModel(host=host, model_id=model_id)