
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    ok: bool = True
    id: int

    model_config = ConfigDict(from_attributes=True)
