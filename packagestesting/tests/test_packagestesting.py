# test/test_testingpackages.py
import unittest
import importlib.util
import sys
from pathlib import Path

# Add the package directory to sys.path
package_path = Path(__file__).resolve().parents[1] / 'packagestesting'
sys.path.insert(0, str(package_path))

# Import the module
spec = importlib.util.spec_from_file_location("packagestesting", package_path / 'packagestesting.py')
testingpackages = importlib.util.module_from_spec(spec)
spec.loader.exec_module(testingpackages)

class TestAddNumbers(unittest.TestCase):
    def test_add(self):
        self.assertEqual(testingpackages.add_numbers(2, 3), 5)
        self.assertEqual(testingpackages.add_numbers(-1, 1), 0)
        self.assertEqual(testingpackages.add_numbers(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
