"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc

class CalTest(SimpleTestCase):
    """Test the cal module"""
    
    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)
        
        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """Test substracting numbers"""
        res = calc.substract(15, 10)
        
        self.assertEqual(res, 5)