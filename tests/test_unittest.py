import unittest

from src.utils.config import Configuration


class TestConfigMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.configurator = Configuration("./src/config.ini")
        return super().setUp()

    def test_printAllGroupSettings(self):
        print(self.configurator.getSections())
        self.assertIs(type(self.configurator.getSections()), list)
