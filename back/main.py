from fastapi import FastAPI, Depends, HTTPException, Security
import models
import pyd
import jwt
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from datetime import datetime, timedelta
from database import engine, get_db
from auth import AuthHandler
import base64
from fastapi.middleware.cors import CORSMiddleware
# from routers import category_router, product_router, user_router

# создание таблиц в БД из моделей
models.Base.metadata.create_all(bind=engine)

# Инициализация фастапи
app = FastAPI()
# получение всех категорий
# @router.get("/", response_model=List[pyd.CategorySchema])
# async def get_categories(db: Session = Depends(get_db)):
#     return db.query(models.Category).all()
auth_handler = AuthHandler()


@app.post('/register', response_model=pyd.UserCreate)
async def user_reg(user_input: pyd.UserCreate, db: Session = Depends(get_db)):
    user_db = db.query(models.User).filter(
        models.User.name == user_input.name
    ).first()
    if user_db:
        raise HTTPException(400, 'User exists')
    hashed_pass = auth_handler.get_password_hash(user_input.pwd)
    user_db = models.User(name=user_input.name,
                          pwd=hashed_pass,
                          email = user_input.email,
                          birthday=user_input.birthday,
                          role_id = user_input.role_id
                          )
    db.add(user_db)
    db.commit()
    return user_db

@app.post('/login')
async def user_login(user_input:pyd.UserLogin,db:Session=Depends(get_db)):
    user_db = db.query(models.User).filter(
        models.User.name == user_input.name
    ).first()
    if not user_db:
        raise HTTPException(404,'User not found')
    if auth_handler.verify_password(user_input.pwd, user_db.pwd):
        token = auth_handler.encode_token(user_db.name)
        return {'token': token}
    else:
        raise HTTPException(403, 'xd')
    
@app.post('/build/url_create',response_model=pyd.URLBase)
async def url_create(url_input:pyd.URLCreate,username=Depends(auth_handler.auth_wrapper),db:Session=Depends(get_db)):
    user_db = db.query(models.User).filter(
        models.User.name == username
    ).first()
    url_db = models.URL(
        name = base64.b64encode(url_input.name.encode()),
        user_id = user_db.id
    )
    db.add(url_db)
    db.commit()
    return url_db

@app.get("/users", response_model=List[pyd.UserSchema])
async def get_users(username=Depends(auth_handler.auth_wrapper),db: Session = Depends(get_db)):
    return db.query(models.User).all()


@app.get("/weapons", response_model=List[pyd.WeaponsSchema])
async def get_weapons(username=Depends(auth_handler.auth_wrapper),db: Session = Depends(get_db)):
    return db.query(models.Weapon).all()


@app.get("/armour", response_model=List[pyd.ArmourSchema])
async def get_armour(username=Depends(auth_handler.auth_wrapper),db: Session = Depends(get_db)):
    return db.query(models.Armour).all()


@app.get("/accessory", response_model=List[pyd.AccessorySchema])
async def get_accessory(username=Depends(auth_handler.auth_wrapper),db: Session = Depends(get_db)):
    return db.query(models.Accessory).all()


@app.get("/classes", response_model=List[pyd.ClassBase])
async def get_classes(username=Depends(auth_handler.auth_wrapper),db: Session = Depends(get_db)):
    return db.query(models.Class).all()


@app.get("/passives", response_model=List[pyd.PassiveSchema])
async def get_passives(username=Depends(auth_handler.auth_wrapper),db: Session = Depends(get_db)):
    return db.query(models.Passive).all()


@app.get("/affixes", response_model=List[pyd.AffixesSchema])
async def get_affixes(username=Depends(auth_handler.auth_wrapper),db: Session = Depends(get_db)):
    return db.query(models.Affix).all()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)