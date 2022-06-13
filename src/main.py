from game import Game


class Main:
    def __init__(self):
        self.game = Game()
        if __name__ == '__main__':
            self.game.ui.window.mainloop()


main = Main()
