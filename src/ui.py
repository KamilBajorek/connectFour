import tkinter
from tkinter import DISABLED

from consts import Consts


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


tkinter.Canvas.create_circle = _create_circle


class UI:
    activePlayerText = "Tura "

    def __init__(self):
        self.fields = list()
        self.buttons = []
        self.window = self.init_window()
        self.canvas = self.init_canvas()

        self.gameStatusText = tkinter.StringVar()

        gameStatus = tkinter.Label(self.window, textvariable=self.gameStatusText)
        gameStatus.place(x=20, y=20)

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

    def block_buttons(self):
        """
        Iteruje po liśce przycisków, blokując (ustawiając state na disabled) wszystkie.
        :return:
        """
        for button in self.buttons:
            button["state"] = DISABLED

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
