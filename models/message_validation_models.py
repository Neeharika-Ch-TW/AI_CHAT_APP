from pydantic import BaseModel,Field
from typing import Literal

class MessageValidation(BaseModel):
    role:Literal['user','assistant']
    content: str=Field(min_length=1)
