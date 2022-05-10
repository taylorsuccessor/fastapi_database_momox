from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# todo database url should be move to server.env also database url also to
# share it to alembic
SQLALCHEMY_DATABASE_URL = "sqlite:///./prod_sqlite_database.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def update(db: sessionmaker, object_class: Base, id: int, data: dict):

    item = db.query(object_class).get(id)
    for attr, val in data.items():
        setattr(item, attr, val)

    db.add(item)
    db.commit()
    db.refresh(item)
    return item

