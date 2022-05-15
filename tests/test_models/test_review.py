#!/usr/bin/python3
"""test ok"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """test ok"""

    def __init__(self, *args, **kwargs):
        """test ok"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """test ok"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """test ok"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """test ok"""
        new = self.value()
        self.assertEqual(type(new.text), str)
