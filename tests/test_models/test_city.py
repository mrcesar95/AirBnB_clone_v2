#!/usr/bin/python3
"""test ok"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """test ok"""

    def __init__(self, *args, **kwargs):
        """test ok"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """test ok"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """test ok"""
        new = self.value()
        self.assertEqual(type(new.name), str)
