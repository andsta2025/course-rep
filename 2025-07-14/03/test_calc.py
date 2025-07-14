import unittest
from calc import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        print("\nSetting up Calculator instance...")
        self.calc = Calculator()

    def tearDown(self):
        print("Tearing down Calculator instance...")
        del self.calc

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertNotEqual(self.calc.add(-1, -1), 0)
        self.assertTrue(self.calc.add(0, 0) == 0)

    @unittest.skip("Skipping subtraction test: feature not ready")
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertTrue(self.calc.subtract(0, 5) < 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(0, 100), 0)


    @unittest.expectedFailure
    def test_divide(self):
        # Intentionally using wrong expected result to show expected failure
        self.assertEqual(self.calc.divide(10, 2), 6)  # should be 5, so this will fail
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()