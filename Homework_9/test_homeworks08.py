import unittest
from homeworks import (
    calculate_goods,
    calculate_computer_cost,
    calculate_order_cost,
    calculate_pages,
    unique_symbols_check
)

class TestHomeworks(unittest.TestCase):

    def test_calculate_goods(self):
        # Позитивный тест
        result = calculate_goods(375291, 250449, 222950)
        self.assertEqual(result, (152341, 98108, 124842))
        
        # Негативный тест
        result = calculate_goods(0, 0, 0)
        self.assertEqual(result, (0, 0, 0))
    
    def test_calculate_computer_cost(self):
        # Позитивный тест
        result = calculate_computer_cost(18, 1179)
        self.assertEqual(result, 21222)
        
        # Негативный тест
        result = calculate_computer_cost(0, 1179)
        self.assertEqual(result, 0)
    
    def test_calculate_order_cost(self):
        # Позитивный тест
        result = calculate_order_cost(4, 2, 4, 1, 3)
        self.assertEqual(result, 2085)
        
        # Негативный тест
        result = calculate_order_cost(0, 0, 0, 0, 0)
        self.assertEqual(result, 0)
    
    def test_calculate_pages(self):
        # Позитивный тест
        result = calculate_pages(232, 8)
        self.assertEqual(result, 29)
        
        # Негативный тест
        result = calculate_pages(0, 8)
        self.assertEqual(result, 0)
    
    def test_unique_symbols_check(self):
        # Позитивный тест
        result = unique_symbols_check("abcdefghijk")
        self.assertTrue(result)
        
        # Негативный тест
        result = unique_symbols_check("abc")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
