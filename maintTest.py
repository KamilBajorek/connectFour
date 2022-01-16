import unittest

from Exceptions import FullColumnException
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

        field1 = RULES.getFieldAt(self.main.ui.fields, 1, 6)
        field2 = RULES.getFieldAt(self.main.ui.fields, 1, 5)
        field3 = RULES.getFieldAt(self.main.ui.fields, 1, 4)
        field4 = RULES.getFieldAt(self.main.ui.fields, 1, 3)

        self.assertTrue(field1.isFilled and field1.player == 1)
        self.assertTrue(field2.isFilled and field2.player == 2)
        self.assertTrue(field3.isFilled and field3.player == 1)
        self.assertTrue(field4.isFilled and field4.player == 2)

    def testRaisingFullColumnExceptionWhenColumnIsFull(self):
        self.main.button_click(1)
        self.main.button_click(1)
        self.main.button_click(1)
        self.main.button_click(1)
        self.main.button_click(1)
        self.main.button_click(1)

        with self.assertRaises(FullColumnException):
            self.main.button_click(1)
