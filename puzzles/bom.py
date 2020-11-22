import unittest
from typing import Dict, Tuple, Set
from heapq import heappush, heappop


Code = Tuple[int]
CodeSet = Dict[Code, bool]


def find_disarm_pattern(
    bomb_pattern: Code,
    disarm_pattern: Code,
    safe_patterns: CodeSet,
    previous_bomb_patterns_set: CodeSet,
) -> bool:
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


Distances = Dict[Tuple[Code, Code], int]

Neighbours = Dict[Code, Set[Code]]

Previous = Dict[Code, Code]


def find_edges(safe_patterns: CodeSet) -> Neighbours:
    neighbours: Neighbours = {}
    for (code, _) in safe_patterns.items():
        vertex_list = []
        for i in range(len(code)):
            new_code = switch_element_in_code(code, i)
            if new_code in safe_patterns:
                vertex_list.append(new_code)
        neighbours[code] = set(vertex_list)
    return neighbours


def find_disarm_pattern_graph(
    bomb_pattern: Code, disarm_pattern: Code, safe_patterns: CodeSet,
) -> bool:
    neighbours = find_edges(safe_patterns)
    distances: Distances = {}
    previous: Previous = {}
    minheap = []
    for (key, value) in safe_patterns.items():
        if key is bomb_pattern:
            distances[(bomb_pattern, key)] = 0
            heappush(minheap, (0, (bomb_pattern, key)))
        else:
            distances[(bomb_pattern, key)] = len(safe_patterns)
            heappush(minheap, (len(safe_patterns), (bomb_pattern, key)))

    while minheap:
        print(minheap)
        (distance, (vertex_from, vertex_to)) = heappop(minheap)
        print(vertex_to)
        for vertex in neighbours[vertex_to]:
            if (
                distances[(vertex_from, vertex)]
                > distances[(vertex_from, vertex_to)] + 1
            ):
                distances[(vertex_from, vertex)] = (
                    distances[(vertex_from, vertex_to)] + 1
                )
                previous[vertex] = vertex_to

    print(distances)
    print(previous)
    print(distances[(bomb_pattern, disarm_pattern)])
    return True


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

    def test_solver_graph(self):
        self.assertTrue(
            find_disarm_pattern_graph(
                bomb_pattern=(0, 1, 0),
                disarm_pattern=(1, 1, 1),
                safe_patterns={
                    (0, 0, 0): True,
                    (0, 0, 1): True,
                    (0, 1, 0): True,
                    (1, 0, 1): True,
                    (1, 1, 1): True,
                },
            )
        )


if __name__ == "__main__":
    unittest.main()
