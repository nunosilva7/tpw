import unittest
import tabuada as t



class MyTestCase(unittest.TestCase):
    def test_something(self):
        calculada=t.tabuada(3)
        expected=['3x1 = 3',
                  '3x2 = 6',
                  '3x3 = 9',
                  '3x4 = 12',
                  '3x5 = 15',
                  '3x6 = 18',
                  '3x7 = 21',
                  '3x8 = 24',
                  '3x9 = 27',
                  '3x10 = 30',]

        self.assertListEqual(expected,calculada)


if __name__ == '__main__':
    unittest.main()
