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