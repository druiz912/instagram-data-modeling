import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    mail = Column(String, unique = True)
    password = Column(String)

class Followers(Base):
    __tablename__ = 'Followers'
    id = Column(Integer, primary_key=True)
    user_From_id = Column(Integer, ForeignKey('User.id'))
    user_To_id = Column(Integer, ForeignKey('User.id'))

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    description = Column(String, nullable = True)

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('Post.id'))
    source_Media = Column(String)
    type_Media = Column(String)  

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('Post.id'))
    user_id = Column(Integer, ForeignKey('User.id'))
    comment = Column(String)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagrama.png')
    print("Bien! diagrama.png generado")
except Exception as e:
    print("Comprueba el código algún error hay...")
    raise e