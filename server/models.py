from sqlalchemy import Numeric, Table, Boolean, Column, ForeignKey, Integer, String, Date, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.sql import func

item_type_subtypes = Table('item_type_subtypes', Base.metadata,
                           Column('type_id', ForeignKey(
                               'item_types.id'), primary_key=True),
                           Column('sub_id', ForeignKey(
                               'item_subtypes.id'), primary_key=True),
                           )

subtype_implicits = Table('subtype_implicits', Base.metadata,
                          Column('sub_id', ForeignKey(
                              'item_subtypes.id'), primary_key=True),
                          Column('implicit_id', ForeignKey(
                              'item_implicits.id'), primary_key=True),
                          )

passive_effects = Table('passive_effects', Base.metadata,
                        Column('passive_id', ForeignKey(
                            'passives.id'), primary_key=True),
                        Column('effect_id', ForeignKey(
                            'effects.id'), primary_key=True),
                        )


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255),nullable=False,unique=True)
    email = Column(String(255), nullable=False, unique=True)
    pwd = Column(String(255), nullable=False)
    birthday = Column(Date(), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), default=1)

    role = relationship('Role', backref="users")


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), default=1)

    user = relationship('User', backref='urls')


class Effect(Base):
    __tablename__ = "effects"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    value = Column(Integer)


class Passive(Base):
    __tablename__ = "passives"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    desc = Column(String(255))

    effects = relationship(
        'Effect', secondary='passive_effects', backref='passives')

# class Passive_effects(Base):
#     __tablename__="passive_effects"
#     id = Column(Integer,primary_key=True)
#     value = Column(Integer)

#     effect_id = Column(Integer,ForeignKey('effects.id'),nullable=False)
#     passive_id= Column(Integer,ForeignKey('passives.id'),nullable=False)

#     passives = relationship('Passive',backref='passive_effects')
#     effects = relationship('Effect',backref='passive_effects')


class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    main_atr = Column(String(255))
    base_atrs = Column(String(255))
    base_hp = Column(Integer, default=1)
    base_mp = Column(Integer, default=1)
    base_armor = Column(Integer, default=1)
    base_evade = Column(Integer, default=1)
    base_ele_res = Column(Integer, default=1)
    base_phys_res = Column(Integer, default=1)


class Affix_type(Base):
    __tablename__ = "affix_types"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))


class Item_type(Base):
    __tablename__ = "item_types"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))


class Affix(Base):
    __tablename__ = "affixes"
    id = Column(Integer, primary_key=True)
    affix_type_id = Column(Integer, ForeignKey(
        'affix_types.id'), default=1, nullable=False)
    item_type_id = Column(Integer, ForeignKey(
        'item_types.id'), default=1, nullable=False)
    effect = Column(String(255))
    value_start = Column(Integer, default=1)
    value_end = Column(Integer, default=1)

    affix_types = relationship('Affix_type', backref='affixes')
    item_types = relationship('Item_type', backref='affixes')


class Item_implicit(Base):
    __tablename__ = "item_implicits"
    id = Column(Integer, primary_key=True)
    effect = Column(String(255))
    value_start = Column(Integer, default=1)
    value_end = Column(Integer, default=1)


class Item_subtype(Base):
    __tablename__ = "item_subtypes"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    item_types = relationship(
        "Item_type", secondary="item_type_subtypes", backref="item_subtypes")
    item_implicits = relationship(
        "Item_implicit", secondary="subtype_implicits", backref="item_subtypes")


class Weapon(Base):
    __tablename__ = "weapons"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    image = Column(String)

    sub_ids = Column(Integer, ForeignKey('item_subtypes.id'), default=1)

    sub_id = relationship('Item_subtype', backref='weapons')


class Armour(Base):
    __tablename__ = "armour"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    image = Column(String)

    sub_ids = Column(Integer, ForeignKey('item_subtypes.id'), default=1)

    sub_id = relationship('Item_subtype', backref='armour')


class Accessory(Base):
    __tablename__ = "accessories"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    image = Column(String)

    sub_ids = Column(Integer, ForeignKey('item_subtypes.id'), default=1)

    sub_id = relationship('Item_subtype', backref='accessories')
