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

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagrama.png')
    print("Bien! diagrama.png generado")
except Exception as e:
    print("Comprueba el código algún error hay...")
    raise e