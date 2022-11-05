import unittest
import os


class Test_test1(unittest.TestCase):
    def test_A(self):
        self.assertEqual(True,True)



class Test_test1(unittest.TestCase):
    def test_A(self):
        if False:
            self.fail("Not implemented")
        else:
            self.assertTrue(True)

class UneClasseDeTest(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(True)


class Test_test2(unittest.TestCase):
    def test_B(self):
        print(False)
        return False

class Test_Config(unittest.TestCase):
    def test_config(self):
        self.assertEqual(8000, 8000)




if __name__ == '__main__':
    unittest.main()