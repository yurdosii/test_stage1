from environs import Env

env = Env()
env.read_env()

# DB configs
MONGODB_URL = env.str("MONGODB_URL")
MONGODB_DATABASE_NAME = env.str("MONGODB_DATABASE_NAME")
MONGODB_USER_COLLECTION_NAME = env.str("MONGODB_USER_COLLECTION_NAME")

# Auth configs
SECRET_KEY = env.str("SECRET_KEY")
JWT_ALGORITHM = env.str("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
