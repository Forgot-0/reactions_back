import motor.motor_asyncio
import asyncio

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client['reactions']

reaction = database['reactions_collections']








async def create_index():

    index_keys_uoc = [("user_id", 1), ("content_type", 1), ('object_pk', 1)]
    index_options_uoc = {
        "name": "uoc",
        "unique": True,
        "background": True
    }

    index_keys_uc = [('user_id', 1), ("content_type", 1)]
    index_options_uc = {
        "name": "uc",
        "unique": False,
        "background": True
    }





    await reaction.create_index(index_keys_uoc, **index_options_uoc)
    await reaction.create_index(index_keys_uc, **index_options_uc)


# asyncio.run(create_index())
