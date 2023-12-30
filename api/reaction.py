from fastapi import APIRouter
from models.schemas.reaction import TotalReaction, Reaction
from models.db.database import reaction

router = APIRouter(prefix="/reaction", tags=["reaction"])



@router.post('/create_reaction/', response_model=Reaction)
async def create_reaction(r: Reaction):
    res = await reaction.insert_one(r.dict())
    return r

@router.delete('/delete_reaction/')
async def delete_reaction(reac: Reaction):
    pass

@router.get('/get_reaction/', response_model=Reaction)
async def get_reaction(user_id: int, object_pk: int, content_type: str):
    pass


@router.get('/popular/', response_model=TotalReaction)
async def get_popular(object_pk: int, content_type: str):
    pass