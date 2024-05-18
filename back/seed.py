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
    role1 = models.Role(name='user')

    eff = models.Effect(name='dexterity', value=15)
    eff2 = models.Effect(name='strength', value=15)
    eff3 = models.Effect(name='Intelligence', value=15)
    eff4 = models.Effect(name='dexterity', value=25)
    eff5 = models.Effect(name='strength', value=25)
    eff6 = models.Effect(name='Intelligence', value=25)
    eff7 = models.Effect(name='Vampirism', value=10)
    eff8 = models.Effect(name='Vampirism', value=25)

    pas1 = models.Passive(
        name='Ловкость', desc='+15 к ловкости', effects=[eff])
    pas2 = models.Passive(name='Сила', desc='+15 к силе', effects=[eff2])
    pas3 = models.Passive(
        name='Интеллект', desc='+15 к интеллекту', effects=[eff3])
    pas4 = models.Passive(name='Суровая закалка',
                          desc='+25 к ловкости и силе', effects=[eff4, eff5])
    pas5 = models.Passive(
        name='Скурпулезность', desc='+25 к ловкости и интеллекту', effects=[eff4, eff6])
    pas6 = models.Passive(name='Поломничество',
                          desc='+25 к интеллекту и силе', effects=[eff5, eff6])
    pas7 = models.Passive(
        name='Вампир', desc='+25 к ловкости и интеллекту', effects=[eff7])
    pas8 = models.Passive(name='Истинный вампир',
                          desc='+25 к интеллекту и силе', effects=[eff8])

    # pasEff = models.Passive_effects(
    #     value=10, passives=[pas1, pas2], effects=[eff])

    cls1 = models.Class(name='Богатырь', main_atr='Сила', base_atrs='60, 20, 20', base_hp=1000, base_mp=50,
                        base_armor=50, base_evade=10, base_ele_res=30, base_phys_res=50)
    cls2 = models.Class(name='Антихрист', main_atr='Ловкость', base_atrs='20, 60, 20', base_hp=600, base_mp=70,
                        base_armor=30, base_evade=50, base_ele_res=40, base_phys_res=30)
    cls3 = models.Class(name='Боголюб', main_atr='Интеллект', base_atrs='20, 20, 60', base_hp=500, base_mp=100,
                        base_armor=40, base_evade=10, base_ele_res=20, base_phys_res=30)
    cls4 = models.Class(name='Налётчик', main_atr='Сила', base_atrs='30, 50, 10', base_hp=900, base_mp=40,
                        base_armor=50, base_evade=40, base_ele_res=40, base_phys_res=50)
    cls5 = models.Class(name='Богохульник', main_atr='Интеллект', base_atrs='10, 40, 50', base_hp=450, base_mp=90,
                        base_armor=30, base_evade=30, base_ele_res=20, base_phys_res=30)
    cls6 = models.Class(name='Скоморох', main_atr='Ловкость', base_atrs='10, 60, 30', base_hp=400, base_mp=60,
                        base_armor=50, base_evade=30, base_ele_res=30, base_phys_res=30)
    cls7 = models.Class(name='Язычница', main_atr='Интеллект', base_atrs='10, 10, 70', base_hp=350, base_mp=120,
                        base_armor=20, base_evade=20, base_ele_res=50, base_phys_res=30)
    cls8 = models.Class(name='Застрельщица', main_atr='Ловкость', base_atrs='10, 70, 10', base_hp=350, base_mp=40,
                        base_armor=30, base_evade=70, base_ele_res=30, base_phys_res=30)

    afxtype1 = models.Affix_type(name='prefix')
    afxtype2 = models.Affix_type(name='suffix')

    itemtype = models.Item_type(name='Одноручное')
    itemtype2 = models.Item_type(name='Броня')
    itemtype3 = models.Item_type(name='Аксессуары')
    itemtype4 = models.Item_type(name='Двуручное')

    afx1 = models.Affix(effect='Увеличенный физ. урон', value_start=10,
                        value_end=50, affix_types=afxtype1, item_types=itemtype)
    afx2 = models.Affix(effect='Увеличенный маг. урон', value_start=10,
                        value_end=50, affix_types=afxtype1, item_types=itemtype)
    afx3 = models.Affix(effect='Увеличенный вампиризм', value_start=10,
                        value_end=50, affix_types=afxtype2, item_types=itemtype)
    afx4 = models.Affix(effect='Увеличенная ловкость', value_start=10,
                        value_end=50, affix_types=afxtype2, item_types=itemtype3)
    afx5 = models.Affix(effect='Увеличенная сила', value_start=10,
                        value_end=50, affix_types=afxtype2, item_types=itemtype3)
    afx6 = models.Affix(effect='Увеличенный интеллект', value_start=10,
                        value_end=50, affix_types=afxtype2, item_types=itemtype3)
    afx7 = models.Affix(effect='Увеличенный физ. урон', value_start=40,
                        value_end=80, affix_types=afxtype1, item_types=itemtype4)
    afx8 = models.Affix(effect='Увеличенный маг. урон', value_start=40,
                        value_end=90, affix_types=afxtype1, item_types=itemtype4)
    afx9 = models.Affix(effect='Увеличенный вампиризм', value_start=40,
                        value_end=90, affix_types=afxtype1, item_types=itemtype4)
    afx10 = models.Affix(effect='Увеличенная ловкость', value_start=40,
                         value_end=60, affix_types=afxtype1, item_types=itemtype2)
    afx11 = models.Affix(effect='Увеличенная сила', value_start=40,
                         value_end=60, affix_types=afxtype1, item_types=itemtype2)
    afx12 = models.Affix(effect='Увеличенный интеллект', value_start=40,
                         value_end=60, affix_types=afxtype1, item_types=itemtype2)

    itemImplicit = models.Item_implicit(
        effect='Физ. урон', value_start=1, value_end=10)

    itemImplicit2 = models.Item_implicit(
        effect='Сопротивление огню', value_start=1, value_end=10)

    itemImplicit3 = models.Item_implicit(
        effect='Шанс крита', value_start=1, value_end=21)

    itemImplicit4 = models.Item_implicit(
        effect='Сопротивление холоду', value_start=1, value_end=21)

    itemImplicit5 = models.Item_implicit(
        effect='Сопротивление яду', value_start=1, value_end=21)

    itemImplicit6 = models.Item_implicit(
        effect='Сопротивление бездне', value_start=1, value_end=21)

    itemImplicit7 = models.Item_implicit(
        effect='Сопротивление молнии', value_start=1, value_end=21)

    itemImplicit8 = models.Item_implicit(
        effect='Сопротивление некротическому урону', value_start=1, value_end=21)

    itemsubtype1 = models.Item_subtype(name='Кинжал', item_types=[
        itemtype], item_implicits=[itemImplicit3])

    itemsubtype2 = models.Item_subtype(name='Шлем', item_types=[
        itemtype2], item_implicits=[itemImplicit2])

    itemsubtype3 = models.Item_subtype(name='Ожерелье', item_types=[
        itemtype3], item_implicits=[itemImplicit3])

    itemsubtype5 = models.Item_subtype(name='Одноручный меч', item_types=[
        itemtype], item_implicits=[itemImplicit])

    itemsubtype6 = models.Item_subtype(name='Двуручный меч', item_types=[
        itemtype], item_implicits=[itemImplicit8])

    itemsubtype7 = models.Item_subtype(name='Скипетр', item_types=[
        itemtype], item_implicits=[itemImplicit6])

    itemsubtype8 = models.Item_subtype(name='Кольцо', item_types=[
        itemtype3], item_implicits=[itemImplicit5])

    itemsubtype9 = models.Item_subtype(name='Кольцо', item_types=[
        itemtype3], item_implicits=[itemImplicit7])

    itemsubtype10 = models.Item_subtype(name='Кольцо', item_types=[
        itemtype3], item_implicits=[itemImplicit4])

    itemsubtype12 = models.Item_subtype(name='Нагрудник', item_types=[
        itemtype2], item_implicits=[itemImplicit5])

    itemsubtype13 = models.Item_subtype(name='Наручи', item_types=[
        itemtype2], item_implicits=[itemImplicit6])

    itemsubtype14 = models.Item_subtype(name='Поножи', item_types=[
        itemtype2], item_implicits=[itemImplicit7])

    wpn1 = models.Weapon(
        name='Костяной', sub_id=itemsubtype1, image='/img/knife')
    wpn2 = models.Weapon(
        name='Стальной', sub_id=itemsubtype1, image='/img/knife')
    wpn3 = models.Weapon(
        name='Стальной', sub_id=itemsubtype5, image='/img/knife')
    wpn4 = models.Weapon(
        name='Стальной', sub_id=itemsubtype6, image='/img/knife')

    armr1 = models.Armour(
        name='Рогатый', sub_id=itemsubtype2, image='/img/helmet')
    armr2 = models.Armour(
        name='Рогатый', sub_id=itemsubtype12, image='/img/Chest')
    armr3 = models.Armour(
        name='Рогатый', sub_id=itemsubtype13, image='/img/Gloves')
    armr4 = models.Armour(
        name='Рогатый', sub_id=itemsubtype14, image='/img/Pants')

    accry1 = models.Accessory(
        name='Изумрудное', sub_id=itemsubtype3, image='/img/emerald_neck')
    accry2 = models.Accessory(
        name='Изумрудное', sub_id=itemsubtype9, image='/img/emerald_ring')
    accry3 = models.Accessory(
        name='Кровавое', sub_id=itemsubtype10, image='/img/blood_ring')
    accry4 = models.Accessory(
        name='Ониксовое', sub_id=itemsubtype8, image='/img/Onyx_ring')

    session.add_all([role1, eff, eff2, eff3, eff4, eff5, eff6, eff7, eff8,
                    pas1, pas2, pas3, pas4, pas5, pas6, pas7, pas8,
                    cls1, cls2, cls3, cls4, cls5, cls6, cls7, cls8,
                    afxtype1, afxtype2,
                    itemtype, itemtype2, itemtype3, itemtype4,
                    afx1, afx2, afx3, afx4, afx5, afx6, afx7, afx8, afx9, afx10, afx11, afx12,
                    itemImplicit, itemImplicit2, itemImplicit3,itemImplicit4,itemImplicit5,itemImplicit6,itemImplicit7,itemImplicit8,
                    itemsubtype1, itemsubtype2, itemsubtype3,itemsubtype5,itemsubtype6,itemsubtype7,itemsubtype8,itemsubtype9,itemsubtype10,itemsubtype12,itemsubtype13,itemsubtype14,
                    wpn1,wpn2,wpn3,wpn4,
                    armr1,armr2,armr3,armr4,
                    accry1,accry2,accry3,accry4,
                    ])
    session.commit()
