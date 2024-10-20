# Boolean Logic Simulator (CLI Version)

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

# CLI Interface
def cli_interface():
    print("Welcome to Boolean Logic Simulator")
    
    # Input gate type
    gate = input("Enter gate type (AND, OR, NOT, XOR): ").upper()
    
    # Validate gate type
    if not validate_gate(gate):
        print("Invalid gate type. Try again.")
        return
    
    # Input the values for the logic gate
    if gate == "NOT":
        a = int(input("Enter input (0 or 1): "))
        if not validate_input([a]):
            print("Invalid input. Try again.")
            return
        print(f"NOT {a} = {int(NOT_gate(a))}")
    else:
        a = int(input("Enter input 1 (0 or 1): "))
        b = int(input("Enter input 2 (0 or 1): "))
        if not validate_input([a, b]):
            print("Invalid inputs. Try again.")
            return
        
        # Perform the selected gate operation
        if gate == "AND":
            print(f"{a} AND {b} = {int(AND_gate(a, b))}")
        elif gate == "OR":
            print(f"{a} OR {b} = {int(OR_gate(a, b))}")
        elif gate == "XOR":
            print(f"{a} XOR {b} = {int(XOR_gate(a, b))}")

# Run the CLI interface
if __name__ == '__main__':
    cli_interface()
