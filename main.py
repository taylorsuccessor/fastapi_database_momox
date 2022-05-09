from fastapi import FastAPI

from app.routers import books_router
from app.database import init_db

app = FastAPI()

app.include_router(books_router)

@app.get("/beat")
def root():
    return {"message": """
            We Checked the connections to database and other
            part of the system and we make sure it's return correct status
            """}

#@app.on_event("startup")
#async def on_startup():
#    await init_db()
