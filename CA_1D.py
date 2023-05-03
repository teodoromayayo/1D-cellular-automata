import numpy as np
import matplotlib.pyplot as plt

def cellular_automata_deterministic(iterations, size, rule, type, generation_probability):

    # Convert the decimal rule to binary
    rule = np.binary_repr(rule, width=8)

    # Create the rule table, with the 8 possible rules
    rule_table = {'111': int(rule[0]), '110': int(rule[1]), '101': int(rule[2]),
                  '100': int(rule[3]), '011': int(rule[4]), '010': int(rule[5]),
                  '001': int(rule[6]), '000': int(rule[7])}

    # Create an array to store the cellular automaton
    cellular_automata = np.zeros((iterations, size), dtype=int)
    initial_condition = cellular_automata[0]

    # Standard initial conditions
    if type == 'standard':
        initial_condition[int(size/2)] = 1

    # Random initial conditions
    else:
        random_indices = np.random.choice(size, size=int(generation_probability*size), replace=False)
        initial_condition[random_indices] = 1

    cellular_automata[0] = initial_condition

    # Iterate for the desired number of iterations
    for i in range(1, iterations):
        for j in range(size):
            # Determine the 3 cells used for the rule
            if j == 0:
                cells = ''.join([str(int(cell)) for cell in [initial_condition[-1], initial_condition[j], initial_condition[j + 1]]])
            elif j == size - 1:
                cells = ''.join([str(int(cell)) for cell in [initial_condition[j - 1], initial_condition[j], initial_condition[0]]])
            else:
                cells = ''.join([str(int(cell)) for cell in [initial_condition[j - 1], initial_condition[j], initial_condition[j + 1]]])

            # Apply the rule
            new_value = rule_table[cells]

            # Update the cellular automaton
            cellular_automata[i][j] = new_value

        initial_condition = cellular_automata[i]

    return cellular_automata

def cellular_automata_stochatic(iterations, size, rule, survival_prob, type, generation_probability):

    # Convert the decimal rule to binary
    rule = np.binary_repr(rule, width=8)

    # Create the rule table, with the 8 possible rules
    rule_table = {'111': int(rule[0]), '110': int(rule[1]), '101': int(rule[2]),
                  '100': int(rule[3]), '011': int(rule[4]), '010': int(rule[5]),
                  '001': int(rule[6]), '000': int(rule[7])}

    # Create an array to store the cellular automaton
    cellular_automata = np.zeros((iterations, size), dtype=int)
    initial_condition = cellular_automata[0]

    # Standard initial conditions
    if type == 'standard':
        initial_condition[size-1] = 1

    # Random initial conditions
    else:
        random_indices = np.random.choice(size, size=int(generation_probability*size), replace=False)
        initial_condition[random_indices] = 1

    cellular_automata[0] = initial_condition

    # Iterate for the desired number of iterations
    for i in range(1, iterations):
        for j in range(size):
            # Determine the 3 cells used for the rule
            if j == 0:
                cells = ''.join([str(int(cell)) for cell in [initial_condition[-1], initial_condition[j], initial_condition[j + 1]]])
            elif j == size - 1:
                cells = ''.join([str(int(cell)) for cell in [initial_condition[j - 1], initial_condition[j], initial_condition[0]]])
            else:
                cells = ''.join([str(int(cell)) for cell in [initial_condition[j - 1], initial_condition[j], initial_condition[j + 1]]])

            # Apply the rule
            new_value = rule_table[cells]

            # Apply stochasticity
            if new_value == 1 and np.random.rand() > survival_prob:
                new_value = 0

            # Update the cellular automaton
            cellular_automata[i][j] = new_value

        initial_condition = cellular_automata[i]

    return cellular_automata

def plot_cellular_automata(cellular_automata):

    # Plot of the cellular automata generated
    plt.imshow(cellular_automata, cmap='binary')
    plt.axis('off')
    plt.show()
