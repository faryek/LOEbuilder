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

    user1 = models.User(username='xd', password='xdpass', role=role1)

    url1 = models.URL(name='xdddddddd', user=user1)

    eff = models.Effect(name='Uber')

    pas1 = models.Passive(name='Dexterity', desc='+15 dex')
    pas2 = models.Passive(name='Strength', desc='+15 str')

    PasEff = models.Passive_effects(
        value=10, passives=[pas1, pas2], effects=[eff])

    cls1 = models.Class(name='Богатырь', main_atr='str', base_atrs=[
                        60, 20, 20], base_hp=1000, base_mp=50,
                        base_armor=50, base_evade=10, base_ele_res=30, base_phys_res=50)

    afxtype = models.Affix_type(name='strong')

    itemtype = models.Item_type(name='weapon')

    afx = models.Affix(effect='Giga', value_start=10,
                       value_end=50, affix_types=afxtype, item_types=itemtype)

    itemImplicit = models.Item_implicit(
        effect='strhiga', value_start=1, value_end=2)

    itemsubtype = models.Item_subtype(name='lmaostr', item_types=[
                                      itemtype], item_implicits=[itemImplicit])

    wpn1 = models.Weapon(name='hatchet', sub_ids=itemsubtype)

    armr1 = models.Armour(name='chestplate', sub_ids=itemsubtype)

    accry1 = models.Armour(name='necklace', sub_ids=itemsubtype)

    session.add_all([role1, user1, url1, eff, pas1, pas2, PasEff, cls1, afxtype,
                    itemtype, afx, itemImplicit, itemsubtype, wpn1, armr1, accry1])
    session.commit()
