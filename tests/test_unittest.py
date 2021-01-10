import unittest
from os import path

from src.utils.config import Configuration
# from src.utils.reader import ReaderLogFile


class TestConfigMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.configurator = Configuration("./src/config.ini")
        return super().setUp()

    def test_printAllGroupSettings(self):
        print(self.configurator.getSections())
        self.assertIs(type(self.configurator.getSections()), list)


# class TestReaderMethods(unittest.TestCase):
#     def setUp(self) -> None:
#         self.filePath = path.abspath("./data/9 January,Saturday.htm")
#         self.lastLine = 19
#         self.initLine = 17
#         return super().setUp()

#     def test_convertLogToJSON(self):
#         reader = ReaderLogFile(self.filePath)
#         jsonText = reader.getJson(reader.getLines())

#         self.assertIs(type(jsonText), str)
#         self.assertEqual(reader.lastLine, self.lastLine,
#                          "Numero final de linea incorrecto")
