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


@app.get("/weapons", response_model=List[pyd.WeaponsSchema])
async def get_urls(db: Session = Depends(get_db)):
    return db.query(models.Weapon).all()

@app.get("/armour", response_model=List[pyd.ArmourSchema])
async def get_urls(db: Session = Depends(get_db)):
    return db.query(models.Armour).all()

@app.get("/accessory", response_model=List[pyd.AccessorySchema])
async def get_urls(db: Session = Depends(get_db)):
    return db.query(models.Accessory).all()

@app.get("/classes", response_model=List[pyd.ClassBase])
async def get_urls(db: Session = Depends(get_db)):
    return db.query(models.Class).all()

@app.get("/passives", response_model=List[pyd.PassiveSchema])
async def get_urls(db: Session = Depends(get_db)):
    return db.query(models.Passive).all()
            
@app.get("/affixes", response_model=List[pyd.AffixesSchema])
async def get_urls(db: Session = Depends(get_db)):
    return db.query(models.Affix).all()

# # подключение АпиРоутера (маршруты сущности)
# app.include_router(user_router)
# app.include_router(category_router)
# app.include_router(product_router)


# тестовый комент 228
