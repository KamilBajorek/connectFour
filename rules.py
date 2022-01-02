from enum import Enum


class RULES:
    def ktoWygral(self, fields, clicked_column, clicked_row):
        raise NotImplementedError()

    def czyRemis(self, fields):
        for field in fields:
            if field.isFilled == 0:
                return False
        return True

    def getFieldAt(self, fields, column, row):
        for field in fields:
            if field.row == row and field.column == column:
                return field


class RULES_VERTICAL(RULES):
    def ktoWygral(self, fields, clicked_column, clicked_row):
        for i in range(1, 4):
            field1 = self.getFieldAt(fields, clicked_column, i)
            field2 = self.getFieldAt(fields, clicked_column, i + 1)
            field3 = self.getFieldAt(fields, clicked_column, i + 2)
            field4 = self.getFieldAt(fields, clicked_column, i + 3)
            if field1.isFilled == 1 and field1.player == field2.player and field2.player == field3.player and field3.player == field4.player:
                return field1.player
        if self.czyRemis(fields):
            return RESULT.DRAW
        else:
            return RESULT.IN_PROGRESS


class RULES_HORIZONTAL(RULES):
    def ktoWygral(self, fields, clicked_column, clicked_row):
        for i in range(1, 5):
            field1 = self.getFieldAt(fields, i, clicked_row)
            field2 = self.getFieldAt(fields, i + 1, clicked_row)
            field3 = self.getFieldAt(fields, i + 2, clicked_row)
            field4 = self.getFieldAt(fields, i + 3, clicked_row)
            if field1.isFilled == 1 and field1.player == field2.player and field2.player == field3.player and field3.player == field4.player:
                return field1.player
        if self.czyRemis(fields):
            return RESULT.DRAW
        else:
            return RESULT.IN_PROGRESS


class RULES_DIAGONALLY(RULES):
    def ktoWygral(self, fields, clicked_column, clicked_row):
        pass


class RESULT(Enum):
    IN_PROGRESS = 0,
    PLAYER1 = 1,
    PLAYER2 = 2,
    DRAW = 3
