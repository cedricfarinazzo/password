import unittest
from password.db.security import *


class TestHash(unittest.TestCase):

    def test_hash(self):
        text = "password"
        self.assertNotEqual(Hash.hash(text), text)

    def test_verify(self):
        text = "password"
        hash = Hash.hash(text)
        self.assertTrue(Hash.verify_hash(text, hash))
