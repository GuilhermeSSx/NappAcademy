import unittest
from exercicio06 import calculo_porcentagem_entre_0_e_1

class CalculoPorcentagemTestCase(unittest.TestCase):
    def test_calculo_porcentagem_cenario_1(self):
        self.assertEqual(50, calculo_porcentagem_entre_0_e_1(50, 1))
        self.assertEqual(0, calculo_porcentagem_entre_0_e_1(50, 0))

if __name__ == '__main__':
    unittest.main()