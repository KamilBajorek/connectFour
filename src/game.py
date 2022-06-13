import tkinter
from tkinter import DISABLED
from tkinter.constants import NORMAL

import field as f
from Exceptions import FullColumnException
from player import PLAYER
from rules import RULES_VERTICAL, RULES_HORIZONTAL, RESULT, RULES_DIAGONALLY

import ui


class Game:
    def get_max_unfilled_in_column(self, column):
        """ Pobranie najniższego numeru wiersza dla danej kolumny, który nie jest uzupełniony.
             Args:
                 column: Numer kolumny
             Returns:
                Maksymalny (czyli najwyższy) wiersz, który nie został uzupełniony dla tej kolumny
             """
        max_unfilled = 0
        for field in self.ui.fields:
            if field.column == column and field.isFilled == 0:
                if field.row >= max_unfilled:
                    max_unfilled = field.row
        return max_unfilled

    def button_click(self, number):
        """ Obsługuje pojedyncze kliknięcie przycisku nad kolumną.
            Sprawdza najwyższy wolny wiersz do którego można dorzucić monetę dla tej kolumny.
            Dodaje monetę do kolumny.
            Blokuje przycisk jeśli zapełniono wszystkie kolumny.
            Sprawdza wynik gry i kończy ją w przypadku zwycięstwa/remisu.
            W przeciwnym wypadku zmienia aktywnego gracza.
            Args:
                number: Numer klikniętej kolumny
        """
        max_unfilled = self.get_max_unfilled_in_column(number)
        self.add_coin_to_column(number, max_unfilled, self.active_player.colour)

        if max_unfilled == 1:
            self.ui.buttons[number - 1]["state"] = DISABLED

        result = self.check_result(number, max_unfilled)
        if result != RESULT.IN_PROGRESS:
            self.finish_game(result)
        self.change_active_player()

    def finish_game(self, result):
        """ Metoda kończenia gry - blokuje przyciski do wrzucania monet.
            W zależności od wyniku ustawia zmienną result_text i przekazuje ją do wyskakującego
            okienka z wynikiem gry.
            Args:
                result: Obiekt klasy RESULT
        """
        self.ui.block_buttons()

        result_text = ""
        if result == RESULT.DRAW:
            result_text = "REMIS"
        else:
            result_text = "WYGRAŁ GRACZ " + str(result)

        self.ui.finish_game_popup(result_text)

    def check_result(self, column, row):
        """ Metoda sprawdzania wyniku dla klikniętej kolumny i wiersza.
            Sprawdza wszystkie kombinacje dla których możliwe jest określenie wyniku.
            Args:
                column: numer kolumny
                row: numer wiersza
            Returns:
                 Wynik gry - obiekt RESULT
        """
        vertical_result = self.rulesVertical.ktoWygral(self.ui.fields, column, row)
        horizontal_result = self.rulesHorizontal.ktoWygral(self.ui.fields, column, row)
        diagonally_result = self.rulesDiagonally.ktoWygral(self.ui.fields, column, row)

        if vertical_result != RESULT.IN_PROGRESS:
            return vertical_result
        if horizontal_result != RESULT.IN_PROGRESS:
            return horizontal_result
        if diagonally_result != RESULT.IN_PROGRESS:
            return diagonally_result
        return RESULT.IN_PROGRESS

    def change_active_player(self):
        """ Metoda zmienia aktywnego gracza. Ustawia pole active_player oraz przekazuje zmianę do UI.
        """
        if self.active_player == self.player1:
            self.active_player = self.player2
        else:
            self.active_player = self.player1
        self.ui.change_active_player_label(self.active_player.name)

    def _create_circle(self, x, y, r, **kwargs):
        """ Metoda do tworzenia kół, reprezentujących pola, do wrzucania monet
        """
        return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)

    def create_button(self, x, y, name, column):
        """ Metoda do tworzenia przycisków
            Args:
                x: Położenie x przycisku
                y: Położenie y przycisku
                name: Nazwa przycisku (np. Kolumna 1)
                column: Numer kolumny przycisku
            Returns:
                Zwraca ID przycisku
        """
        button = tkinter.Button(self.ui.window, text=name, command=lambda: self.button_click(column))
        button.place(x=x, y=y, width=self.default_width)
        return button

    def add_coin_to_column(self, column, max_unfilled, colour):
        """ Metoda dodawania monety do kolumny.
            Jeśli następuje próba wrzucenia monety do kolumny 0 - podnoszony jest wyjątek FullColumnException
            W przeciwnym wypadku znajdywany jest odpowiedni obiekt klasy Field i pole jest uzupełnianie.
            Args:
                column: numer kolumny
                max_unfilled: numer wiersza do wrzucenia monety
                colour: kolor gracza
        """
        if max_unfilled == 0:
            raise FullColumnException()
        for field in self.ui.fields:
            if field.row == max_unfilled and field.column == column:
                field.fill(self.ui.canvas, colour, self.active_player.id)

    def reset_game(self):
        """ Metoda służąca do resetowania gry. Ustawia pola na nieuzupełnione isFilled oraz ustawia gracza na 0.
            Odblokowuje przyciski do wrzucania monet oraz zmienia aktywnego gracza.
        """
        for field in self.ui.fields:
            self.ui.canvas.itemconfig(field.circle, fill="")
            field.isFilled = 0
            field.player = 0
        for button in self.ui.buttons:
            button["state"] = NORMAL
        self.active_player = self.player1
        self.ui.change_active_player_label(self.active_player.name)

    def __init__(self):

        self.rulesVertical = RULES_VERTICAL()
        self.rulesHorizontal = RULES_HORIZONTAL()
        self.rulesDiagonally = RULES_DIAGONALLY()

        self.player1 = PLAYER("red", "gracza 1", 1)
        self.player2 = PLAYER("yellow", "gracza 2", 2)

        self.active_player = self.player1

        self.ui = ui.UI()

        self.default_width = 100

        self.resetButton = tkinter.Button(self.ui.window, text="Resetuj", command=self.reset_game)
        self.resetButton.place(x=160, y=20)

        self.ui.change_active_player_label(self.active_player.name)

        for i in range(0, 7):
            self.ui.buttons.append(
                self.create_button(20 + (self.default_width * i), 60, "Kolumna " + str(i + 1), i + 1))

        for i in range(0, 7):
            for j in range(0, 6):
                circle = self.ui.canvas.create_circle(70 + (self.default_width * i), 160 + (self.default_width * j), 40)
                self.ui.fields.append(f.FIELD(circle, i + 1, j + 1))
