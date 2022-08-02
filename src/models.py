import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
# User = possible customer
   __tablename__ = 'User'
   id = Column(Integer, primary_key=True)
   name = Column(String(50), nullable=False)
   last_name = Column(String(50), nullable=False)
   email = Column(String(40), nullable=False)
   addres = Column(String(200), nullable=False)
   Phone_Number = Column(String(20), nullable=False)
   bith_date = Column(String(12), nullable=False)
   
class Character(Base):
   __tablename__ = 'Character'
   id = Column(Integer, primary_key=True)
   name = Column(String(50), nullable=False)
   age = Column(String(10),)
   faction = Column(String(10),)
   race = Column(String(10),)
   clase = Column(String(10), nullable=False)

class Planets(Base):
   __tablename__ = 'Planets'
   id = Column(Integer, primary_key=True)
   name = Column(String(50), nullable=False)
   weigth = Column(Integer, nullable=False)
   size = Column(Integer, nullable=False)
   galaxy = Column(String(50), nullable=False)

class UserFavoritePlanets(Base):
    __tablename__ = 'UserFavoritePlanets'
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('User.id'))
    User = relationship(User)
    Planets_id = Column(Integer, ForeignKey('Planets.id'))
    Planets = relationship(Planets)


class UserFavoriteCharacters(Base):
   __tablename__ = 'UserFavoriteCharacters'
   id = Column(Integer, primary_key=True)
   User_id = Column(Integer, ForeignKey('User.id'))
   User = relationship(User)
   Characater_id = Column(Integer, ForeignKey('Character.id'))
   Character = relationship(Character)

class ShoppingCart(Base):
   __tablename__ = 'ShoppingCart'
   id = Column(Integer, primary_key=True)
   User_id = Column(Integer, ForeignKey('User.id'))
   User = relationship(User)
   Planets_id = Column(Integer, ForeignKey('Planets.id'))   
   Planets = relationship(Planets)
   Characater_id = Column(Integer, ForeignKey('Character.id'))
   Character = relationship(Character)

class Order(Base):
   __tablename__ = 'Order'
   id = Column(Integer, primary_key=True)
   User_id = Column(Integer, ForeignKey('User.id'))
   User = relationship(User)
   ShoppingCart_id = Column(Integer, ForeignKey('ShoppingCart.id'))
   ShoppingCart = relationship(ShoppingCart)

class OrderDetails(Base):
   __tablename__ = 'OrderDetails'
   id = Column(Integer, primary_key=True)
   User_id = Column(Integer, ForeignKey('User.id'))
   User = relationship(User)
   Order_id = Column(Integer, ForeignKey('Order.id'))
   Order = relationship(Order)

class ShippingAddres(Base):
   __tablename__ = 'ShippingAddres'
   id = Column(Integer, primary_key=True)
   User_id = Column(Integer, ForeignKey('User.id'))
   User = relationship(User)
   OrderDetails_id = Column(Integer, ForeignKey('OrderDetails.id'))
   OrderDetails = relationship(OrderDetails)

 
   
def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')