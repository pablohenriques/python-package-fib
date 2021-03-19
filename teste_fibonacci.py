import unittest

from fibonacci import fibonacci as fibo
from values import cache

class TesteFibonnaci(unittest.TestCase):

    def unique(self, item):
        self.assertEqual(cache[item], fibo.sum(item))

    def test_many_values(self):
        for i in range(301):
            self.unique(i)

if __name__ == "__main__":
    unittest.main()