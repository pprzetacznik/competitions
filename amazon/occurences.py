import unittest


def lengthEachScene(inputList):
    first_occurences = {}
    for i in range(len(inputList)):
        if not inputList[i] in first_occurences:
            first_occurences[inputList[i]] = i + 1
    stack = []
    for i in range(len(inputList)):
        stack += [1]
        if first_occurences[inputList[i]] < i:
            difference = i + 1 - first_occurences[inputList[i]]
            count = 0
            while count <= difference:
                count += stack.pop()
            stack.append(count)
        print(stack)
    return stack


class TestWordCount(unittest.TestCase):
    def test_word_count1(self):
        self.assertListEqual(lengthEachScene(["a", "b", "c"]), [1, 1, 1])

    def test_word_count2(self):
        self.assertListEqual(lengthEachScene(["a", "b", "c", "a"]), [4])


if __name__ == "__main__":
    unittest.main()
