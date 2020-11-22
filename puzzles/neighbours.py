import unittest


def compute(states, days):
    for i in range(days):
        states = compute_epoch(states)
    return states


def compute_epoch(states):
    new_states = []
    for j in range(len(states)):
        if get_state(states, j - 1) == get_state(states, j + 1):
            new_states.append(0)
        else:
            new_states.append(1)
    return new_states


def get_state(states, i):
    if i < 0 or i > len(states) - 1:
        return 0
    else:
        return states[i]


class TestCompute(unittest.TestCase):
    def test_get_state(self):
        self.assertEqual(get_state([1, 0, 0, 0, 0, 1, 0, 1], -1), 0)
        self.assertEqual(get_state([1, 0, 0, 0, 0, 1, 0, 1], 8), 0)
        self.assertEqual(get_state([1, 0, 0, 0, 0, 1, 0, 1], 7), 1)
        self.assertEqual(get_state([1, 0, 0, 0, 0, 1, 0, 1], 6), 0)

    def test_first(self):
        self.assertEqual(
            compute([1, 0, 0, 0, 0, 1, 0, 0], 1), [0, 1, 0, 0, 1, 0, 1, 0]
        )

    def test_second(self):
        self.assertEqual(
            compute([1, 1, 1, 0, 1, 1, 1, 1], 2), [0, 0, 0, 0, 0, 1, 1, 0]
        )


if __name__ == "__main__":
    unittest.main()
