import unittest


def bin_count(a):
    count = 0
    while a != 0:
        a = a & a - 1
        count += 1
    return count


def max_quality(n, m, a):
    return max_quality_details(a, [i for i in range(0, len(a))], m, 0)


def max_quality_details(a, c, m, acc):
    print(a)
    print(c)
    print("m: {}, acc: {}".format(m, acc))
    print("===============")

    if not a or not c:
        return acc
    bigger = 0
    last_a = a[-1]
    last_c = c[-1]
    for new_last_c in range(last_c, m + 1):
        print("new_last_c: {}".format(new_last_c))
        bigger = max(
            bigger,
            max_quality_details(
                a[:-1],
                c[:-1],
                new_last_c - 1,
                acc + (bin_count(new_last_c) * last_a),
            ),
        )
    print("bigger: {}".format(bigger))
    return bigger


class TestPOP(unittest.TestCase):
    def test_get_state(self):
        self.assertEqual(max_quality(3, 5, [2, -1, 3]), 9)
        self.assertEqual(max_quality(3, 2, [1, 1, -1]), 0)

    def test_bin_count(self):
        self.assertEqual(bin_count(0), 0)
        self.assertEqual(bin_count(1), 1)
        self.assertEqual(bin_count(2), 1)
        self.assertEqual(bin_count(3), 2)
        self.assertEqual(bin_count(4), 1)
        self.assertEqual(bin_count(5), 2)
        self.assertEqual(bin_count(6), 2)
        self.assertEqual(bin_count(7), 3)
        self.assertEqual(bin_count(8), 1)


if __name__ == "__main__":
    unittest.main()
