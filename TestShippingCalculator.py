import unittest

import ShippingCalculator

class KnownValues(unittest.TestCase):
    known_values = ( (-1, 0),
                     (0, 0),
                     (.99, 5.99),
                     (10, 15),
                     (19.99, 24.99),
                     (20.00, 30.00),
                     (33.50, 43.50),
                     (49.99, 59.99),
                     (50, 65),
                     (75.25, 90.25),
                     (99.99, 114.99),
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

