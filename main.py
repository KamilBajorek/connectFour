import tkinter
import field

default_width = 100
buttons = []
fields = []

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


def create_button(x, y, name):
    button = tkinter.Button(window, text=name)
    button.place(x=x, y=y, width=default_width)
    return button


window = tkinter.Tk()
window.title("Connect Four")
window.geometry("1080x720")
window.resizable(width=False, height=False)

canvas = tkinter.Canvas(window, width=1080, height=720)
canvas.grid()

tkinter.Canvas.create_circle = _create_circle

for i in range(0, 7):
    buttons.append(create_button(20 + (100 * i), 60, "Kolumna " + str(i + 1)))

for i in range(0, 7):
    for j in range(0, 7):
        circle = canvas.create_circle(70 + (100 * i), 160 + (100 * j), 40)
        fields.append(field.FIELD(circle, j, i))

window.mainloop()
