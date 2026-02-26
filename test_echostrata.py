# test_echostrata.py
"""
Tests for EchoStrata module.
"""

import unittest
from echostrata import EchoStrata

class TestEchoStrata(unittest.TestCase):
    """Test cases for EchoStrata class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EchoStrata()
        self.assertIsInstance(instance, EchoStrata)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EchoStrata()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
