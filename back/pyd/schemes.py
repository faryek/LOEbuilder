from .base_models import *
from typing import List

class UserSchema(UserBase):
    role: RoleBase

class URLSSchema(URLBase):
    user: UserSchema
    clas: ClassBase

# class PassiveEffectsSchema(PassiveEffectsBase):
#     passives: List[PassiveBase]
#     effects: List[EffectBase]

class PassiveSchema(PassiveBase):
    effects: List[EffectBase]

class EffectSchema(EffectBase):
    passives: List[PassiveBase]

class AffixesSchema(AffixBase):
    affix_types: Affix_typeBase
    item_types: Item_typeBase

class Item_typeSchema(Item_typeBase):
    item_subtypes:List[Item_subtypeBase]

class Item_subtypeSchema(Item_subtypeBase):
    item_types: List[Item_typeBase]
    item_implicits: List[Item_implicitBase]

class ItemImplicitsSchema(Item_implicitBase):
    subtypes: List[Item_subtypeBase]

class WeaponsSchema(WeaponBase):
    sub_id: Item_subtypeSchema

class ArmourSchema(ArmourBase):
    sub_id: Item_subtypeSchema

class AccessorySchema(AccessoryBase):
    sub_id: Item_subtypeSchema




# # Схемы включают в себя ссылки на другие сущности для вложеного вывода
# # их нужно выносить отдельно, чтобы избежать рекурсии в импорте
# class CategorySchema(CategoryBase):
#     products: List[ProductBase]


# class ProductSchema(ProductBase):
#     categories: List[CategoryBase]
