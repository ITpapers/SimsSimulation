import unittest
from libtest import *

class MY_Test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2,2),4)
    def test_kwargs(self):
        self.assertEqual(adder(a=10,b=3),13)

    def test_mixed(self):
        self.assertEqual(adder(10,b=3),13)

    def test_different(self):
        x = 10
        y=0
        self.assertEqual(adder(0, -5, y, a=x,b=3),8)

    def test_wrong_datatype(self):
        self.assertEqual(adder("abc", 7, b=3), 10)

    def test_wrong_datatype2(self):
        self.assertEqual(adder("abc", 7, b=3, xx="XXX"), 10)

    def test_wrong_datatype3(self):
        self.assertEqual(adder(True, "abc", 7, b=3, xx="XXX"), 11)

    def test_wrong_datatype4(self):
        self.assertEqual(adder(False, "abc", 7, b=3, xx="XXX"), 10)

    def test_wrong_datatype3(self):
        self.assertEqual(adder(True, "abc", 7, b=3, xx="XXX", y=False), 11)

    def test_wrong_datatype4(self):
        self.assertEqual(adder(False, "abc", 7, b=3, xx="XXX", y=True), 11)

if __name__ == "__main__":
    unittest.main()
