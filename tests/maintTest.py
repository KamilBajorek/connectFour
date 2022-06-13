import unittest

from Exceptions import FullColumnException
from game import Game
from rules import RULES


class MainTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def testTwoMovesAtTheSameColumn(self):
        self.game.button_click(1)
        self.game.button_click(1)
        self.game.button_click(1)
        self.game.button_click(1)

        field1 = RULES.getFieldAt(self.game.ui.fields, 1, 6)
        field2 = RULES.getFieldAt(self.game.ui.fields, 1, 5)
        field3 = RULES.getFieldAt(self.game.ui.fields, 1, 4)
        field4 = RULES.getFieldAt(self.game.ui.fields, 1, 3)

        self.assertTrue(field1.isFilled and field1.player == 1)
        self.assertTrue(field2.isFilled and field2.player == 2)
        self.assertTrue(field3.isFilled and field3.player == 1)
        self.assertTrue(field4.isFilled and field4.player == 2)

    def testRaisingFullColumnExceptionWhenColumnIsFull(self):
        self.game.button_click(1)
        self.game.button_click(1)
        self.game.button_click(1)
        self.game.button_click(1)
        self.game.button_click(1)
        self.game.button_click(1)

        with self.assertRaises(FullColumnException):
            self.game.button_click(1)
