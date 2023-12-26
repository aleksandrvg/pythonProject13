import unittest

import main


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here


class ReverseTest1(unittest.TestCase):
    def testReverse(self):
        self.assertEqual(main.Reverse([1, 2, 3]), [3, 2, 1], "Массив должен быть перевернут")


class ReverseTest2(unittest.TestCase):
    def testSquare(self):
        self.assertEqual(main.Square(2), 4, "Значение в квадрате")


class ReverseTest3(unittest.TestCase):
    def testSquare(self):
        self.assertEqual(main.Square(-3), 9, "Значение в квадрате")


if __name__ == '__main__':
    unittest.main()
