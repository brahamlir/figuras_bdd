import math as m


class Figuras:

    def cuadrado(self, lado):
        try:
            lado = float(lado)
            return lado * lado
        except Exception:
            return 'dato incorrecto'

    def rectangulo(self, base, altura):
        try:
            if base < 0 or altura < 0:
                return 'dato incorrecto'
            else:
                base = float(base)
                altura = float(altura)
                return base * altura
        except Exception:
            return 'dato incorrecto'

    def triangulo(self, base, altura):
        try:
            if base < 0 or altura < 0:
                return 'dato incorrecto'
            else:
                base = float(base)
                altura = float(altura)
                return (base * altura) / 2
        except Exception:
            return 'dato incorrecto'

    def circunferencia(self, radio):
        try:
            if radio < 0:
                return 'dato incorrecto'
            else:
                radio = float(radio)
                return m.pi * m.pow(radio, 2)
        except Exception:
            return 'dato incorrecto'
