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
import json


app = FastAPI()

auth_handler = AuthHandler()


@app.post('/urls_user', response_model=List[pyd.URLSSchema])
async def get_urls_user(user_input:pyd.URLSortBase,username=Depends(auth_handler.auth_wrapper),db:Session=Depends(get_db)):
    user_db = db.query(models.User).filter(
        models.User.name == username
    ).first()

    url_db =  db.query(models.URL).filter(
        models.URL.user_id == user_db.id
    ).all()

    sorted_array = []
    cycles = []
    classes = []
    types = []
    purposes = []

    if user_input.cycle == '':
        cycles = ['Первое бытие','Второе житие']
    else:
        cycles.append(user_input.cycle)

    if user_input.class_id== 9:
        classes = [1,2,3,4,5,6,7,8]
    else:
        classes.append(user_input.class_id)
    
    if user_input.type == '':
        types = ['Стартер','Эндгейм']
    else:
        types.append(user_input.type)
    
    if user_input.purpose == '':
        purposes = ['Боссинг','Маппинг']
    else:
        purposes.append(user_input.purpose)

    for i in range(len(url_db)):
        for_decode = url_db[i].name.replace('%slash%','/')
        decoded = base64.b64decode(for_decode)
        my_json = decoded.decode('utf-8').replace("'", '"')
        parsed = json.loads(my_json)
        my_json =my_json + 'HereWeAre'
        my_json = my_json + url_db[i].name
        url_db[i].name = my_json

        if url_db[i].class_id in classes and parsed['top_inputs']['cycle'] in cycles and parsed['top_inputs']['type'] in types and parsed['top_inputs']['purpose'] in purposes:
            sorted_array.append(url_db[i])

    return sorted_array


@app.post('/urls', response_model=List[pyd.URLSSchema])
async def urls_sort(user_input:pyd.URLSortBase,db:Session=Depends(get_db)):
    url_db = db.query(models.URL).all()

    sorted_array = []
    cycles = []
    classes = []
    types = []
    purposes = []

    if user_input.cycle == '':
        cycles = ['Первое бытие','Второе житие']
    else:
        cycles.append(user_input.cycle)

    if user_input.class_id== 9:
        classes = [1,2,3,4,5,6,7,8]
    else:
        classes.append(user_input.class_id)
    
    if user_input.type == '':
        types = ['Стартер','Эндгейм']
    else:
        types.append(user_input.type)
    
    if user_input.purpose == '':
        purposes = ['Боссинг','Маппинг']
    else:
        purposes.append(user_input.purpose)

    for i in range(len(url_db)):
        for_decode = url_db[i].name.replace('%slash%','/')
        decoded = base64.b64decode(for_decode)
        my_json = decoded.decode('utf-8').replace("'", '"')
        parsed = json.loads(my_json)
        my_json =my_json + 'HereWeAre'
        my_json = my_json + url_db[i].name
        url_db[i].name = my_json
        
        if url_db[i].class_id in classes and parsed['top_inputs']['cycle'] in cycles and parsed['top_inputs']['type'] in types and parsed['top_inputs']['purpose'] in purposes:
            sorted_array.append(url_db[i])

            
    return sorted_array



@app.get('/urls_user', response_model=List[pyd.URLSSchema])
async def get_urls(username=Depends(auth_handler.auth_wrapper),db:Session=Depends(get_db)):
    user_db = db.query(models.User).filter(
        models.User.name == username
    ).first()
    url_db =  db.query(models.URL).filter(
        models.URL.user_id == user_db.id
    ).all()
    for i in range(len(url_db)):
        for_decode = url_db[i].name.replace('%slash%','/')
        decoded = base64.b64decode(for_decode)
        my_json = decoded.decode('utf-8').replace("'", '"')
        my_json =my_json + 'HereWeAre'
        my_json = my_json + url_db[i].name

        url_db[i].name = my_json
    return url_db

