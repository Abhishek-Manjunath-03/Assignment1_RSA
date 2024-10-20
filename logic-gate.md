# Functions for each logic gate
def AND_gate(a, b):
    return a and b

def OR_gate(a, b):
    return a or b

def NOT_gate(a):
    return not a

def XOR_gate(a, b):
    return a != b

# Validation functions
def validate_gate(gate):
    valid_gates = ['AND', 'OR', 'NOT', 'XOR']
    return gate.upper() in valid_gates

def validate_input(inputs):
    return all(x in [0, 1] for x in inputs)
