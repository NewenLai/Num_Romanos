import unittest
from romanos import convSimbolos


class RomanosTests(unittest.TestCase):
    def test_Numeros_romanos(self):
        self.assertEqual(convSimbolos("I"), 1)
        self.assertEqual(convSimbolos("V"), 5)

    def test_Numeros_complejos(self):
        self.assertEqual(convSimbolos("XXV"), 25)
        self.assertEqual(convSimbolos("CDXXIV"), 424)
    
    def test_no_se_resta_ni_v_ni_L_ni_D(self): 
        with self.assertRaises(ValueError):
            convSimbolos("VC")
            convSimbolos("IL")

    def test_no_se_resta_mas_de_un_salto(self):
        self.assertEqual(convSimbolos("IV"), 4)
        self.assertEqual(convSimbolos("XL"), 40)
        self.assertEqual(convSimbolos("CD"), 400)
        self.assertEqual(convSimbolos("XC"), 90)
        with self.assertRaises(ValueError):
            convSimbolos("IM")
            convSimbolos("IL")
            convSimbolos("XM")
    #def tests_no_mas_de_tres_repeticiones(self):

