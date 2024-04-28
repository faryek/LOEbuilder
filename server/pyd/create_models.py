from pydantic import BaseModel, Field
from typing import List

class UserCreate(BaseModel):
    username: str = Field(..., max_length=255, example='Login')
    password: str = Field(..., max_length=255, example='passExample')
    class Config:
        orm_mode = True

class URLCreate(BaseModel):
    id: int = Field(None, gt=0, example=1)
    name: str = Field(..., example='https://poeplanner.com/atlas-tree/BAAQAIQAJuaH1PP3Xz4PgWXyArZjD0sy67sklwBIHtey-uUxt-Vs8whDhrSxnyySEYQIesHuZIBtiMAq6ng8WSFgky14ZvI4jEEqbrVmpdrOAF6dzlrJ_Uy6jeqT8n7IqLz8-iq72Vt9Hsy3hqGvOr3a5PcfAKoKnzumNAf0TdfXK2iJZ2AqEntg1I-HnS370MbsDwLFtdiCp6FoKY2OOQF6fitZhnTSglGI6EU6ZjA342ayz0fhEBkKpXPiDqQFotDLFyFMxSEX3TUwx10XUDak9nUZlMGvOnbBdOXsOMZxC4_lAzCIB7cP1WnCdvrl2VypQ7VjoHHEGLli5DOar2-1mbkc3c776We51NAoFAAfiwgAAAAAAAADAwAAAAAAAAAAAA==')

    class Config:
        orm_mode = True
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
