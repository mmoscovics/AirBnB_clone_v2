#!/usr/bin/python3
"""test for databse storage"""
import unittest
import pep8
import json
import os
import MySQLdb
from models.base_model import BaseModel, Base
from models.engine.db_storage import DBStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship


class TestDatabaseStorage(unittest.TestCase):
    '''this will test the database'''

    @classmethod
    def setUpClass(cls):
        """
        set up for test
        """
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = DBStorage()

    def setUp(self):
        """
        Setup unit test
        """

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db",
                     "db isn't being used")
    def test_all(self):
        """tests if all works in File Storage"""
        storage = DBStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._DBStorage__objects)

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


if __name__ == "__main__":
    unittest.main()
