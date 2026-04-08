import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        assert 2 * 2 == 4
        assert 4 *3 == 12
        assert 5 * 4 == 20

    def test_divide(self): # 3 assertions
        assert 4 / 2 == 2
        assert 8 / 2 == 4
        assert 10 / 5 == 2
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
             logarithm(0, 5)
    def test_hypotenuse(self): # 3 assertions
        assert hypotenuse(3, 4) == 5
        assert hypotenuse(5, 12) == 13
        assert hypotenuse(0, 0) == 0

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-10)
        with self.assertRaises(ValueError):
            square_root(-5)
        with self.assertRaises(ValueError):
            square_root(-2)
        ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()