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
    role1 = models.Role(name = 'user')

    eff = models.Effect(name='dexterity', value=15)
    eff2 = models.Effect(name='strength', value=15)

    pas1 = models.Passive(
        name='Ловкость', desc='+15 к ловкости', effects=[eff])
    pas2 = models.Passive(name='Сила', desc='+15 к силе', effects=[eff2])

    # pasEff = models.Passive_effects(
    #     value=10, passives=[pas1, pas2], effects=[eff])

    cls1 = models.Class(name='Богатырь', main_atr='сила', base_atrs='60, 20, 20', base_hp=1000, base_mp=50,
                        base_armor=50, base_evade=10, base_ele_res=30, base_phys_res=50)

    afxtype = models.Affix_type(name='prefix')

    itemtype = models.Item_type(name='Одноручное')
    itemtype2 = models.Item_type(name='Броня')
    itemtype3 = models.Item_type(name='Аксессуары')

    afx = models.Affix(effect='Увеличенный физ. урон', value_start=10,
                       value_end=50, affix_types=afxtype, item_types=itemtype)

    itemImplicit = models.Item_implicit(
        effect='Физ. урон', value_start=1, value_end=2)
    
    itemImplicit2 = models.Item_implicit(
        effect='Сопротивление огню', value_start=1, value_end=2)
    
    itemImplicit3 = models.Item_implicit(
        effect='Шанс крита', value_start=1, value_end=2)

    itemsubtype1 = models.Item_subtype(name='Кинжал', item_types=[
        itemtype], item_implicits=[itemImplicit], image='/img/knife')

    itemsubtype2 = models.Item_subtype(name='Шлем', item_types=[
        itemtype2], item_implicits=[itemImplicit2], image='/img/helmet')

    itemsubtype3 = models.Item_subtype(name='Ожерелье', item_types=[
        itemtype3], item_implicits=[itemImplicit3], image='/img/necklace')

    wpn1 = models.Weapon(name='Костяной', sub_id=itemsubtype1)

    armr1 = models.Armour(name='Рогатый', sub_id=itemsubtype2)

    accry1 = models.Accessory(name='Изумрудное', sub_id=itemsubtype3)

    session.add_all([eff, eff2, pas1, pas2, cls1, afxtype,
                    itemtype, itemtype2, itemtype3, afx, itemImplicit,itemImplicit2,itemImplicit3, itemsubtype1, itemsubtype2, itemsubtype3,
                    wpn1, armr1, accry1
                     ])
    session.commit()
