from calc import soma
import unittest


class TestesPrincipais(unittest.TestCase):

    def test_soma(self):

        resultado = soma(2,3)
        self.assertEqual(5,resultado)
