class Chess:
    def __init__(self, color, place):
        self.color = color
        self.place = place

    def change_color(self):
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"

    def change_place(self, x, y):
        if 0 <= x <= 7 and 0 <= y <= 7:
            self.place = (x, y)
        else:
            print("Over board!")


chess = Chess("white", (1, 2))

chess.change_color()
print(chess.color)

chess.change_place(6, 2)
print(chess.place)

chess.change_place(8, 4)
