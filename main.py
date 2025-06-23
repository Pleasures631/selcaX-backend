from fastapi import FastAPI
from apps.api.routes import item

app = FastAPI()

app.include_router(item.router, prefix="/api")