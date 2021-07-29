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

    def test_metodos_magicos_comparaciones(self):  
        uno = RomanNumber(1)
        dos = RomanNumber(2)

        self.assertEqual (uno, 1)
        self.assertEqual (uno, 1.0)
        with self.assertRaises(ValueError):
            self.assertEqual(uno, {})

        self.assertNotEqual (uno, 1.1)
        self.assertNotEqual (uno, 2)
        self.assertNotEqual (uno, "II")
        with self.assertRaises(ValueError):
            self.assertEqual(uno, {})

        self.assertTrue (uno < "II")
        self.assertTrue (uno < 1.3)
        self.assertTrue (dos > "I")
        self.assertFalse (dos > "DI")
        self.assertTrue (dos > 1.3)
        self.assertTrue (dos > uno)
        self.assertTrue (uno < "II")
        self.assertTrue (uno <= "DI")
        self.assertTrue (uno <= "I")
        with self.assertRaises(ValueError):
            dos > {}