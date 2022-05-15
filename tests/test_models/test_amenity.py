#!/usr/bin/python3
"""test ok"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """test ok"""

    def __init__(self, *args, **kwargs):
        """test ok"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """test ok"""
        new = self.value()
        self.assertEqual(type(new.name), str)
