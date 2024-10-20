# Function to simulate logic gates
def logic_gate_simulator(gate_type, *inputs):
    if gate_type.upper() == "AND":
        result = all(inputs)
    elif gate_type.upper() == "OR":
        result = any(inputs)
    elif gate_type.upper() == "NOT":
        if len(inputs) != 1:
            return "NOT gate only accepts one input."
        result = not inputs[0]
    elif gate_type.upper() == "XOR":
        if len(inputs) != 2:
            return "XOR gate only accepts two inputs."
        result = inputs[0] ^ inputs[1]
    else:
        return "Invalid gate type."
    
    return int(result)  # Return as 0 or 1 (boolean as integer)