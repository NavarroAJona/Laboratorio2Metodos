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
    def test_calculate_transitions_bigrams(self):
        words = ['$$hello$$', '$$world$$']
        sequences = ['$$', '$h', '$w', 'd$', 'el', 'he', 'ld', 'll', 'lo', 'o$', 'or', 'rl', 'wo']
        expectedoutputpython = [[0,  0.5, 0.5, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
                                [0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0 ],
                                [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1 ],
                                [1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
                                [0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0 ],
                                [0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0 ],
                                [0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
                                [0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0 ],
                                [0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0 ],
                                [1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
                                [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0 ],
                                [0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0 ],
                                [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0 ]]
        expectedoutputnumpy = np.array(expectedoutputpython)
        nptest.assert_array_equal(pokemon.calculate_transitions(words,sequences),expectedoutputnumpy, 
                        "deberia dar la matriz {expectedoutput}")
    
    def test_pokemon_names(self):
        palabras = pokemon.load_words("pokemon.csv")
        model = pokemon.create_model(palabras,1)
        self.assertEqual(pokemon.generate_word(model, 17), "Mowaror", "Deberia generar Mowaror")
        model = pokemon.create_model(palabras,2)
        self.assertEqual(pokemon.generate_word(model, 42), "Palassich", "Deberia generar Palassich")
        model = pokemon.create_model(palabras,3)
        self.assertEqual(pokemon.generate_word(model, 21), "Corinoon", "Deberia generar Corinoon")

if __name__ == '__main__':
    unittest.main()