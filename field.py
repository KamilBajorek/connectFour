class FIELD:
    def __init__(self, _circle, _column, _row):
        self.circle = _circle
        self.column = _column
        self.row = _row
        self.isFilled = 0

    def fill(self, canvas, colour):
        if self.isFilled == 0:
            canvas.itemconfig(self.circle, fill=colour)
            self.isFilled = 1
