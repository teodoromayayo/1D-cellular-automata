from CA_1D import cellular_automata, plot_cellular_automata

#----------------------Assigning values to variables----------------------------------

iterations = 4*256
size = 2*iterations+1
rule = 102
# Survival probability is equal to 1 if the cellular automata is deterministic
survival_prob = 1
# If a standard type is implemented, size should be bigger or equal to 2*iteration+1 becaus is coded for periodic boundarie and we would avoid collisions
type = 'standard'
# Is the probability of appearing living cells when considering random conditions in the initial array
generation_probability = 0.5

#-----------------------Implementation of the code------------------------------------

# Implememntation of the cellular automata and the measure of fractal dimension
CA = cellular_automata(iterations, size, rule, survival_prob, type, generation_probability)
plot_cellular_automata(CA)