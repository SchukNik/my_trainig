import math

class Figure():
    sides_count = 0

    def __init__(self, color, sides):
        self.__sides = sides
        self.__color = color
        self.filled = True

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        if r in range(255) and g in range(255) and b in range(255):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) == True:
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        for i in sides:
            if isinstance(i, int) and i > 0 and len(sides) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        perimetr = 0
        for j in self.__sides:
            perimetr += j
        return perimetr

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(sides, color)
        self.__sides = sides
        self.__radius = sides / (2 * math.pi)

    def get_square(self):
        return pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(sides, color)

    def get_square(self, a, b, c):
        p = (a + b + c)/2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            super().__init__(color, ([sides[0]] * self.sides_count))
        else:
            super().__init__(color, ([1] * self.sides_count))

    def set_sides(self, *new_sides):
        if len(new_sides) == 1 and isinstance(new_sides[0], int) and new_sides[0] > 0:
            super().set_sides(*([new_sides[0]] * self.sides_count))

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())