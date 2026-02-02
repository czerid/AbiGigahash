# test_abigigahash.py
"""
Tests for AbiGigahash module.
"""

import unittest
from abigigahash import AbiGigahash

class TestAbiGigahash(unittest.TestCase):
    """Test cases for AbiGigahash class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AbiGigahash()
        self.assertIsInstance(instance, AbiGigahash)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AbiGigahash()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
