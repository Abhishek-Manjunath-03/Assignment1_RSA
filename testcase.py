import unittest

# Your logic gate functions and validation functions here
def AND_gate(a, b):
    return a and b

def OR_gate(a, b):
    return a or b

def NOT_gate(a):
    return not a

def XOR_gate(a, b):
    return a != b

def validate_gate(gate):
    valid_gates = ['AND', 'OR', 'NOT', 'XOR']
    return gate.upper() in valid_gates

def validate_input(inputs):
    return all(x in [0, 1] for x in inputs)

# Test cases for the Boolean Logic Simulator
class TestBooleanLogicSimulator(unittest.TestCase):

    def test_AND_gate(self):
        self.assertEqual(AND_gate(0, 0), 0)
        self.assertEqual(AND_gate(0, 1), 0)
        self.assertEqual(AND_gate(1, 0), 0)
        self.assertEqual(AND_gate(1, 1), 1)

    def test_OR_gate(self):
        self.assertEqual(OR_gate(0, 0), 0)
        self.assertEqual(OR_gate(0, 1), 1)
        self.assertEqual(OR_gate(1, 0), 1)
        self.assertEqual(OR_gate(1, 1), 1)

    def test_NOT_gate(self):
        self.assertEqual(NOT_gate(0), 1)
        self.assertEqual(NOT_gate(1), 0)

    def test_XOR_gate(self):
        self.assertEqual(XOR_gate(0, 0), 0)
        self.assertEqual(XOR_gate(0, 1), 1)
        self.assertEqual(XOR_gate(1, 0), 1)
        self.assertEqual(XOR_gate(1, 1), 0)

    def test_validate_gate(self):
        self.assertTrue(validate_gate('AND'))
        self.assertTrue(validate_gate('OR'))
        self.assertTrue(validate_gate('NOT'))
        self.assertTrue(validate_gate('XOR'))
        self.assertFalse(validate_gate('NAND'))
        self.assertFalse(validate_gate(''))

    def test_validate_input(self):
        self.assertTrue(validate_input([0, 1]))
        self.assertTrue(validate_input([1]))
        self.assertFalse(validate_input([0, 1, 2]))
        self.assertFalse(validate_input([2]))
        self.assertFalse(validate_input([1, -1]))

# Run the tests
if __name__ == '__main__':
    unittest.main()
