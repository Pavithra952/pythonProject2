import unittest
from testprogram2 import program2
class My_test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(program2.rlist1([10,20,30]),[30,20,10])
    def test_case2(self):
        self.assertEqual(program2.rlist1()[-1.2,1.3,1.6]