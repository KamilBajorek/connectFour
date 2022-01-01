import tkinter
from tkinter import DISABLED

import field as f
from player import PLAYER

player1 = PLAYER("red", "Gracz1")
player2 = PLAYER("yellow", "Gracz2")

default_width = 100
buttons = []
fields = []
activePlayerText = "Aktywny gracz: "
active_player = player1

window = tkinter.Tk()
window.title("Connect Four")
window.geometry("1080x720")
window.resizable(width=False, height=False)

canvas = tkinter.Canvas(window, width=1080, height=720)
canvas.grid()


def get_max_unfilled_in_column(column):
    max_unfilled = 0
    for field in fields:
        if field.column == column and field.isFilled == 0:
            if field.row >= max_unfilled:
                max_unfilled = field.row
    return max_unfilled


def button_click(number):
    global active_player

    max_unfilled = get_max_unfilled_in_column(number)
    add_coin_to_column(number, max_unfilled, active_player.colour)

    if max_unfilled == 1:
        buttons[number-1]["state"] = DISABLED

    if active_player == player1:
        active_player = player2
    else:
        active_player = player1
    change_active_player_label()


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


def create_button(x, y, name, column):
    button = tkinter.Button(window, text=name, command=lambda: button_click(column))
    button.place(x=x, y=y, width=default_width)
    return button


def add_coin_to_column(column, max_unfilled, colour):
    if max_unfilled == 0:
        return
    for field in fields:
        if field.row == max_unfilled and field.column == column:
            field.fill(canvas, colour)


tkinter.Canvas.create_circle = _create_circle

gameStatusText = tkinter.StringVar()


def change_active_player_label():
    gameStatusText.set(activePlayerText + active_player.name)


gameStatus = tkinter.Label(window, textvariable=gameStatusText)
gameStatus.place(x=20, y=20)

gameStatusText.set(activePlayerText + active_player.name)

for i in range(0, 7):
    buttons.append(create_button(20 + (default_width * i), 60, "Kolumna " + str(i + 1), i + 1))

for i in range(0, 7):
    for j in range(0, 6):
        circle = canvas.create_circle(70 + (default_width * i), 160 + (default_width * j), 40)
        fields.append(f.FIELD(circle, i + 1, j + 1))

window.mainloop()
