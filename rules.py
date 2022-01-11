from enum import Enum


class RULES:
    def ktoWygral(self, fields, clicked_column, clicked_row):
        raise NotImplementedError()

    def czyRemis(self, fields):
        for field in fields:
            if field.isFilled == 0:
                return False
        return True

    @staticmethod
    def getFieldAt(fields, column, row):
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
    max_row = 6
    max_column = 7
    connect_size = 4

    def ktoWygral(self, fields, clicked_column, clicked_row):
        for i in range(0, 4):
            col_min = clicked_column - i
            row_min = clicked_row - i
            if self.czy_prawidlowy_punkt(col_min, row_min) and self.czy_prawidlowy_punkt(col_min + 3, row_min + 3):
                res = self.sprawdzOdLewejDoPrawej(fields, col_min, row_min)
                if res is not None:
                    return res

            col_plus = clicked_column + i
            if self.czy_prawidlowy_punkt(col_plus, row_min) and self.czy_prawidlowy_punkt(col_plus - 3, row_min + 3):
                res = self.sprawdzOdPrawejDoLewej(fields, col_plus, row_min)
                if res is not None:
                    return res

        if self.czyRemis(fields):
            return RESULT.DRAW
        else:
            return RESULT.IN_PROGRESS

    def sprawdzOdLewejDoPrawej(self, fields, column_from, row_from):
        field1 = self.getFieldAt(fields, column_from, row_from)
        field2 = self.getFieldAt(fields, column_from + 1, row_from + 1)
        field3 = self.getFieldAt(fields, column_from + 2, row_from + 2)
        field4 = self.getFieldAt(fields, column_from + 3, row_from + 3)
        if field1.isFilled == 1 and field1.player == field2.player and field2.player == field3.player and field3.player == field4.player:
            return field1.player
        return None

    def sprawdzOdPrawejDoLewej(self, fields, column_from, row_from):
        field1 = self.getFieldAt(fields, column_from, row_from)
        field2 = self.getFieldAt(fields, column_from - 1, row_from + 1)
        field3 = self.getFieldAt(fields, column_from - 2, row_from + 2)
        field4 = self.getFieldAt(fields, column_from - 3, row_from + 3)
        if field1.isFilled == 1 and field1.player == field2.player and field2.player == field3.player and field3.player == field4.player:
            return field1.player
        return None

    def sprawdz_odleglosc(self, column_from, row_from, column_to, row_to):
        cols = abs(column_from - column_to)
        rows = abs(row_from - row_to)
        if cols == rows:
            return cols

    def czy_prawidlowy_punkt(self, col, row):
        return col in range(1, self.max_column+1) and row in range(1, self.max_row+1)


class RESULT(Enum):
    IN_PROGRESS = 0,
    PLAYER1 = 1,
    PLAYER2 = 2,
    DRAW = 3
