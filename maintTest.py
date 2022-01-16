import unittest
from main import Main
from rules import RULES


class MainTest(unittest.TestCase):
    def setUp(self):
        self.main = Main()

    def testTwoMovesAtTheSameColumn(self):
        self.main.button_click(1)
        self.main.button_click(1)
        self.main.button_click(1)
        self.main.button_click(1)
        self.main.button_click(1)
        self.main.button_click(1)

        field1 = RULES.getFieldAt(self.main.ui.fields, 1, 6)

        self.assertTrue(field1.isFilled)
