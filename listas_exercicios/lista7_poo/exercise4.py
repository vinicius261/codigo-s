"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 5: Progamação Orientada a Objetos

Exercício 4

"""

from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def area_calc(self):
        pass

    @abstractmethod
    def perimeter_calc(self):
        pass


class Triangle(Polygon):
    def __init__(self, side_lenght) -> None:
        self.sides_lenght = side_lenght

    def area_calc(self):
        area = self.sides_lenght*(self.sides_lenght*(3**(1/2)/2))
        return area

    def perimeter_calc(self):
        perimeter = 3*self.sides_lenght
        return perimeter


class Square(Polygon):
    def __init__(self, side_lenght) -> None:
        self.sides_lenght = side_lenght

    def area_calc(self):
        area = self.sides_lenght**2
        return area

    def perimeter_calc(self):
        perimeter = 4*self.sides_lenght
        return perimeter


class Pentagon(Polygon):
    def __init__(self, side_lenght) -> None:
        self.sides_lenght = side_lenght

    def area_calc(self):
        area = 5*(self.sides_lenght*(self.sides_lenght*(3**(1/2)/2)))
        return area

    def perimeter_calc(self):
        perimeter = 5*self.sides_lenght
        return perimeter


triangulo = Triangle(5)

quadrado = Square(5)

pentagono = Pentagon(5)

print(triangulo.area_calc())
print(triangulo.perimeter_calc())

print(quadrado.area_calc())
print(quadrado.perimeter_calc())

print(pentagono.area_calc())
print(pentagono.perimeter_calc())
