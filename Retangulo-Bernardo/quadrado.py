import math

class Quadrado:
    def __init__(self, a):
        self.__a = a

    def __str__(self):
        return f"Base/Altura = {self.__a}"
    
    def calc_area(self):
        return math.pow(self.__a, 2)