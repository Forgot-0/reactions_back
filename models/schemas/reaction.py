from pydantic import BaseModel



class Reaction(BaseModel):
    user_id: int
    object_pk: int
    content_type: str
    reac: str


class TotalReaction(BaseModel):
    object_pk: int
    content_type: str
    reac: str
    total: int