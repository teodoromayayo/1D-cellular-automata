def dec_to_bin(num):
    return format(num, '08b')

def bin_to_dec(binary_str):
    return int(binary_str, 2)

def calculate_langton_parameter(rule_number):
    # Get the binary representation of the rule number
    rule_binary_representation = dec_to_bin(rule_number)

    # Convert the binary string to a list of integers
    binary_list = [int(bit) for bit in rule_binary_representation]

    # Calculate the Langton parameter (ratio of 1s to total cells in the rule's neighborhood)
    return sum(binary_list) / len(binary_list)

def complement(binary_str):
    inverted_str = binary_str[::-1] # reverse the string
    complement_list = []
    for i in range(len(inverted_str)):
        if inverted_str[i] == '0':
            complement_list.append('1')
        else:
            complement_list.append('0')
    return ''.join(complement_list) # join the list and reverse the result

def reflect(binary_str):
    binary_list = list(binary_str)
    binary_list[1], binary_list[4] = binary_list[4], binary_list[1]
    binary_list[3], binary_list[6] = binary_list[6], binary_list[3]
    return ''.join(binary_list)

def reflect_and_complement(binary_str):
    return complement(reflect(binary_str))

def main():
    inequivalent_rules = []
    langton_parameters = {}
    
    # Calculate Langton's ant parameters for each rule
    for rule in range(256):
        rule_binary = format(rule, '08b')
        langton_parameters[rule] = calculate_langton_parameter(rule)
        
    # Check each rule and its transformations for smallest Langton's ant parameter
    for rule in range(256):
        rule_binary = format(rule, '08b')
        rule_inverted = complement(rule_binary)
        rule_reflected = reflect(rule_binary)
        rule_reflected_inverted = reflect_and_complement(rule_binary)
        
        rules = [rule, bin_to_dec(rule_inverted), bin_to_dec(rule_reflected), bin_to_dec(rule_reflected_inverted)]
        min_parameter = min(langton_parameters[rule] for rule in rules)
        min_rules = [rule for rule in rules if langton_parameters[rule if isinstance(rule, int) else format(rule, '08b')] == min_parameter]
        min_rule = min(min_rules)
        
        if min_rule not in inequivalent_rules:
            inequivalent_rules.append(min_rule)
    print(f'The {len(inequivalent_rules)} inequivalent rules are: {sorted(inequivalent_rules)}')
    return sorted(inequivalent_rules)


if __name__ == "__main__":
    main()
