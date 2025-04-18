from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables, delete_tables
from books_router import router as books_router
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена...")
    await create_tables()
    print("... и готова к работе")
    yield
    print("stopping...")


app = FastAPI(lifespan=lifespan)
app.include_router(books_router)
app.include_router(tasks_router)
