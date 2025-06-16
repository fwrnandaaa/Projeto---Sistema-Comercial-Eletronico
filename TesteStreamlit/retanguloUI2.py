from retangulo import Retangulo

class RetanguloUI2:
    def main():
        print("Cálculo com Retângulos")
        b = input("Informe a base: ")
        h = input("Informe a altura: ")
        r = Retangulo(float(b), float(h))
        print(r)
        print(f"Área = {r.calc_area()}")
        print(f"Diagonal = {r.calc_diagonal()}")