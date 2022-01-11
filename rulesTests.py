import unittest
import random

import player
from rules import RULES, RESULT
from rules import RULES_VERTICAL
from rules import RULES_HORIZONTAL
from rules import RULES_DIAGONALLY

import field as f


class RulesTests(unittest.TestCase):
    def setUp(self):
        self.player1 = player.PLAYER("red", "gracza 1", 1)
        self.player2 = player.PLAYER("yellow", "gracza 2", 2)
        self.fields = list()

    def testReturnFirstPlayerAsWinnerIfFourConnectedVerticallyByFirstPlayer(self):
        for i in range(0, 7):
            for j in range(0, 6):
                self.fields.append(f.FIELD(None, i + 1, j + 1))

        field1 = RULES.getFieldAt(self.fields, 1, 1)
        field2 = RULES.getFieldAt(self.fields, 1, 2)
        field3 = RULES.getFieldAt(self.fields, 1, 3)
        field4 = RULES.getFieldAt(self.fields, 1, 4)

        vertical_fields = (field1, field2, field3, field4)
        self.setFieldsToPlayer(vertical_fields, self.player1.id)

        rules = RULES_VERTICAL()
        result = rules.ktoWygral(self.fields, 1, 1)

        self.assertEqual(self.player1.id, result)

    def testReturnSecondPlayerAsWinnerIfFourConnectedHorizontallyBySecondPlayer(self):
        for i in range(0, 7):
            for j in range(0, 6):
                self.fields.append(f.FIELD(None, i + 1, j + 1))

        field1 = RULES.getFieldAt(self.fields, 1, 2)
        field2 = RULES.getFieldAt(self.fields, 2, 2)
        field3 = RULES.getFieldAt(self.fields, 3, 2)
        field4 = RULES.getFieldAt(self.fields, 4, 2)

        horizontal_fields = (field1, field2, field3, field4)
        self.setFieldsToPlayer(horizontal_fields, self.player2.id)

        rules = RULES_HORIZONTAL()
        result = rules.ktoWygral(self.fields, 2, 2)

        self.assertEqual(self.player2.id, result)

    def testReturnAnyPlayerAsWinnerIfFourConnectedHorizontallyByAnyPlayer(self):
        for i in range(0, 7):
            for j in range(0, 6):
                self.fields.append(f.FIELD(None, i + 1, j + 1))

        field1 = RULES.getFieldAt(self.fields, 1, 2)
        field2 = RULES.getFieldAt(self.fields, 2, 3)
        field3 = RULES.getFieldAt(self.fields, 3, 4)
        field4 = RULES.getFieldAt(self.fields, 4, 5)

        diagonal_fields = (field1, field2, field3, field4)
        any_player = random.randrange(self.player1.id, self.player2.id, 1)
        self.setFieldsToPlayer(diagonal_fields, any_player)

        rules = RULES_DIAGONALLY()
        result = rules.ktoWygral(self.fields, 2, 3)

        self.assertEqual(any_player, result)

    def testReturnDrawAsIfThereAreNoConnectedFour(self):
        for i in range(0, 7):
            for j in range(0, 6):
                self.fields.append(f.FIELD(None, i + 1, j + 1))

        for i in range(1, 8):
            for j in range(1, 7):
                field = RULES.getFieldAt(self.fields, i, j)
                field_list = list()
                field_list.append(field)
                p = 1
                if j in (0, 1, 3, 4):
                    if i % 2 == 0:
                        p = 2
                else:
                    if i % 2 != 0:
                        p = 2
                self.setFieldsToPlayer(field_list, p)

        rules_d = RULES_DIAGONALLY()
        rules_h = RULES_HORIZONTAL()
        rules_v = RULES_VERTICAL()
        result = None
        for i in range(1, 8):
            for j in range(1, 7):
                result_d = rules_d.ktoWygral(self.fields, i, j)
                result_h = rules_h.ktoWygral(self.fields, i, j)
                result_v = rules_v.ktoWygral(self.fields, i, j)
                if result_v != RESULT.IN_PROGRESS:
                    result = result_v
                if result_h != RESULT.IN_PROGRESS:
                    result = result_h
                if result_d != RESULT.IN_PROGRESS:
                    result = result_d

        self.assertEqual(RESULT.DRAW, result)

    def testReturnFirstPlayerAsWinnerIfFiveConnectedHorizontallyBySecondPlayer(self):
        for i in range(0, 7):
            for j in range(0, 6):
                self.fields.append(f.FIELD(None, i + 1, j + 1))

        p1_field1 = RULES.getFieldAt(self.fields, 1, 2)
        p1_field2 = RULES.getFieldAt(self.fields, 2, 2)
        p1_field3 = RULES.getFieldAt(self.fields, 3, 2)
        p1_field4 = RULES.getFieldAt(self.fields, 5, 2)
        p1_field5 = RULES.getFieldAt(self.fields, 6, 2)
        p1_field6 = RULES.getFieldAt(self.fields, 7, 2)

        p2_field1 = RULES.getFieldAt(self.fields, 1, 1)
        p2_field2 = RULES.getFieldAt(self.fields, 2, 1)
        p2_field3 = RULES.getFieldAt(self.fields, 3, 1)
        p2_field4 = RULES.getFieldAt(self.fields, 4, 1)
        p2_field5 = RULES.getFieldAt(self.fields, 5, 1)
        p2_field6 = RULES.getFieldAt(self.fields, 6, 1)
        p2_field7 = RULES.getFieldAt(self.fields, 7, 1)

        p1_fields = (p1_field1, p1_field2, p1_field3, p1_field4, p1_field5, p1_field6)
        p2_fields = (p2_field1, p2_field2, p2_field3, p2_field4, p2_field5, p2_field6, p2_field7)
        self.setFieldsToPlayer(p1_fields, self.player1.id)
        self.setFieldsToPlayer(p2_fields, self.player2.id)

        rules = RULES_HORIZONTAL()
        result = rules.ktoWygral(self.fields, 4, 1)

        self.assertEqual(self.player2.id, result)

    def setFieldsToPlayer(self, fields, playerId):
        for field in fields:
            field.isFilled = 1
            field.player = playerId
