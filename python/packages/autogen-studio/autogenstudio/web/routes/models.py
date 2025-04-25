from typing import Dict, List

from autogen_ext.models.anthropic._model_info import _MODEL_INFO as anthropic_models
from autogen_ext.models.ollama._model_info import _MODEL_INFO as ollama_models
from autogen_ext.models.openai._model_info import _MODEL_INFO as openai_models
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_models() -> Dict[str, List[str]]:
    response = {
        "anthropic": list(anthropic_models.keys()),
        "ollama": list(ollama_models.keys()),
        "openAI": list(openai_models.keys()),
        "azureOpenAI": list(openai_models.keys()),
    }

    return response