@app.post('/check_url')
async def check_url(user_input: pyd.URLCheckBase,db:Session=Depends(get_db)):
    user_input_correct = user_input.name.replace('/','%slash%')
    print(user_input_correct)
    url_db = db.query(models.URL).filter(
        models.URL.name == user_input_correct
    ).first()
    if not url_db:
        raise HTTPException(404, 'Build not found')
    print(user_input.name)
    decoded = base64.b64decode(user_input.name)
    my_json = decoded.decode('utf-8').replace("'", '"')

    weapons = []
    armour = []
    accessories = []

    weapons_names = ['left_hand_id','right_hand_id']
    armour_names = ['belt_id','body_id','boots_id','gloves_id','head_id']
    accessories_names = ['left_ring_id','neck_id','relic_id','right_ring_id']

    final_arrays = [weapons, armour, accessories]

    arrays = [weapons_names,armour_names,accessories_names]

    top_inputs_tuple = ["class","cycle","lvl","name","purpose","type"]
    top_inputs = []


    data = json.loads(my_json)
    s = json.dumps(data, indent=4, sort_keys=True)
    for i in range(3):
        for j in range(len(arrays[i])):
            final_arrays[i].append(data['equiped_ids'][arrays[i][j]])

    for i in range(6):
        top_inputs.append(data['top_inputs'][top_inputs_tuple[i]])
        if i in [0,1,4,5]:
            top_inputs[i].replace("\\","\\\\").encode().decode('unicode-escape')

    return {'equiped_ids':data['equiped_ids'],
            'stats':data['stats'],
            'top_inputs':top_inputs,
            }

@app.post('/register', response_model=pyd.UserCreate)
async def user_reg(user_input: pyd.UserCreateReg, db: Session = Depends(get_db)):
    user_db = db.query(models.User).filter(
        models.User.name == user_input.name
    ).first()
    if user_db:
        raise HTTPException(400, 'User exists')
    user_db = db.query(models.User).filter(
        models.User.email == user_input.email
    ).first()
    if user_db:
        raise HTTPException(400,'email exists')
    if user_input.pwd_2 != user_input.pwd:
        raise HTTPException(403, detail='wrong second password')
    hashed_pass = auth_handler.get_password_hash(user_input.pwd)
    user_db = models.User(name=user_input.name,
                          pwd=hashed_pass,
                          email = user_input.email,
                          role_id = 1
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
    if not user_db:
        raise HTTPException(404,'User not found')
    
    if url_input.name == '':
        raise HTTPException(404,detail='Error')
    
    if url_input.build_name == '':
        raise HTTPException(404,detail='Enter build name')

    url_db = models.URL(
        name = url_input.name,
        user_id = user_db.id,
        class_id = url_input.class_id,
        build_name = url_input.build_name,
    )
    db.add(url_db)
    db.commit()
    return url_db

@app.delete('/build/delete/{url_id}')
async def delete_url(url_id:int,username = Depends(auth_handler.auth_wrapper),db:Session=Depends(get_db)):
    user_db = db.query(models.User).filter(
        models.User.name == username
    ).first()

    url_db = db.query(models.URL).filter(
        models.URL.user_id == user_db.id
    ).first()

    if not url_db:
        raise HTTPException(404,'Ошибка')
    
    url_db_del = db.query(models.URL).filter(
        models.URL.id == url_id
    ).first()
    
    db.delete(url_db_del)
    db.commit()
    return 'success'

@app.get('/user_name')
async def get_username(username=Depends(auth_handler.auth_wrapper),db: Session = Depends(get_db)):
    user_db = db.query(models.User).filter(
        models.User.name == username
    ).first()
    return {"username": username,
            "email":user_db.email}

@app.get("/users", response_model=List[pyd.UserSchema])
async def get_users(username=Depends(auth_handler.auth_wrapper),db: Session = Depends(get_db)):
    return db.query(models.User).all()

@app.get('/urls', response_model=List[pyd.URLSSchema])
async def get_urls(db:Session=Depends(get_db)):
    url_db =  db.query(models.URL).all()
    for i in range(len(url_db)):
        for_decode = url_db[i].name.replace('%slash%','/')
        decoded = base64.b64decode(for_decode)
        my_json = decoded.decode('utf-8').replace("'", '"')
        my_json =my_json + 'HereWeAre'
        my_json = my_json + url_db[i].name

        url_db[i].name = my_json
    return url_db


@app.get("/weapons", response_model=List[pyd.WeaponsSchema])
async def get_weapons(db: Session = Depends(get_db)):
    return db.query(models.Weapon).all()


@app.get("/armour", response_model=List[pyd.ArmourSchema])
async def get_armour(db: Session = Depends(get_db)):
    return db.query(models.Armour).all()


@app.get("/accessory", response_model=List[pyd.AccessorySchema])
async def get_accessory(db: Session = Depends(get_db)):
    return db.query(models.Accessory).all()


@app.get("/classes", response_model=List[pyd.ClassBase])
async def get_classes(db: Session = Depends(get_db)):
    return db.query(models.Class).all()


@app.get("/passives", response_model=List[pyd.PassiveSchema])
async def get_passives(db: Session = Depends(get_db)):
    return db.query(models.Passive).all()


@app.get("/affixes", response_model=List[pyd.AffixesSchema])
async def get_affixes(db: Session = Depends(get_db)):
    return db.query(models.Affix).all()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)