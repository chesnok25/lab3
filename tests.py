import unittest
import math
from project import Geometric_mean
class TestGeometric(unittest.TestCase):
    def test_Geo(self):
        self.assertEqual(Geometric_mean(10,10),10)
        self.assertEqual(Geometric_mean(-10,10),"one argument is negative")
        self.assertEqual(Geometric_mean(10,-10),"one argument is negative")
        self.assertEqual(Geometric_mean(3,12),6)
        self.assertEqual(Geometric_mean(8,32),16)
    def test_types(self):
        with self.assertRaises(TypeError):
            Geometric_mean([10],[10])
        with self.assertRaises(TypeError):
            Geometric_mean("10","10")
        with self.assertRaises(TypeError):
            Geometric_mean(1 + 1j,2 + 1j)
        with self.assertRaises(TypeError):
            Geometric_mean(1 + 3j,4 + 5j)