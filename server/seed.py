# вставка начальных данных
from sqlalchemy.orm import Session
from database import engine
import models

models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session:
    # cat1 = models.Category(name='Еда', description='Вкусная, для людей')
    # cat2 = models.Category(name='Вода', description='Без вкуса, для людей')
    # cat3 = models.Category(name='Одежда', description='Без стиля, для людей')

    # prod1 = models.Product(name='Дошик', description='Не вкусный, для студентов', price=66.5,categories=[cat1])
    # prod2 = models.Product(name='Святой источник', description='Обычная вода, для людей', price=33.4,categories=[cat2])
    # prod3 = models.Product(name='Кепка ОДМО', description='Специально для ОДМОшников', price=350.0,categories=[cat3])
    # session.add_all([cat1, cat2, cat3, prod1, prod2, prod3])

    role1 = models.Role(name='parjur')

    user1 = models.User(username='xd',password='xdpass',role=role1)

    url1 = models.URL(name = 'xdddddddd',user = [user1])

    session.add_all([role1,user1,url1])
    session.commit()
