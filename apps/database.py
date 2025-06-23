from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import text

DATABASE_URL = "mysql+pymysql://root:Alz081897997!@localhost:3306/selcashoes"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Buat tes koneksi
# try:
#     # Tes koneksi dengan execute query sederhana
#     with engine.connect() as connection:
#         result = connection.execute(text("SELECT 1"))
#         print("✅ Koneksi berhasil! Hasil:", result.fetchone())
# except Exception as e:
#     print("❌ Gagal konek ke database:")
#     print(e)