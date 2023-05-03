from fastapi import Depends, FastAPI

from .auth_api.views import router as auth_router
from .middlewares import verify_token
from .users_api.views import router as users_router

app = FastAPI()
app.include_router(users_router)
app.include_router(auth_router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/protected")
async def read_protected_root(_: str = Depends(verify_token)):
    return {"Hello": "Protected World"}
