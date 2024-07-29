from db.database import base
from sqlalchemy import String, Float, Integer, ForeignKey, Column, JSON
from sqlalchemy.orm import relationship


class User(base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password =  Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    name = Column(String)
    phone = Column(String)
    expenses = relationship('Expense', back_populates='owner')
    
class Expense(base):
    __tablename__ = 'expenses'
    
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    split_method = Column(String, nullable=False)
    split_details = Column(JSON, nullable=False)
    owner = relationship('User', back_populates='expenses')
    