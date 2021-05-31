import unittest
from exercicio08 import juros_compostos

class CalculoJurosCompostosTestCase(unittest.TestCase):
    def test_calculo_juros_compostos_cenario_1(self):
        self.assertEqual(400, juros_compostos(100, 100, 2))
        self.assertEqual(10, juros_compostos(10, 0, 1))

if __name__ == '__main__':
    unittest.main()