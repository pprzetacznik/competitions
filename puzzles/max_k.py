import unittest
from typing import List, Tuple, Dict


class MinKSolver:
    @classmethod
    def solve(cls, numbers_list: List[int], k: int) -> int:
        left_sum = cls._partial_sum(numbers_list)
        right_sum = cls._partial_sum(reversed(numbers_list))
        if k >= len(numbers_list):
            return left_sum[-1]
        left_counter = 0
        min_sum = left_sum[k]
        for left_counter in range(1, k + 1):
            right_counter = k - left_counter if k > 0 else 0
            min_sum = min(
                min_sum, left_sum[left_counter] + right_sum[right_counter]
            )
        return min_sum

    @classmethod
    def _partial_sum(cls, numbers_list: List[int]) -> List[int]:
        sum_list = [0]
        for item in numbers_list:
            sum_list += [sum_list[-1] + item]
        return sum_list


HistoryEntry = Tuple[int]
HistoryDict = Dict[HistoryEntry, int]


class MinKRecursiveSolver:
    @classmethod
    def solve(cls, numbers_list: List[int], k: int) -> int:
        return cls.solve_details(
            numbers_list, k, current_sum=0, history=(0, 0), history_cache={},
        )

    @classmethod
    def solve_details(
        cls,
        numbers_list: List[int],
        k: int,
        current_sum: int,
        history: HistoryEntry,
        history_cache: HistoryDict,
    ) -> int:

        if history in history_cache:
            return history_cache[history]
        if not numbers_list or k <= 0:
            history_cache[history] = current_sum
            return current_sum

        lower_sum = min(
            cls.solve_details(
                numbers_list[1:],
                k - 1,
                current_sum=current_sum + numbers_list[0],
                history=(history[0] + 1, history[1]),
                history_cache=history_cache,
            ),
            cls.solve_details(
                numbers_list[:-1],
                k - 1,
                current_sum=current_sum + numbers_list[-1],
                history=(history[0], history[1] + 1),
                history_cache=history_cache,
            ),
        )
        history_cache[history] = lower_sum
        return lower_sum


class TestBom(unittest.TestCase):
    def test_min_k(self):
        self.assertEqual(
            MinKSolver.solve([7, 8, 1, 3, 4, 5, 7, 3, 2, 8, 9], 1), 7
        )
        self.assertEqual(
            MinKSolver.solve([7, 8, 1, 3, 4, 5, 7, 3, 2, 8, 9], 2), 15
        )
        self.assertEqual(
            MinKSolver.solve([7, 8, 1, 3, 4, 5, 7, 3, 2, 8, 9], 3), 16
        )
        self.assertEqual(
            MinKSolver.solve([7, 8, 1, 3, 4, 5, 7, 3, 2, 8, 9], 4), 19
        )
        self.assertEqual(MinKSolver.solve([1, 3, 5, 7, 6, 4, 2], 0), 0)
        self.assertEqual(MinKSolver.solve([1, 3, 5, 7, 6, 4, 2], 10), 28)

    def test_min_k_recursive(self):
        self.assertEqual(
            MinKRecursiveSolver.solve([7, 8, 1, 3, 4, 5, 7, 3, 2, 8, 9], 1), 7
        )
        self.assertEqual(
            MinKRecursiveSolver.solve([7, 8, 1, 3, 4, 5, 7, 3, 2, 8, 9], 2), 15
        )
        self.assertEqual(
            MinKRecursiveSolver.solve([7, 8, 1, 3, 4, 5, 7, 3, 2, 8, 9], 3), 16
        )
        self.assertEqual(
            MinKRecursiveSolver.solve([7, 8, 1, 3, 4, 5, 7, 3, 2, 8, 9], 4), 19
        )
        self.assertEqual(
            MinKRecursiveSolver.solve([1, 3, 5, 7, 6, 4, 2], 0), 0
        )
        self.assertEqual(
            MinKRecursiveSolver.solve([1, 3, 5, 7, 6, 4, 2], 10), 28
        )


if __name__ == "__main__":
    unittest.main()
