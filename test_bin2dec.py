import unittest
from bin2dec import bin2dec


class TestBin2Dec(unittest.TestCase):
    """Test cases for the bin2dec function"""
    
    def test_single_digit_zero(self):
        """Test converting '0' to 0"""
        self.assertEqual(bin2dec('0'), 0)
    
    def test_single_digit_one(self):
        """Test converting '1' to 1"""
        self.assertEqual(bin2dec('1'), 1)
    
    def test_two_digits(self):
        """Test converting 2-digit binary strings"""
        self.assertEqual(bin2dec('10'), 2)
        self.assertEqual(bin2dec('11'), 3)
        self.assertEqual(bin2dec('01'), 1)
    
    def test_three_digits(self):
        """Test converting 3-digit binary strings"""
        self.assertEqual(bin2dec('100'), 4)
        self.assertEqual(bin2dec('101'), 5)
        self.assertEqual(bin2dec('110'), 6)
        self.assertEqual(bin2dec('111'), 7)
    
    def test_four_digits(self):
        """Test converting 4-digit binary strings"""
        self.assertEqual(bin2dec('1000'), 8)
        self.assertEqual(bin2dec('1111'), 15)
    
    def test_eight_digits(self):
        """Test converting 8-digit binary strings (max length)"""
        self.assertEqual(bin2dec('10000000'), 128)
        self.assertEqual(bin2dec('11111111'), 255)
        self.assertEqual(bin2dec('10101010'), 170)
        self.assertEqual(bin2dec('01010101'), 85)
    
    def test_leading_zeros(self):
        """Test that leading zeros are handled correctly"""
        self.assertEqual(bin2dec('00000001'), 1)
        self.assertEqual(bin2dec('00001111'), 15)
    
    def test_whitespace_handling(self):
        """Test that whitespace is stripped"""
        self.assertEqual(bin2dec(' 101 '), 5)
        self.assertEqual(bin2dec('  1111  '), 15)
    
    def test_empty_string(self):
        """Test that empty string raises ValueError"""
        with self.assertRaises(ValueError) as context:
            bin2dec('')
        self.assertIn("empty", str(context.exception).lower())
    
    def test_empty_whitespace(self):
        """Test that whitespace-only string raises ValueError"""
        with self.assertRaises(ValueError) as context:
            bin2dec('   ')
        self.assertIn("empty", str(context.exception).lower())
    
    def test_too_long(self):
        """Test that strings longer than 8 digits raise ValueError"""
        with self.assertRaises(ValueError) as context:
            bin2dec('111111111')  # 9 digits
        self.assertIn("8 digits", str(context.exception).lower())
    
    def test_invalid_characters(self):
        """Test that non-binary characters raise ValueError"""
        with self.assertRaises(ValueError) as context:
            bin2dec('102')
        self.assertIn("0", str(context.exception))
        self.assertIn("1", str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            bin2dec('abc')
        
        with self.assertRaises(ValueError) as context:
            bin2dec('10 10')
    
    def test_non_string_input(self):
        """Test that non-string input raises ValueError"""
        with self.assertRaises(ValueError) as context:
            bin2dec(101)
        self.assertIn("string", str(context.exception).lower())
        
        with self.assertRaises(ValueError) as context:
            bin2dec(None)


if __name__ == '__main__':
    unittest.main()
