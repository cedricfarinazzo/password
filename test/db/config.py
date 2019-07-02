import os
import unittest
from password.db.config import *


class TestConfig(unittest.TestCase):

    def setUp(self):
        self.conf = Config()

    def test_init(self):
        self.assertIsNotNone(self.conf)
        self.assertEqual(len(self.conf), 0)

    def test_set(self):
        self.conf.clean()
        self.conf["path"] = "/test"
        with self.subTest():
            self.assertTrue("path" in self.conf)
            self.assertEqual(self.conf["path"], "/test")
            self.assertEqual(len(self.conf), 1)

    def test_del(self):
        self.conf.clean()
        self.conf["path"] = "/test"
        del self.conf["path"]
        with self.subTest():
            self.assertFalse("path" in self.conf)
            self.assertEqual(len(self.conf), 0)

    def test_save_load(self):
        self.conf.clean()
        path = "config.bin"
        self.conf["path"] = path
        self.conf["pass"] = "password"
        self.conf["user"] = "user"
        try:
            self.conf.save_config(path)
            conf2 = Config.load_config(path)
            self.assertIsNotNone(conf2)
            for k1, v1 in self.conf:
                with self.subTest(key=k1, value=v1):
                    self.assertTrue(k1 in conf2)
                    self.assertEqual(v1, conf2[k1])
        except Exception as e:
            raise e
        finally:
            os.remove(path)
