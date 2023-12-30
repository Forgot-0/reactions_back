from fastapi import FastAPI
from api.reaction import router


app = FastAPI()
app.include_router(router)