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
    eff3 = models.Effect(name='intelligence', value=15)
    eff4 = models.Effect(name='dexterity', value=25)
    eff5 = models.Effect(name='strength', value=25)
    eff6 = models.Effect(name='intelligence', value=25)
    eff7 = models.Effect(name='vamp', value=10)
    eff8 = models.Effect(name='vamp', value=25)
    eff9 = models.Effect(name='critical_damage', value=20)
    eff10 = models.Effect(name='critical_chance', value=5)
    eff11 = models.Effect(name='vamp_chance', value=5)

    pas1 = models.Passive(
        name='Ловкость', desc='+15 к ловкости', effects=[eff], image='/img/icons/dexterity.png')
    pas2 = models.Passive(name='Сила', desc='+15 к силе',
                          effects=[eff2], image='/img/icons/strength.png')
    pas3 = models.Passive(
        name='Интеллект', desc='+15 к интеллекту', effects=[eff3], image='/img/icons/intelligence.png')
    pas4 = models.Passive(name='Суровая закалка',
                          desc='+25 к ловкости и силе', effects=[eff4, eff5], image='/img/icons/dexterity.png')
    pas5 = models.Passive(
        name='Скурпулезность', desc='+25 к ловкости и интеллекту', effects=[eff4, eff6], image='/img/icons/intelligence.png')
    pas6 = models.Passive(name='Поломничество',
                          desc='+25 к интеллекту и силе', effects=[eff5, eff6], image='/img/icons/strength.png')
    pas7 = models.Passive(
        name='Вампир', desc='+10% вампиризма', effects=[eff7], image='/img/icons/strength.png')
    pas8 = models.Passive(name='Истинный вампир',
                          desc='+25% вампиризма', effects=[eff8], image='/img/icons/strength.png')
    pas9 = models.Passive(name="Большая сила", effects=[
                          eff5], desc='', image='/img/icons/strength.png')
    pas10 = models.Passive(name="Большая ловкость", effects=[
                           eff4], desc='', image='/img/icons/dexterity.png')
    pas11 = models.Passive(name="Большой интеллект", effects=[
                           eff6], desc='', image='/img/icons/intelligence.png')
    pas12 = models.Passive(name="Крит. шанс", effects=[
                           eff9], desc='', image='/img/icons/dexterity.png')
    pas13 = models.Passive(name="Крит. урон", effects=[
                           eff10], desc='', image='/img/icons/dexterity.png')
    pas14 = models.Passive(name="Шанс вампиризма", effects=[
                           eff11], desc='', image='/img/icons/intelligence.png')

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
    itemtype5 = models.Item_type(name='Второстепенное')

    afx1 = models.Affix(effect='Увеличенный физ. урон', value_start=10,
                        value_end=50, tag='phys_damage', affix_types=afxtype1, item_types=itemtype)
    afx2 = models.Affix(effect='Увеличенный маг. урон', value_start=10,
                        value_end=50, tag='mag_damage', affix_types=afxtype1, item_types=itemtype)
    afx3 = models.Affix(effect='Увеличенный вампиризм', value_start=10,
                        value_end=50, tag='vamp', affix_types=afxtype2, item_types=itemtype)
    afx4 = models.Affix(effect='Увеличенная ловкость', value_start=10,
                        value_end=50, tag='dexterity', affix_types=afxtype2, item_types=itemtype3)
    afx5 = models.Affix(effect='Увеличенная сила', value_start=10,
                        value_end=50, tag='strength', affix_types=afxtype2, item_types=itemtype3)
    afx6 = models.Affix(effect='Увеличенный интеллект', value_start=10,
                        value_end=50, tag='intelligence', affix_types=afxtype2, item_types=itemtype3)
    afx7 = models.Affix(effect='Увеличенный физ. урон', value_start=40,
                        value_end=80, tag='phys_damage', affix_types=afxtype1, item_types=itemtype4)
    afx8 = models.Affix(effect='Увеличенный маг. урон', value_start=40,
                        value_end=90, tag='mag_damage', affix_types=afxtype1, item_types=itemtype4)
    afx9 = models.Affix(effect='Увеличенный вампиризм', value_start=40,
                        value_end=90, tag='vamp', affix_types=afxtype1, item_types=itemtype4)
    afx10 = models.Affix(effect='Увеличенная ловкость', value_start=40,
                         value_end=60, tag='dexterity', affix_types=afxtype1, item_types=itemtype2)
    afx11 = models.Affix(effect='Увеличенная сила', value_start=40,
                         value_end=60, tag='strength', affix_types=afxtype1, item_types=itemtype2)
    afx12 = models.Affix(effect='Увеличенный интеллект', value_start=40,
                         value_end=60, tag='intelligence', affix_types=afxtype1, item_types=itemtype2)

    itemImplicit = models.Item_implicit(
        effect='Физ. урон', value_start=1, value_end=10, tag='phys_damage')
    itemImplicit2 = models.Item_implicit(
        effect='Сопротивление элем. урону', value_start=1, value_end=10, tag='ele_res')
    itemImplicit3 = models.Item_implicit(
        effect='Шанс крита', value_start=1, value_end=21, tag='critical_chance')
    itemImplicit7 = models.Item_implicit(
        effect='Сопротивление физ урону', value_start=1, value_end=21, tag='phys_res')
    itemImplicit8 = models.Item_implicit(
        effect='Маг. урон', value_start=1, value_end=21, tag='magic_damage')

    itemsubtype1 = models.Item_subtype(name='Кинжал', item_types=[
        itemtype], item_implicits=[itemImplicit3])
    itemsubtype2 = models.Item_subtype(name='Шлем', item_types=[
        itemtype2], item_implicits=[itemImplicit2])
    itemsubtype3 = models.Item_subtype(name='Ожерелье', item_types=[
        itemtype3], item_implicits=[itemImplicit3])
    itemsubtype5 = models.Item_subtype(name='Одноручный меч', item_types=[
        itemtype], item_implicits=[itemImplicit])
    itemsubtype6 = models.Item_subtype(name='Двуручный меч', item_types=[
        itemtype], item_implicits=[itemImplicit])
    itemsubtype7 = models.Item_subtype(name='Скипетр', item_types=[
        itemtype], item_implicits=[itemImplicit8])
    itemsubtype8 = models.Item_subtype(name='Кольцо', item_types=[
        itemtype3], item_implicits=[itemImplicit2])
    itemsubtype9 = models.Item_subtype(name='Кольцо', item_types=[
        itemtype3], item_implicits=[itemImplicit7])
    itemsubtype10 = models.Item_subtype(name='Кольцо', item_types=[
        itemtype3], item_implicits=[itemImplicit8])
    itemsubtype12 = models.Item_subtype(name='Нагрудник', item_types=[
        itemtype2], item_implicits=[itemImplicit7])
    itemsubtype13 = models.Item_subtype(name='Наручи', item_types=[
        itemtype2], item_implicits=[itemImplicit7])
    itemsubtype15 = models.Item_subtype(name='Щит', item_types=[
        itemtype5], item_implicits=[itemImplicit7])
    itemsubtype16 = models.Item_subtype(name='Катализатор', item_types=[
        itemtype5], item_implicits=[itemImplicit8])
    itemsubtype17 = models.Item_subtype(name='Ремень', item_types=[
        itemtype2], item_implicits=[itemImplicit7])
    itemsubtype18 = models.Item_subtype(name='Реликвия', item_types=[
        itemtype3], item_implicits=[itemImplicit7])
    itemsubtype19 = models.Item_subtype(name='Ботинки', item_types=[
        itemtype2], item_implicits=[itemImplicit7])

    wpn1 = models.Weapon(
        name='Костяной', sub_id=itemsubtype1, image='/img/items/one_hand_sword_1.png')
    wpn2 = models.Weapon(
        name='Стальной', sub_id=itemsubtype1, image='/img/items/dagger_1.png')
    wpn3 = models.Weapon(
        name='Стальной', sub_id=itemsubtype5, image='/img/items/one_hand_axe_1.png')
    wpn4 = models.Weapon(
        name='Стальной', sub_id=itemsubtype6, image='/img/items/one_hand_axe_2.png')
    wpn5 = models.Weapon(
        name='Стальной', sub_id=itemsubtype15, image='/img/items/shield_1.png')
    wpn6 = models.Weapon(
        name='Стальной', sub_id=itemsubtype16, image='/img/items/catalyst_1.png')

    armr1 = models.Armour(
        name='Рогатый', sub_id=itemsubtype2, image='/img/items/head_1.png')
    armr2 = models.Armour(
        name='Рогатый', sub_id=itemsubtype12, image='/img/items/body_1.png')
    armr3 = models.Armour(
        name='Рогатые', sub_id=itemsubtype13, image='/img/items/gloves_1.png')
    armr4 = models.Armour(
        name='Рогатые', sub_id=itemsubtype19, image='/img/items/boots_1.png')
    armr5 = models.Armour(
        name='Рогатый', sub_id=itemsubtype17, image='/img/items/belt_1.png')

    accry1 = models.Accessory(
        name='Изумрудное', sub_id=itemsubtype3, image='/img/items/neck_1.png')
    accry2 = models.Accessory(
        name='Изумрудное', sub_id=itemsubtype9, image='/img/items/ring_2.png')
    accry3 = models.Accessory(
        name='Кровавое', sub_id=itemsubtype10, image='/img/items/ring_3.png')
    accry4 = models.Accessory(
        name='Ониксовое', sub_id=itemsubtype8, image='/img/items/ring_4.png')
    accry5 = models.Accessory(
        name='Ониксовое', sub_id=itemsubtype18, image='/img/items/relic_1.png')

    session.add_all([role1, eff, eff2, eff3, eff4, eff5, eff6, eff7, eff8, eff9, eff10, eff11,
                    pas1, pas2, pas3, pas4, pas5, pas6, pas7, pas8, pas9, pas10, pas11, pas12, pas13, pas14,
                    cls1, cls2, cls3, cls4, cls5, cls6, cls7, cls8,
                    afxtype1, afxtype2,
                    itemtype, itemtype2, itemtype3, itemtype4, itemtype5,
                    afx1, afx2, afx3, afx4, afx5, afx6, afx7, afx8, afx9, afx10, afx11, afx12,
                    itemImplicit, itemImplicit2, itemImplicit3, itemImplicit7,itemImplicit8,
                    itemsubtype1, itemsubtype2, itemsubtype3, itemsubtype5, itemsubtype6, itemsubtype7, itemsubtype8,
                    itemsubtype9, itemsubtype10, itemsubtype12, itemsubtype13, itemsubtype17,
                    itemsubtype16, itemsubtype18, itemsubtype19, itemsubtype15,
                    wpn1, wpn2, wpn3, wpn4, wpn5, wpn6,
                    armr1, armr2, armr3, armr4, armr5,
                    accry1, accry2, accry3, accry4, accry5
                     ])
    session.commit()
