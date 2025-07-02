from fastapi import FastAPI
from apps.api.routes import item, order, auth

app = FastAPI()

for router in [item.router, order.router, auth.router]:
    app.include_router(router, prefix="/api")