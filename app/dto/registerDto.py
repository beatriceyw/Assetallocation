from typing import Optional

from pydantic import BaseModel

class registerRequestDto(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str

class mail_DobleCheck_RequestDto(BaseModel):
    email: str