import unittest
from typing import List, Dict

Repetitions = Dict[str, int]


def pattern_to_dict(pattern: str) -> Repetitions:
    repetitions = {}
    for c in pattern:
        repetitions[c] = repetitions.get(c, 0) + 1
    return repetitions


def permutations_matching(text: str, pattern: str) -> List[int]:
    text_length = len(text)
    pattern_length = len(pattern)
    pattern_repetitions = pattern_to_dict(pattern)
    q_repetitions = {}
    q_catched = 0
    results = []
    for new_letter_index in range(text_length):
        q_beginning = new_letter_index - pattern_length + 1
        new_letter = text[new_letter_index]
        old_letter = None if q_beginning - 1 < 0 else text[q_beginning - 1]
        if new_letter in pattern_repetitions:
            q_catched += 1
            q_repetitions[new_letter] = q_repetitions.get(new_letter, 0) + 1
        if old_letter in pattern_repetitions:
            q_catched -= 1
            q_repetitions[old_letter] -= 1
        if (
            q_catched == pattern_length
            and q_repetitions.get(old_letter, 0)
            == pattern_repetitions.get(old_letter, 0)
            and q_repetitions.get(new_letter, 0)
            == pattern_repetitions.get(new_letter, 0)
        ):
            results.append(q_beginning)
    return results


class TestPatternPermutations(unittest.TestCase):
    def test_permutations_matching(self):
        self.assertEqual(
            permutations_matching("abcdabcaabdaabc", "baac"), [4, 5, 6, 11]
        )


if __name__ == "__main__":
    unittest.main()
