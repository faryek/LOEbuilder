from pydantic import BaseModel, Field, EmailStr
from datetime import date,datetime

class UserBase(BaseModel):
    id: int = Field(None,  example=1)
    email: EmailStr = Field(..., example='help@gmail.com')
    name:str=Field(...,example='nagibator69')
    role_id: int = Field(...,example=1)

    class Config:
        orm_mode = True

class RoleBase(BaseModel):
    id: int = Field(None, gt=0, example=1)
    name: str = Field(..., max_length=255, example='Guest')

    class Config:
        orm_mode = True

class URLBase(BaseModel):
    id: int = Field(None, gt=0, example=1)
    name: str = Field(..., example='https://poeplanner.com/atlas-tree/BAAQAIQAJuaH1PP3Xz4PgWXyArZjD0sy67sklwBIHtey-uUxt-Vs8whDhrSxnyySEYQIesHuZIBtiMAq6ng8WSFgky14ZvI4jEEqbrVmpdrOAF6dzlrJ_Uy6jeqT8n7IqLz8-iq72Vt9Hsy3hqGvOr3a5PcfAKoKnzumNAf0TdfXK2iJZ2AqEntg1I-HnS370MbsDwLFtdiCp6FoKY2OOQF6fitZhnTSglGI6EU6ZjA342ayz0fhEBkKpXPiDqQFotDLFyFMxSEX3TUwx10XUDak9nUZlMGvOnbBdOXsOMZxC4_lAzCIB7cP1WnCdvrl2VypQ7VjoHHEGLli5DOar2-1mbkc3c776We51NAoFAAfiwgAAAAAAAADAwAAAAAAAAAAAA==')
    build_name: str = Field(...,example = 'Test_build_name')
    user_id: int = Field(...,gt=0, example=1)
    class_id: int = Field(...,gt=0, example=1)

    class Config:
        orm_mode = True

class URLSortBase(BaseModel):
    cycle: str = Field(...,example='Первое бытие')
    type: str = Field(...,example='Стартер')
    purpose: str = Field(...,example='Маппинг')
    class_id: int = Field(...,gt=0,example=1)

class URLCheckBase(BaseModel):
    id: int = Field(None, gt=0, example=1)
    name: str = Field(..., example='https://poeplanner.com/atlas-tree/BAAQAIQAJuaH1PP3Xz4PgWXyArZjD0sy67sklwBIHtey-uUxt-Vs8whDhrSxnyySEYQIesHuZIBtiMAq6ng8WSFgky14ZvI4jEEqbrVmpdrOAF6dzlrJ_Uy6jeqT8n7IqLz8-iq72Vt9Hsy3hqGvOr3a5PcfAKoKnzumNAf0TdfXK2iJZ2AqEntg1I-HnS370MbsDwLFtdiCp6FoKY2OOQF6fitZhnTSglGI6EU6ZjA342ayz0fhEBkKpXPiDqQFotDLFyFMxSEX3TUwx10XUDak9nUZlMGvOnbBdOXsOMZxC4_lAzCIB7cP1WnCdvrl2VypQ7VjoHHEGLli5DOar2-1mbkc3c776We51NAoFAAfiwgAAAAAAAADAwAAAAAAAAAAAA==')

    class Config:
        orm_mode = True

class EffectBase(BaseModel):
    id: int = Field(None, gt=0, example=1)
    name: str = Field(..., max_length=255, example='Culling')
    value: int = Field(..., gt=0,example=1)

    class Config:
        orm_mode = True

class PassiveBase(BaseModel):
    id: int = Field(None, gt=0, example=1)
    name: str = Field(..., max_length=255, example='Strike')
    desc: str = Field(..., max_length=255, example='Powerful Strike')
    image: str= Field(...,example='img/p1')
    
    class Config:
        orm_mode = True

# class PassiveEffectsBase(BaseModel):
#     id: int = Field(None, gt=0, example=1)
#     value : int = Field(..., gt=0,example=1)

#     class Config:
#         orm_mode = True

class ClassBase(BaseModel):
    id : int = Field(None, gt=0,example=1)
    name : str = Field(..., max_length=255, example='Strike')
    main_atr : str = Field(..., max_length=255, example='Strike')
    base_atrs : str = Field(..., max_length=255, example='Strike')
    base_hp : int = Field(..., gt=0,example=1)
    base_mp : int = Field(..., gt=0,example=1)
    base_armour : int = Field(..., gt=0,example=1)
    base_evade : int = Field(..., gt=0,example=1)
    base_elem_res : int = Field(..., gt=0,example=1)
    base_phys_res : int = Field(..., gt=0,example=1)

    class Config:
        orm_mode = True

class Affix_typeBase(BaseModel):
    id : int = Field(None, gt=0,example=1)
    name : str = Field(..., max_length=255, example='Strike')

    class Config:
        orm_mode = True

class Item_typeBase(BaseModel):
    id : int = Field(None, gt=0,example=1)
    name : str = Field(..., max_length=255, example='Strike')

    class Config:
        orm_mode = True

class AffixBase(BaseModel):
    id : int = Field(None, gt=0,example=1)
    effect : str = Field(...,example='Физ. урон')
    value_start : int = Field(...,gt=0,example=1)
    value_end : int = Field(...,gt=0,example=1)
    tag : str = Field(..., example='phys_damage')

    class Config:
        orm_mode = True

class Item_subtypeBase(BaseModel):
    id : int = Field(None, gt=0,example=1)
    name : str = Field(..., max_length=255, example='Strike')

    class Config:
        orm_mode = True

class Item_implicitBase(BaseModel):
    id : int = Field(None, gt=0,example=1)
    effect : str = Field(...,example='Физ. урон')
    value_start : int = Field(...,gt=0,example=1)
    value_end : int = Field(...,gt=0,example=1)
    tag : str = Field(..., example='phys_damage')
    class Config:
        orm_mode = True

class WeaponBase(BaseModel):
    id : int = Field(None, gt=0,example=1)
    name : str = Field(..., max_length=255, example='Strike')
    image: str = Field(None,example='/img/dagger/1')

    class Config:
        orm_mode = True

class ArmourBase(BaseModel):
    id : int = Field(None, gt=0,example=1)
    name : str = Field(..., max_length=255, example='Strike')
    image: str = Field(None,example='/img/armour/1')

    class Config:
        orm_mode = True

class AccessoryBase(BaseModel):
    id : int = Field(None, gt=0,example=1)
    name : str = Field(..., max_length=255, example='Strike')
    image: str = Field(None,example='/img/necklace/1')

    class Config:
        orm_mode = True