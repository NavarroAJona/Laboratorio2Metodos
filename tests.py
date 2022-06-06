import pokemon
import unittest
import numpy as np
import numpy.testing as nptest

class TestPokemon(unittest.TestCase):
    def test_calculate_transitions(self):
        words = ['$hello$', '$world$']
        sequences = ['$','d','e','h','l','o','r','w']
        expectedOutputPython = [[0, 0, 0, 0.5, 0, 0, 0, 0.5],
                          [1, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 0, 0],
                          [0, 1.0/3, 0, 0, 1.0/3, 1.0/3, 0, 0],
                          [0.5, 0, 0, 0, 0, 0, 0.5, 0],
                          [0, 0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1, 0, 0]]
        expectedOutputNumpy = np.array(expectedOutputPython)
        nptest.assert_array_equal(pokemon.calculate_transitions(words,sequences),expectedOutputNumpy, 
                        "Deberia dar la matriz {expectedOutput}")

if __name__ == '__main__':
    unittest.main()