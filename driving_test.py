import unittest  # Import Python's built-in unit testing framework
from main_file import can_drive  # Import the function to test

# Create a test case class that inherits from unittest.TestCase
class TestCanDrive(unittest.TestCase):

    def test_underage(self):
        # Test a person under 16 (should return False)
        self.assertFalse(can_drive(15))

    def test_exact_age(self):
        # Test someone exactly 16 (should return True)
        self.assertTrue(can_drive(16))

    def test_above_age(self):
        # Test someone older than 16 (should return True)
        self.assertTrue(can_drive(18))

    def test_negative_age(self):
        # Negative age is invalid (should return False)
        self.assertFalse(can_drive(-3))

    def test_edge_case(self):
        # Very close to 16 but not quite (should return False)
        self.assertFalse(can_drive(15.9))

# If this file is run directly, run the tests
if __name__ == "__main__":
    unittest.main()

