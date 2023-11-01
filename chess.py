class Chess:
    def __init__(self, color, place):
        self.color = color
        self.place = place

    def change_color(self):
        if self.color == "Білий":
            self.color = "Чорний"
        else:
            self.color = "Білий"

    def change_place(self, x, y):
        if 0 <= x <= 7 and 0 <= y <= 7:
            self.place = (x, y)
        else:
            print("За межами поля!")


class Pawn(Chess):

    def check_move(self, new_place):
        if isinstance(new_place, tuple):
            x, y = new_place
        elif isinstance(new_place, int):
            x = new_place // 10
            y = new_place % 10
        else:
            return "Невірний формат позиції"

        if x < 1 or x > 8 or y < 1 or y > 8:
            return "Позиція виходить за межі дошки"

        if x == self.place[0] + 1 and y == self.place[1]:
            return "Можливо зробити хід"
        else:
            return "Недопустимий хід для пішака"


print('-- Реалізація класу для фігури - Пішак --')
pawn = Pawn('white', (2, 2))
print(pawn.check_move((3, 2)))
print(pawn.check_move((4, 2)))

pawn.change_color()
print(pawn.color)

pawn.change_place(6, 2)
print(pawn.place)

pawn.change_place(8, 4)


class Knight(Chess):

    def check_move(self, new_place):
        if isinstance(new_place, tuple):
            x, y = new_place
        elif isinstance(new_place, int):
            x = new_place // 10
            y = new_place % 10
        else:
            return "Невірний формат позиції"

        if x < 1 or x > 8 or y < 1 or y > 8:
            return "Позиція виходить за межі дошки"

        dx = abs(x - self.place[0])
        dy = abs(y - self.place[1])

        if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
            return "Можливо зробити хід"
        else:
            return "Недопустимий хід для коня"


print('-- Реалізація класу для фігури - Кінь --')
knight = Knight('black', (2, 2))
print(knight.check_move((4, 3)))
print(knight.check_move((5, 4)))
knight.change_color()
print(knight.color)

knight.change_place(6, 2)
print(knight.place)

knight.change_place(8, 4)


class Bishop(Chess):

    def check_move(self, new_place):
        if isinstance(new_place, tuple):
            x, y = new_place
        elif isinstance(new_place, int):
            x = new_place // 10
            y = new_place % 10
        else:
            return "Невірний формат позиції"

        if x < 1 or x > 8 or y < 1 or y > 8:
            return "Позиція виходить за межі дошки"

        if abs(x - self.place[0]) == abs(y - self.place[1]):
            return "Можливо зробити хід"
        else:
            return "Недопустимий хід для офіцера"


print('-- Реалізація класу для фігури - Офіцер --')
bishop = Bishop('white', (3, 3))
print(bishop.check_move((6, 6)))
print(bishop.check_move((5, 4)))

bishop.change_color()
print(bishop.color)

bishop.change_place(6, 2)
print(bishop.place)

bishop.change_place(8, 4)


class Rook(Chess):
    def check_move(self, new_place):
        if isinstance(new_place, tuple):
            x, y = new_place
        elif isinstance(new_place, int):
            x = new_place // 10
            y = new_place % 10
        else:
            return "Невірний формат позиції"

        if x < 1 or x > 8 or y < 1 or y > 8:
            return "Позиція виходить за межі дошки"

        if x == self.place[0] or y == self.place[1]:
            return "Можливо зробити хід"
        else:
            return "Недопустимий хід для тури"


print('-- Реалізація класу для фігури - Тур --')
rook = Rook('black', (1, 1))
print(rook.check_move((4, 1)))
print(rook.check_move((3, 4)))

rook.change_color()
print(rook.color)

rook.change_place(6, 2)
print(rook.place)

rook.change_place(8, 4)


class Queen(Chess):

    def check_move(self, new_place):
        if isinstance(new_place, tuple):
            x, y = new_place
        elif isinstance(new_place, int):
            x = new_place // 10
            y = new_place % 10
        else:
            return "Невірний формат позиції"

        if x < 1 or x > 8 or y < 1 or y > 8:
            return "Позиція виходить за межі дошки"

        if x == self.place[0] or y == self.place[1] or abs(x - self.place[0]) == abs(y - self.place[1]):
            return "Можливо зробити хід"
        else:
            return "Недопустимий хід для королеви"


print('-- Реалізація класу для фігури - Королева --')
queen = Queen('black',(1, 1))
print(queen.check_move((4, 1)))
print(queen.check_move((2, 6)))

queen.change_color()
print(queen.color)

queen.change_place(6, 2)
print(queen.place)

queen.change_place(8, 4)


class King(Chess):
    def check_move(self, new_place):
        if isinstance(new_place, tuple):
            x, y = new_place
        elif isinstance(new_place, int):
            x = new_place // 10
            y = new_place % 10
        else:
            return "Невірний формат позиції"

        if x < 1 or x > 8 or y < 1 or y > 8:
            return "Позиція виходить за межі дошки"

        if abs(x - self.place[0]) <= 1 and abs(y - self.place[1]) <= 1:
            return "Можливо зробити хід"
        else:
            return "Недопустимий хід для короля"


print('-- Реалізація класу для фігури - Король --')
king = King('white', (1, 1))
print(king.check_move((2, 1)))
print(king.check_move((3, 3)))

king.change_color()
print(king.color)

king.change_place(6, 2)
print(king.place)

king.change_place(8, 4)
