from fastapi import FastAPI, Depends
import models
from database import SessionLocal, engine, get_db
from typing import List
import pyd
from sqlalchemy.orm import Session
# from routers import category_router, product_router, user_router

# создание таблиц в БД из моделей
models.Base.metadata.create_all(bind=engine)

# Инициализация фастапи
app = FastAPI()
# получение всех категорий
# @router.get("/", response_model=List[pyd.CategorySchema])
# async def get_categories(db: Session = Depends(get_db)):
#     return db.query(models.Category).all()


@app.get("/", response_model=List[pyd.URLSSchema])
async def get_urls(db: Session = Depends(get_db)):
    return db.query(models.URL).all()


# # подключение АпиРоутера (маршруты сущности)
# app.include_router(user_router)
# app.include_router(category_router)
# app.include_router(product_router)


# тестовый комент 228
