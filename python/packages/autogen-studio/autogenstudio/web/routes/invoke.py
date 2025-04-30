import os

from fastapi import APIRouter
from autogen_core import ComponentModel
from autogenstudio.teammanager import TeamManager
from autogenstudio.datamodel import Response
from typing import Union
from pydantic import BaseModel

router = APIRouter()
team_manager = TeamManager()

class InvokeTaskRequest(BaseModel):
    task: str
    team_config: dict

@router.post("/")
async def invoke(request: InvokeTaskRequest):
    response = Response(message="Task successfully completed", status=True, data=None)
    try:
        result_message = await team_manager.run(task=request.task, team_config=request.team_config)
        response.data = result_message
    except Exception as e:
        response.message = str(e)
        response.status = False
    return response
