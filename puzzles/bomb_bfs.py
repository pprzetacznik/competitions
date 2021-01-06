from queue import Queue
from typing import Optional, Dict, Set, List, Tuple
from unittest import main, TestCase

State = int
Path = List[State]
States = Set[State]
NeighboursGraph = Dict[State, Set[State]]
VisitedDict = Dict[State, Tuple[str, State]]


class BombSolver:
    def __init__(
        self,
        accepted_states: States,
        initial_state: State,
        final_state: State,
        length: int,
    ) -> None:
        self.accepted_states = accepted_states
        self.initial_state = initial_state
        self.final_state = final_state
        self.length = length

    def is_path(self) -> bool:
        return bool(self.find_path())

    def find_path(self) -> Optional[Path]:
        neighbours_graph: NeighboursGraph = self._create_neighbours()
        visited_dict: VisitedDict = {}
        q = Queue()
        q.put((self.initial_state, "A", None))
        q.put((self.final_state, "B", None))
        while not q.empty():
            (state, start, previous) = q.get()
            if state in visited_dict:
                start_visited, previous_visited = visited_dict[state]
                if start is not start_visited:
                    return self._recreate_path(visited_dict, previous, state)
            else:
                visited_dict[state] = start, previous
                for neighbour in neighbours_graph[state]:
                    if neighbour not in visited_dict:
                        q.put((neighbour, start, state))
        return None

    def _recreate_path(self, visited_dict, a_state, b_state) -> Path:
        def traverse_to_beginning(path, state):
            while state:
                path.append(state)
                _, state = visited_dict[state]
            return path

        path = traverse_to_beginning([], a_state)
        path = list(reversed(path))
        path = traverse_to_beginning(path, b_state)
        if path[0] == self.final_state:
            path = list(reversed(path))
        return path

    def _create_neighbours(self) -> NeighboursGraph:
        neighbours_graph: NeighboursGraph = {
            state: {
                state_candidate
                for state_candidate in [
                    self._toggle_nth(state, i) for i in range(self.length)
                ]
                if state_candidate in self.accepted_states
            }
            for state in self.accepted_states
        }
        return neighbours_graph

    def _toggle_nth(self, state: State, n: int) -> State:
        if n > self.length:
            raise Exception("n too big")
        return state ^ (1 << n)


class TestBomb(TestCase):
    def test_bomb_positive(self):
        bomb_solver = BombSolver(
            accepted_states={
                0b1000,
                0b1001,
                0b1011,
                0b1010,
                0b1110,
                0b1011,
                0b1111,
            },
            initial_state=0b1110,
            final_state=0b1011,
            length=4,
        )
        self.assertTrue(bomb_solver.is_path())
        if bomb_solver.is_path():
            print([f"{i:b}" for i in bomb_solver.find_path()])

    def test_bomb_negative(self):
        bomb_solver = BombSolver(
            accepted_states={0b1000, 0b1001, 0b1011, 0b1110, 0b1011},
            initial_state=0b1110,
            final_state=0b1011,
            length=4,
        )
        self.assertFalse(bomb_solver.is_path())
        self.assertIsNone(bomb_solver.find_path())


if __name__ == "__main__":
    main()
