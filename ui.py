import tkinter
from tkinter import DISABLED


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
        self.gameStatusText.set(self.activePlayerText + gracz)

    def init_window(self):
        window = tkinter.Tk()
        window.title("Connect Four")
        window.geometry("1080x720")
        window.resizable(width=False, height=False)

        return window

    def init_canvas(self):
        canvas = tkinter.Canvas(self.window, width=1080, height=720)
        canvas.grid()

        return canvas

    def block_buttons(self):
        for button in self.buttons:
            button["state"] = DISABLED

    def finish_game_popup(self, text):
        popup = tkinter.Toplevel()
        popup.geometry("250x150")
        game_over_label = tkinter.Label(popup, text="Koniec gry!")
        game_over_label.pack(fill='x', padx=50, pady=5)

        result_label = tkinter.Label(popup, text=text)
        result_label.pack(fill='x', padx=50, pady=5)

        close_button = tkinter.Button(popup, text="Zamknij", command=popup.destroy)
        close_button.pack(padx=50, pady=5)
