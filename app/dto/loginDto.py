from typing import Optional

from pydantic import BaseModel

class loginRequestDto(BaseModel):
    email: str
