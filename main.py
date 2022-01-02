import tkinter
from tkinter import DISABLED
from tkinter.constants import NORMAL

import field as f
from player import PLAYER
from rules import RULES_VERTICAL, RULES_HORIZONTAL, RESULT

rulesVertical = RULES_VERTICAL()
rulesHorizontal = RULES_HORIZONTAL()

player1 = PLAYER("red", "Gracz1", 1)
player2 = PLAYER("yellow", "Gracz2", 2)

default_width = 100
buttons = []
fields = list()
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
        buttons[number - 1]["state"] = DISABLED

    result = check_result(number, max_unfilled)
    if result != RESULT.IN_PROGRESS:
        finish_game(result)
    change_active_player()


def finish_game(result):
    block_game()

    popup = tkinter.Toplevel()
    popup.geometry("250x150")
    game_over_label = tkinter.Label(popup, text="Koniec gry!")
    game_over_label.pack(fill='x', padx=50, pady=5)

    resultText = ""

    if result == RESULT.DRAW:
        resultText = "REMIS"
    else:
        resultText = "WYGRAŁ GRACZ " + str(result)

    result_label = tkinter.Label(popup, text=resultText)
    result_label.pack(fill='x', padx=50, pady=5)

    close_button = tkinter.Button(popup, text="Zamknij", command=popup.destroy)
    close_button.pack(padx=50, pady=5)


def block_game():
    for button in buttons:
        button["state"] = DISABLED


def check_result(column, row):
    vertical_result = rulesVertical.ktoWygral(fields, column, row)
    horizontal_result = rulesHorizontal.ktoWygral(fields, column, row)

    if vertical_result != RESULT.IN_PROGRESS:
        return vertical_result
    if horizontal_result != RESULT.IN_PROGRESS:
        return horizontal_result
    return RESULT.IN_PROGRESS


def change_active_player():
    global active_player

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
            field.fill(canvas, colour, active_player.id)


def reset_game():
    global active_player
    for field in fields:
        canvas.itemconfig(field.circle, fill="")
        field.isFilled = 0
        field.player = 0
    for button in buttons:
        button["state"] = NORMAL
    active_player = player1
    change_active_player_label()


tkinter.Canvas.create_circle = _create_circle

gameStatusText = tkinter.StringVar()


def change_active_player_label():
    gameStatusText.set(activePlayerText + active_player.name)


gameStatus = tkinter.Label(window, textvariable=gameStatusText)
gameStatus.place(x=20, y=20)

resetButton = tkinter.Button(window, text="Resetuj", command=reset_game)
resetButton.place(x=160, y=20)

gameStatusText.set(activePlayerText + active_player.name)

for i in range(0, 7):
    buttons.append(create_button(20 + (default_width * i), 60, "Kolumna " + str(i + 1), i + 1))

for i in range(0, 7):
    for j in range(0, 6):
        circle = canvas.create_circle(70 + (default_width * i), 160 + (default_width * j), 40)
        fields.append(f.FIELD(circle, i + 1, j + 1))

window.mainloop()
