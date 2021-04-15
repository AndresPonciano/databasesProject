import math
import Jaccard
import copy
import FE_sim

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
        S_i = FE_sim.full_expand(s, R_i)
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

