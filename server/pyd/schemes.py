from .base_models import *
from typing import List

class UserSchema(UserBase):
    role: RoleBase

class URLSSchema(URLBase):
    user: UserSchema


# # Схемы включают в себя ссылки на другие сущности для вложеного вывода
# # их нужно выносить отдельно, чтобы избежать рекурсии в импорте
# class CategorySchema(CategoryBase):
#     products: List[ProductBase]


# class ProductSchema(ProductBase):
#     categories: List[CategoryBase]
