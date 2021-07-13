import unittest
from calculator1 import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calc=Calculator()

    def test_add(self):

        ##self.assertEqual(self.calc.add(2,3),5)

        
        valor, numeral, textual = self.calc.add(2,3, 'a')
        self.assertEqual(valor,5)
        self.assertEqual(numeral, "2+3 = 5")
        self.assertEqual(textual, 'dois mais três é igual a cinco')

    def test_add_dec(self):
        res, s, textual=self.calc.add(5.3, 4)
        self.assertEqual(res, 9.3)
        self.assertEqual(s,'5.3+4 = 9.3')



    def test_addNeg(self):
        valor, numeral, textual = self.calc.add(-45, 98, 'a')
        self.assertEqual(valor, 53)
        self.assertEqual(numeral, "-45+98 = 53")
        self.assertEqual(textual, 'menos quarenta e cinco mais noventa e oito é igual a cinquenta e três')

    def test_add_neg1(self):
        res, s, textual = self.calc.add(2, -3)
        self.assertEqual(res, -1)
        self.assertEqual(s, "2+-3 = -1")

    def test_add_null(self):
        res, s, textual = self.calc.add(3, 0)
        self.assertEqual(res, 3)
        self.assertEqual(s, "3+0 = 3")

    """
        def test_add_invalid_value(self):
            self.assertRaises(TypeError, self.calc.add, "dois", "tr3s!")
    """

    # Subtração
    def test_sub(self):
        res, s = self.calc.sub(5, 3)
        self.assertEqual(res, 2)
        self.assertEqual(s, "5-3 = 2")

    def test_sub_resneg(self):
        res, s = self.calc.sub(5, 7)
        self.assertEqual(res, -2)
        self.assertEqual(s, "5-7 = -2")

    def test_sub_neg(self):
        res, s = self.calc.sub(-5, 3)
        self.assertEqual(res, -8)
        self.assertEqual(s, "-5-3 = -8")

    def test_sub_neg2(self):
        res, s = self.calc.sub(-5, -3)
        self.assertEqual(res, -2)
        self.assertEqual(s, "-5--3 = -2")

    def test_sub_dec(self):
        res, s = self.calc.sub(5, .3)
        self.assertEqual(res, 4.7)
        self.assertEqual(s, "5-0.3 = 4.7")

    """
        def test_sub_invalid_value(self):
            self.assertRaises(TypeError, self.calc.sub, "dois", "tr3s!")
    """

    # Multiplicação
    def test_mul(self):
        res, s = self.calc.mult(2, 3)
        self.assertEqual(res, 6)
        self.assertEqual(s, "2x3 = 6")

    def test_mul_zero(self):
        res, s = self.calc.mult(2, 0)
        self.assertEqual(res, 0)
        self.assertEqual(s, "2x0 = 0")

    """

        def test_multiply_invalid_value(self):
            self.assertRaises(TypeError, self.calc.mul, "dois", "tr3s!")
    """

    # Divisão
    def test_div(self):
        res, s = self.calc.div(10, 2)
        self.assertEqual(res, 5)
        self.assertEqual(s, "10/2 = 5.0")

    def test_div_dec(self):
        res, s = self.calc.div(10, .5)
        self.assertEqual(res, 20)
        self.assertEqual(s, "10/0.5 = 20.0")

    def test_div_zero(self):
        self.assertRaises(ZeroDivisionError, self.calc.div, 1, 0)

    """
        def test_div_invalid_value(self):
            self.assertRaises(TypeError, self.calc.div, "dois", "tr3s!")
    """


if __name__ == '__main__':
    unittest.main()
