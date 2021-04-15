import math
import Jaccard
import copy

# expand a string according to the whole rule set
def full_expand(s, rule_set):
    S_prime = set()
    for i in rule_set:
        if i[0] in s:
            if ' ' in i[1]:
                temp = i[1].split(' ')
                for j in temp:
                    S_prime.add(j)
            else:
                S_prime.add(i[1])
    S = set(s.split(' '))
    for i in S:
        S_prime.add(i)
    return S_prime

# similarity measure with full expansion
def full_expansion_sim_measure(s1, s2, rule_set):
    temp1 = full_expand(s1, rule_set)
    temp2 = full_expand(s2, rule_set)
    result = Jaccard.jaccard_similarity(temp1, temp2)
    return result

# signature generate in prefix_filter scheme
def prefix_signatures_gen(s, theta):
    result = set()
    temp = sorted(s)
    threshold = math.ceil((1-theta) * len(temp))
    for i in range(threshold):
        result.add(temp[i])
    return result

# extend prefix_signature_gen
def SN_signatures_gen(s, theta, rule_set):
    result = set()
    for i in rule_set:
        R_i = []
        R_i.append((i[0], i[1]))
        S_i = full_expand(s, R_i)
        Sig_S_i = prefix_signatures_gen(S_i, theta)
        result = result | Sig_S_i
    return result
        
# SN_join with 2 set of strings S and T
def SN_join(S, T, rule_set, theta, sim_measure):
    # filtering
    temp_S = copy.deepcopy(S)
    temp_T = copy.deepcopy(T)
    for i in range(len(S)):
        temp_S[i] = SN_signatures_gen(S[i], theta, rule_set)
    for i in range(len(T)):
        temp_T[i] = SN_signatures_gen(T[i], theta, rule_set)
    
    overlap = []
    for i in range(len(S)):
        for j in range(len(T)):
            if len(temp_S[i] & temp_T[j]) != 0:
                overlap.append((i, j))
    # verification
    result = []
    for i in overlap:
        if sim_measure(S[i[0]], T[i[1]], rule_set) >= theta: 
            result.append((S[i[0]], T[i[1]]))
    return result

