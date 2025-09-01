# -*- coding: utf-8 -*-
import unittest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import lenguajes as lg

class TestLenguajes(unittest.TestCase):
    def test_union_basica(self):
        self.assertEqual(lg.union_lenguajes(lg.L1, lg.L2), {'a','b','ab','ba','b','c','bc','cb'} | set())

    def test_interseccion_basica(self):
        self.assertEqual(lg.interseccion_lenguajes(lg.L1, lg.L2), {'b'})

    def test_concatenacion_epsilon(self):
        A = {'0','1'}
        B = {lg.EPSILON, '00'}
        esperado = {'0', '1', '000', '100'}
        self.assertEqual(lg.concatenacion_lenguajes(A,B), esperado)

    def test_pertenencia(self):
        self.assertFalse(lg.pertenece("abc", lg.union_lenguajes(lg.L1, lg.L2)))
        self.assertTrue(lg.pertenece("cab", lg.concatenacion_lenguajes(lg.L3, lg.L4)))

if __name__ == "__main__":
    unittest.main()
