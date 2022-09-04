import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
class Users(Base):
    __tablename__ = 'users'
    id_user = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(12), nullable=False)
    favourites = relationship("Favourites", backref= "users", lazy=True)

class Planets(Base):
    __tablename__ = 'planets'
    id_planets = Column(Integer, primary_key=True)
    name_planets = Column(String(30))
    coordinates = Column(Integer, nullable=True)

class Characters(Base):
    __tablename__ = 'characters'
    id_characters = Column(Integer, primary_key=True)
    name_characters = Column(String(30))
    breed = Column(String(30))

class Starships(Base):
    __tablename__ = 'starships'
    id_starship = Column(Integer, primary_key=True)
    name_starship = Column(String(30))
    origin = Column(String(50))

class Favourites(Base):
    __tablename__ = 'favorites'
    id_favourite = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id_user'), nullable=False)
    id_planets = Column(Integer, ForeignKey('planets.id_planet'))
    id_characters = Column(Integer, ForeignKey('characters.id_character'))
    id_starship = Column(Integer, ForeignKey('starships.id_starship'))    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagrama.png')
    print("Bien! diagrama.png generado")
except Exception as e:
    print("Comprueba el código algún error hay...")
    raise e