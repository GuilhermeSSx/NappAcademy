import unittest
from exercicio07 import calculo_porcentagem_entre_0_e_100

class CalculoPorcentagemTestCase(unittest.TestCase):
    def test_calculo_porcentagem_cenario_1(self):
        self.assertEqual(50, calculo_porcentagem_entre_0_e_100(50, 100))
        self.assertEqual(0, calculo_porcentagem_entre_0_e_100(50, 0))

if __name__ == '__main__':
    unittest.main()