import unittest

import ShippingCalculator

class KnownValues(unittest.TestCase):
    known_values = ( (-1, 0),
                     (0, 0),
                     (.99, 5.99),
                     (10, 15),
                     (19.99, 24.99),
                     (49.50, 59.50),
                     (50, 65),
                     (99.99, 109.99),
                     (100, 100),
                     (150, 150)
                     )
    def test_getTotalCost(self):
        """ test_totalcost_known_values """
        for i in self.known_values:
            inp = i[0]
            result = ShippingCalculator.getTotalCost(inp)
            expected = i[1]
            self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

