import unittest
from romanclass import RomanNumber

class RomanNumberClassTests(unittest.TestCase):
    def test_Crear_Numero_romano(self):
        uno = RomanNumber(1)

        self.assertEqual(uno.cadena,"I")       
        self.assertEqual(uno.valor, 1)
        self.assertEqual(uno.cadena,"I")

        with self.assertRaises(ValueError):
            cuatromil = RomanNumber(4000)
        
        dos = RomanNumber ("II")
        self.assertEqual(dos.valor, 2)
        self.assertEqual(dos.cadena, "II")

    def test_metodos_magicos(self):
        uno = RomanNumber(1)

        self.assertEqual (uno, "I")
        self.assertLess (uno, "II")