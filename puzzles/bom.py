import unittest
from typing import Dict, Tuple


Code = Tuple[int]
CodeSet = Dict[Code, bool]


def find_disarm_pattern(
    bomb_pattern: Code,
    disarm_pattern: Code,
    safe_patterns: CodeSet,
    previous_bomb_patterns_set: CodeSet,
) -> bool:
    print("previous_bomb_patterns_set: {}".format(previous_bomb_patterns_set))
    print("bomb_pattern: {}".format(bomb_pattern))

    if bomb_pattern in previous_bomb_patterns_set:
        return False
    if bomb_pattern == disarm_pattern:
        return True
    possible_bomb_patterns = [bomb_pattern] * len(bomb_pattern)
    for i in range(len(possible_bomb_patterns)):
        single_bomb_pattern = switch_element_in_code(
            possible_bomb_patterns[i], i
        )
        if single_bomb_pattern in safe_patterns:
            previous_bomb_patterns_set_new = previous_bomb_patterns_set.copy()
            previous_bomb_patterns_set_new[bomb_pattern] = True
            if find_disarm_pattern(
                single_bomb_pattern,
                disarm_pattern,
                safe_patterns,
                previous_bomb_patterns_set_new,
            ):
                return True
    return False


def switch_element_in_code(code: Code, i):
    new_code = list(code)
    new_code[i] = 1 if not new_code[i] else 0
    return tuple(new_code)


class TestBom(unittest.TestCase):
    def test_switch_element(self):
        self.assertEqual(switch_element_in_code((1, 0, 1), 1), (1, 1, 1))

    def test_find(self):
        self.assertTrue(
            find_disarm_pattern(
                bomb_pattern=(0, 1, 0),
                disarm_pattern=(1, 1, 1),
                safe_patterns={
                    (0, 0, 0): True,
                    (0, 0, 1): True,
                    (0, 1, 0): True,
                    (1, 0, 1): True,
                    (1, 1, 1): True,
                },
                previous_bomb_patterns_set={},
            )
        )


if __name__ == "__main__":
    unittest.main()
