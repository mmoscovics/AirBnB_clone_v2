#!/usr/bin/python3
"""This is the state class"""
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete',
                              backref='state')
    else:

        @property
        def cities(self):
            """[<8;62;23m]
            Returns the list of City instances with
            state_id equals to the current State.id
            """
            city_list = []

            for key, value in models.storage().all():
                inst = key.split('.')
                name_inst = inst[0]
                if name_inst == "City":
                    if value.state_id == self.id:
                        city_list.append(value)
            return city_list
