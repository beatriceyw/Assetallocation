from typing import Optional

from pydantic import BaseModel

class userInfoRequestDto(BaseModel):
    email: str
    userPassword: str
