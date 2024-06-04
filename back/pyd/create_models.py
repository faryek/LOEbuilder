from pydantic import BaseModel, Field, EmailStr
from typing import List
from datetime import date,datetime

class UserCreate(BaseModel):
    email: EmailStr = Field(..., example='help@gmail.com')
    name:str=Field(...,max_length=255,min_length=3,example='nagibator69')
    pwd:str=Field(...,max_length=255,min_length=6,example='123456')

class UserCreateReg(BaseModel):
    email: EmailStr = Field(..., example='help@gmail.com')
    name:str=Field(...,max_length=255,min_length=3,example='nagibator69')
    pwd:str=Field(...,max_length=255,min_length=6,example='123456')
    pwd_2: str= Field(...,max_length=255,min_length=6,example='123456')

class UserLogin(BaseModel):
    name:str=Field(...,max_length=255,min_length=3,example='nagibator69')
    pwd:str=Field(...,max_length=255,min_length=6,example='123456')

class URLCreate(BaseModel):
    id: int = Field(None, gt=0, example=1)
    name: str = Field(..., example='weapons=[1],armour=[1,5,12],accessory=[3,3,15],passives=[1,5,6,7,8,12,15,19,22]')
    class_id: int = Field(...,example=1)

# # тут модели которые используются при создании/редактировании сущностей
# class CategoryCreate(BaseModel):
#     name: str = Field(..., max_length=255, example='Еда')
#     description: str = Field(None, max_length=255, example='То что можно скушать')

#     class Config:
#         orm_mode = True


# class ProductCreate(BaseModel):
#     name: str = Field(..., max_length=255, example='Колбаса')
#     description: str = Field(None, max_length=255, example='Варенная колбаса, самая вкусная')
#     price: int = Field(..., gt=0, example=99.95)

#     category_ids: List[int] = None

#     class Config:
#         orm_mode = True


# class CreateUser(BaseModel):
#     username: str = Field(..., max_length=255, example='Колбаса')
#     password: str = Field(..., max_length=255, example='Колбаса')

#     class Config:
#         orm_mode = True
