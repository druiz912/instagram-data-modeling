import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), unique=True, nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    password= Column(Integer, unique=False, nullable=False)
    posts = relationship('post', backref='usuario', lazy=True)
    friends = relationship('friend', backref='usuario', lazy=True)
    followers = relationship('followers', backref='usuario', lazy=True)
    my_saved= relationship('saved', backref='usuario', lazy=True)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(100),unique=False, nullable=False)
    text = Column(String(300),unique=False, nullable=False)
    location = Column(String(100), unique=False, nullable=True)
    likes = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    saved_post = relationship('saved', backref='post',lazy=True)

class Friend(Base):
    __tablename__ = 'friends'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    friend_id = Column(Integer, ForeignKey('usuario.id'))

class BestFriends(Base):
    __tablename__="bestfriends"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    friend_id = Column(Integer,ForeignKey('usuario.id'))

class Follower(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    follower_id = Column(Integer, ForeignKey('usuario.id'))


class Saved(Base):
    __tablename__ = 'saved'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagrama.png')
    print("Bien! diagrama.png generado")
except Exception as e:
    print("Comprueba el código algún error hay")
    raise e