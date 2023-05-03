from fastapi import FastAPI

from .users_api.views import router as users_router

app = FastAPI()
app.include_router(users_router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}
