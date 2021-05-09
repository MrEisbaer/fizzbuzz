import unittest

from fizzbuzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    
    def test_fizz_buzz(self):
        assert_value = [
            1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 
            13, 14, 'fizzbuzz', 16, 17, 'fizz', 19, 'buzz', 'fizz', 22, 23, 
            'fizz', 'buzz', 26, 'fizz', 28, 29, 'fizzbuzz', 31, 32, 'fizz', 
            34, 'buzz', 'fizz', 37, 38, 'fizz', 'buzz', 41, 'fizz', 43, 44, 
            'fizzbuzz', 46, 47, 'fizz', 49, 'buzz'
        ]
        self.assertEqual(fizz_buzz(1,50), assert_value)

    def test_fizz_buzz_other_values(self):
        assert_value = [
            1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 
            13, 14, 'fizzbuzz', 16
        ]
        self.assertEqual(fizz_buzz(1,16), assert_value)

if __name__ == '__main__':
    unittest.main()