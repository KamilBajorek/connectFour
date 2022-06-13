class FIELD:
    def __init__(self, _circle, _column, _row):
        self.circle = _circle
        self.column = _column
        self.row = _row
        self.isFilled = 0
        self.player = 0

    def fill(self, canvas, colour, _id):
        """ Metoda uzupełnia pole, nadając mu kolor oraz przypisując numer gracza.
                Args:
                      canvas: obiekt przekazywany z UI, pozwala na skonfigurowanie koloru obiektu
                      colour: kolor pola
                      _id: id gracza
        """
        if self.isFilled == 0:
            canvas.itemconfig(self.circle, fill=colour)
            self.isFilled = 1
            self.player = _id
