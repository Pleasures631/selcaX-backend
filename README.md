echo "# Selcashoes POS System

Aplikasi backend sederhana untuk manajemen inventory dan order dengan Python + FastAPI + SQLAlchemy + Alembic
## Fitur

- CRUD Product
- CRUD Order
- Auto generate Order ID
- Migrasi DB pakai Alembic

## Setup

1. Clone repo
2. Buat virtualenv
3. Jalankan \`pip install -r requirements.txt\`
4. Atur .env → DATABASE_URL
5. Jalankan \`alembic upgrade head\`
6. Jalankan backend \`uvicorn main:app --reload\`

" > README.md
