from pydantic import BaseModel

class PushRequest(BaseModel):
    value: float