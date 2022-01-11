import unittest
from main import Main
from rules import RULES


class MainTests(unittest.TestCase):
    def setUp(self):
        self.main = Main()

    def testTwoMovesAtTheSameColumn(self):
        self.main.add_coin_to_column(1, 0, "red")

        field1 = RULES.getFieldAt(self.main.ui.fields, 1, 6)

        self.assertTrue(field1.isFilled)
