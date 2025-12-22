#композиция 

class WinDoor:
    def __init__(self, width, height):
        self.square = width * height

class Room:
    def __init__(self, width, length, height):
        self.__width = width
        self.__length = length
        self.__height = height
        self.__win_door = []
        self.__square = self.__calc_square()

    def __calc_square(self):
        return 2 * self.__height * (self.__width + self.__length)

    def get_square(self):
        return self.__square

    def add_win_door(self, width, height):
        self.__win_door.append(WinDoor(width, height))

    def effective_square(self):
        work_square = self.__square
        for wd in self.__win_door:
            work_square -= wd.square
        return work_square

room = Room(4, 5, 3)
print(room.get_square())          

room.add_win_door(2, 2)
room.add_win_door(2, 0.8)

print(room.effective_square())