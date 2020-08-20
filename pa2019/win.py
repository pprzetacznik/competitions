import unittest
import json


def oldest_wine_traverse(
    wines, graph, stack, availables, oldest, depth, max_depth
):
    print("stack: ", stack)
    print("availables: ", availables)
    print("depth: ", depth)
    if not availables or depth > max_depth:
        print("oldest: {}".format(oldest))
        return oldest

    for item in availables:
        (x, y) = item
        new_stack = stack + [item]
        new_availables = [x for x in availables if x != item]
        if item in graph:
            if (x, y - 1) not in graph or (x, y - 1) in stack:
                new_availables.append(graph[item][0])
            if (x, y + 1) not in graph or (x, y + 1) in stack:
                new_availables.append(graph[item][1])
        oldest = min(
            oldest,
            oldest_wine_traverse(
                wines,
                graph,
                new_stack,
                new_availables,
                min(oldest, wines[item[0]][item[1]]),
                depth + 1,
                max_depth,
            ),
        )
    return oldest


def oldest_wine(wines, max_depth):
    graph = {}
    for i in range(len(wines) - 1):
        for j in range(len(wines[i])):
            index = (i, j)
            print(index)
            graph[index] = [
                (i + 1, j),
                (i + 1, j + 1),
            ]
    graph2 = {"{}:{}".format(x, y): val for ((x, y), val) in graph.items()}
    print(json.dumps(graph2, indent=2))
    return oldest_wine_traverse(wines, graph, [], [(0, 0)], 2020, 1, max_depth)


class TestWin(unittest.TestCase):
    def test_win(self):
        wines = [
            [1999],
            [2019, 2010],
            [850, 1500, 1600],
            [900, 900, 710, 900],
            [1000, 800, 600, 800, 1000],
        ]
        self.assertEqual(oldest_wine(wines, 7), 710)


if __name__ == "__main__":
    unittest.main()
