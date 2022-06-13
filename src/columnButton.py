import tkinter
from tkinter import DISABLED, NORMAL

from consts import Consts


class ColumnButton:
    def __init__(self, x, y, name, column, window, game):
        self.button = tkinter.Button(window, text=name, command=lambda: self.button_click(column, game))
        self.button.place(x=x, y=y, width=Consts.default_width)

    def block(self):
        self.button["state"] = DISABLED

    def activate(self):
        self.button["state"] = NORMAL

    def button_click(self, number, game):
        game.on_button_click(number)
