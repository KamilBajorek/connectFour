import tkinter

import field as f
from columnButton import ColumnButton
from consts import Consts


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


tkinter.Canvas.create_circle = _create_circle


class UI:
    activePlayerText = "Tura "

    def __init__(self, game):
        self.fields = list()
        self.buttons = []
        self.window = self.init_window()
        self.canvas = self.init_canvas()

        self.gameStatusText = tkinter.StringVar()

        gameStatus = tkinter.Label(self.window, textvariable=self.gameStatusText)
        gameStatus.place(x=20, y=20)

        self.create_buttons(game)
        self.create_fields()

    def change_active_player_label(self, gracz):
        """
        Zmienia tekst wyświetlany na ekranie o aktywnym graczu.
        :param gracz: nazwa gracza i jego numer
        """
        self.gameStatusText.set(self.activePlayerText + gracz)

    def init_window(self):
        """
        Tworzy główne okno gry.
        :returns: zwracca utworzone okno gry
        """
        window = tkinter.Tk()
        window.title("Connect Four")
        window.geometry(f"{Consts.window_width}x{Consts.window_height}")
        window.resizable(width=False, height=False)

        return window

    def init_canvas(self):
        """
        Tworzy canvas, dodawany do głównego okna.
        :return: canvas
        """
        canvas = tkinter.Canvas(self.window, width=Consts.window_width, height=Consts.window_height)
        canvas.grid()

        return canvas

    def block_button(self, column):
        """
        Blokuje przycisk.
        :return:
        """
        self.buttons[column].block()

    def block_buttons(self):
        """
        Iteruje po liśce przycisków, blokując (ustawiając state na disabled) wszystkie.
        :return:
        """
        for button in self.buttons:
            button.block()

    def activate_buttons(self):
        """
        Iteruje po liśce przycisków, aktywując (ustawiając state na normal) wszystkie.
        :return:
        """
        for button in self.buttons:
            button.activate()

    def clear_fields(self):
        for field in self.fields:
            self.canvas.itemconfig(field.circle, fill="")
            field.isFilled = 0
            field.player = 0

    def create_buttons(self, game):
        for i in range(0, 7):
            self.buttons.append(
                ColumnButton(20 + (Consts.default_width * i), 60, "Kolumna " + str(i + 1), i + 1, self.window, game))

    def create_fields(self):
        for i in range(0, 7):
            for j in range(0, 6):
                circle = self.canvas.create_circle(70 + (Consts.default_width * i), 160 + (Consts.default_width * j),
                                                   40)
                self.fields.append(f.FIELD(circle, i + 1, j + 1))

    def finish_game_popup(self, text):
        """
        Wyświetla okno z informacją o zakończeniu rozgrywki
        :param text: Tekst z wynikiem gry
        :return:
        """
        popup = tkinter.Toplevel()
        popup.geometry("250x150")
        game_over_label = tkinter.Label(popup, text="Koniec gry!")
        game_over_label.pack(fill='x', padx=50, pady=5)

        result_label = tkinter.Label(popup, text=text)
        result_label.pack(fill='x', padx=50, pady=5)

        close_button = tkinter.Button(popup, text="Zamknij", command=popup.destroy)
        close_button.pack(padx=50, pady=5)
