import unittest
from math import sin, pi


operations = {
    '+': (2, lambda x, y: x+y),
    '*': (2, lambda x, y: x*y),
    '-': (2, lambda x, y: x-y),
    '/': (2, lambda x, y: x/y),
    'sin': (1, lambda x: sin(x))
}


def rpn(instructions=[], stack=[]):
    if not instructions and len(stack) == 1:
        return stack[0]
    if not instructions:
        raise Exception("no more instructions")
    instruction = instructions[0]
    if instruction not in operations:
        return rpn(instructions[1:], stack + [instruction])
    else:
        argv, operation = operations[instruction]
        result = operation(*stack[-argv:])
        return rpn(instructions[1:], stack[:-argv] + [result])


class TestReversePolishNotation(unittest.TestCase):

    def test_empty(self):
        with self.assertRaises(Exception) as context:
            rpn([])
        self.assertTrue("no more instructions" in str(context.exception))

    def test_operations(self):
        self.assertEqual(rpn([1, 2, '+']), 3)
        self.assertEqual(rpn([1, 2, '+', 4, '*']), 12)
        self.assertEqual(rpn([13, 1, 2, '+', 4, '*', '-']), 1)

    def test_sin(self):
        self.assertEqual(rpn([0, 'sin']), 0)
        self.assertAlmostEqual(rpn([pi / 3, 'sin']), 0.86, delta=0.01)
        self.assertAlmostEqual(rpn([pi / 2, 'sin']), 1)


if __name__ == '__main__':
    unittest.main()
