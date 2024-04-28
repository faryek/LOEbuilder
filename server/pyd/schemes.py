from .base_models import *
from typing import List


# class URLSSchema(URLBase):
#     user:List[UserBase]

# class UserSchema(UserBase):
#     role: List[RoleBase]

# class PassiveeffectsSchema(PassiveEffectsBase):
#     passives: List[PassiveBase]
#     effect: List[EffectBase]

# class AffixSchema(AffixBase):
#     affix_types:List[Affix_typeBase]
#     item_types:List[Item_typeBase]

# class ItemSubtypeSchema(Item_subtypeBase):
#     item_types: List[Item_typeBase]
#     item_implicits: List[Item_implicitBase]

# class ItemTypeSchema(Item_typeBase):
#     item_subtypes:List[Item_subtypeBase]

# class ItemImplicitsSchema(Item_implicitBase):
#     subtypes: List[Item_subtypeBase]

# class WeaponSchema(WeaponBase):
#     sub_ids:List[Item_subtypeBase]

# class ArmourSchema(ArmourBase):
#     sub_ids:List[Item_subtypeBase]

# class AccessorySchema(AccessoryBase):
#     sub_ids:List[Item_subtypeBase]

# # Схемы включают в себя ссылки на другие сущности для вложеного вывода
# # их нужно выносить отдельно, чтобы избежать рекурсии в импорте
# class CategorySchema(CategoryBase):
#     products: List[ProductBase]


# class ProductSchema(ProductBase):
#     categories: List[CategoryBase]
