from typing import Optional

from pydantic import BaseModel

class mailCheck_RequestDto(BaseModel):
    email: str
    
class updatePassword_RequestDto(BaseModel):
    email: str
    password: str