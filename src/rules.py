from enum import Enum


class RULES:
    def ktoWygral(self, fields, clicked_column, clicked_row):
        raise NotImplementedError()

    def czyRemis(self, fields):
        """
        Określa wynik gry - czy wystąpił remis.
        Metoda powinna być wywoływana po sprawdzeniu wszystkich innych warunków końca gry.
        Sprawdza czy pozostały jeszcze jakieś nieuzupełnione pola.
        :param fields: Pola gry przekazane z UI
        :return: Zwraca false w przypadku gdy znajdzie jakiekolwiek nieuzupełnione pole,
         w przeciwnym wypadku zwraca true
        """
        for field in fields:
            if field.isFilled == 0:
                return False
        return True

    @staticmethod
    def getFieldAt(fields, column, row):
        """
        Służy do pobierania obiektu pola z listy pól
        :param fields: Pola gry przekazane z UI
        :param column: Kolumna pola
        :param row: wiersz pola
        :return: field - pole gry o podanych parametrach
        """
        for field in fields:
            if field.row == row and field.column == column:
                return field


class RULES_VERTICAL(RULES):
    def ktoWygral(self, fields, clicked_column, clicked_row):
        """
        Sprawdza czy któryś z graczy wygrał układając pionowo cztery monety.
        Sprawdza wszystkie kombinacje pionowo ułożonych monet.
        Jeśli żaden z graczy nie wygrał, sprawdzane jest czy nie nastąpił remis.
        W przypadku braku zwycięstwa lub remisu, zwracana jest informacja o tym, że gra jest w trakcie.
        :param fields: Lista pól przekazanych z UI
        :param clicked_column: Kolumna sprawdzenego pola
        :param clicked_row: Wiersz sprawdzanego pola
        :return: Zwraca enum RESULT z wynikiem
        """
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
        """
        Sprawdza czy któryś z graczy wygrał układając poziomo cztery monety.
        Sprawdza wszystkie kombinacje poziomo ułożonych monet.
        Jeśli żaden z graczy nie wygrał, sprawdzane jest czy nie nastąpił remis.
        W przypadku braku zwycięstwa lub remisu, zwracana jest informacja o tym, że gra jest w trakcie.
        :param fields: Lista pól przekazanych z UI
        :param clicked_column: Kolumna sprawdzenego pola
        :param clicked_row: Wiersz sprawdzanego pola
        :return: Zwraca enum RESULT z wynikiem
        """
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
        """
        Sprawdza czy któryś z graczy wygrał układając cztery monety na ukos.
        Sprawdza wszystkie kombinacje ukośnie ułożonych monet.
        Jeśli żaden z graczy nie wygrał, sprawdzane jest czy nie nastąpił remis.
        W przypadku braku zwycięstwa lub remisu, zwracana jest informacja o tym, że gra jest w trakcie.
        :param fields: Lista pól przekazanych z UI
        :param clicked_column: Kolumna sprawdzenego pola
        :param clicked_row: Wiersz sprawdzanego pola
        :return: Zwraca enum RESULT z wynikiem
        """
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
        """
        Sprawdza pola od lewej do prawej na ukos, w poszukiwaniu 4 monet tego samego gracza.
        :param fields: Lista pól przekazanych z UI
        :param column_from: kolumna pola, od którego jest sprawdzane
        :param row_from: wiersz pola, od którego jest sprawdzane
        :return: Zwraca gracza, którego pola na ukos zostały znalezione lub None
        """
        field1 = self.getFieldAt(fields, column_from, row_from)
        field2 = self.getFieldAt(fields, column_from + 1, row_from + 1)
        field3 = self.getFieldAt(fields, column_from + 2, row_from + 2)
        field4 = self.getFieldAt(fields, column_from + 3, row_from + 3)
        if field1.isFilled == 1 and field1.player == field2.player and field2.player == field3.player and field3.player == field4.player:
            return field1.player
        return None

    def sprawdzOdPrawejDoLewej(self, fields, column_from, row_from):
        """
        Sprawdza pola od prawej do lewej na ukos, w poszukiwaniu 4 monet tego samego gracza.
        :param fields: Lista pól przekazanych z UI
        :param column_from: kolumna pola, od którego jest sprawdzane
        :param row_from: wiersz pola, od którego jest sprawdzane
        :return: Zwraca gracza, którego pola na ukos zostały znalezione lub None
        """
        field1 = self.getFieldAt(fields, column_from, row_from)
        field2 = self.getFieldAt(fields, column_from - 1, row_from + 1)
        field3 = self.getFieldAt(fields, column_from - 2, row_from + 2)
        field4 = self.getFieldAt(fields, column_from - 3, row_from + 3)
        if field1.isFilled == 1 and field1.player == field2.player and field2.player == field3.player and field3.player == field4.player:
            return field1.player
        return None

    def sprawdz_odleglosc(self, column_from, row_from, column_to, row_to):
        """
        Sprawdza odleglosc pomiędzy polami
        :param column_from: Kolumna pola od
        :param row_from: Wiersz pola od
        :param column_to: Kolumna pola do
        :param row_to: Wiersz pola do
        :return: Zwraca odległość między polami
        """
        cols = abs(column_from - column_to)
        rows = abs(row_from - row_to)
        if cols == rows:
            return cols

    def czy_prawidlowy_punkt(self, col, row):
        """
        Sprawdza czy punkt o podanych koordynatach istnieje na planszy.
        :param col: Kolumna sprawdzanego pola
        :param row: Wiersz sprawdzanego pola
        :return: Zwraca True/False w zależności od tego czy takie pole istnieje czy nie
        """
        return col in range(1, self.max_column + 1) and row in range(1, self.max_row + 1)


class RESULT(Enum):
    """
    Opisuje wynik gry

    0 - w trakcie

    1/2 - zwycięski gracz

    3 - remis
    """
    IN_PROGRESS = 0,
    PLAYER1 = 1,
    PLAYER2 = 2,
    DRAW = 3
