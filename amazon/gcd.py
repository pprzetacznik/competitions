import unittest


def generalizedGCD(num, arr):
    if num > 0:
        prev = arr[0]
    for i in arr[1:]:
        prev = gcd(prev, i)
    return prev


def gcd(a, b):
    if b < a:
        a, b = b, a
    if a == 1:
        return 1
    if a == 0:
        return b
    return gcd(b % a, a)


class TestCompute(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(5, 15), 5)
        self.assertEqual(gcd(2, 10), 2)
        self.assertEqual(gcd(111, 1), 1)

    def test_first(self):
        self.assertEqual(generalizedGCD(5, [2, 3, 4, 5, 6]), 1)

    def test_second(self):
        self.assertEqual(generalizedGCD(5, [2, 4, 6, 8, 10]), 2)


if __name__ == "__main__":
    unittest.main()
