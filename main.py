from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.api.routes import item, order, auth

app = FastAPI()

# Izinkan asal (origin) dari perangkat yang jalankan React Native
origins = [
    "http://localhost:19006",  # Jika pakai Expo Go via browser
    "http://localhost:8081",   # Jika debug di Metro
    "http://127.0.0.1:8081",
    "http://192.168.0.101",    # Ganti xxx dengan IP lokal kamu
    "exp://192.168.0.101",     # Jika pakai Expo Go
    "*",  # (opsional) semua origin - hanya untuk testing, jangan untuk production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Bisa pakai ["*"] untuk testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in [item.router, order.router, auth.router]:
    app.include_router(router, prefix="/api")