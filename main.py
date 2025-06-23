from fastapi import FastAPI
from apps.api.routes import item, order

app = FastAPI()

for router in [item.router, order.router]:
    app.include_router(router, prefix="/api")