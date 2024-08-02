import unittest
from paquetes.operacionesBasicas.operaciones import sumar, restar, multiplicar, dividir

class PruebasHola(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2, 5), 7)
        self.assertEqual(sumar(-8, 12), 4)
        self.assertEqual(sumar(-5, -7), -12)

    def test_restar(self):
        self.assertEqual(restar(2, 5), -3)
        self.assertEqual(restar(6, 2), 4)
        self.assertEqual(restar(-8, 12), -20)
        self.assertEqual(restar(-5, -7), 2)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 5), 10)
        self.assertEqual(multiplicar(-8, 4), -32)
        self.assertEqual(multiplicar(-5, -7), 35)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(-12, 4), -3)
        self.assertEqual(dividir(12, -4), -3)
        self.assertEqual(dividir(-35, -7), 5)
