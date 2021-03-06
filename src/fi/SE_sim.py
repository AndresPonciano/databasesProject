from Jaccard import jaccard_similarity
from FE_sim import full_expand

def rule_gain(rhs, string1, string2, all_rules):
    temp = rhs.split(' ')
    rhs_set = set(temp)
    set_1 = set(string1.split(' '))

    U = rhs_set.difference(set_1)
    if not U:
        return 0

    set_2 = set(string2.split(' '))

    #finding applicable rulles of set_2
    rules_prime = full_expand(string2, all_rules)
        
    # set_2_prime
    for rule in rules_prime:
        set_2.add(rule)

    G = (rhs_set.intersection(set_2)).difference(set_1)

    return len(G)/len(U)

def find_initial_candidates(string1, string2, all_rules):
    cset = []
    for rule in all_rules:
        rg = rule_gain(rule[1], string1, string2, all_rules)
        # print('for rule: ', rule, 'RG IS: ', rg)
        if rg > 0 and rule[0] in string1:
            cset.append(rule)

    return cset

def find_candidate_rule_set(string1, string2, all_rules):
    #change these to dictionaries??
    cset_1 = find_initial_candidates(string1, string2, all_rules)
    cset_2 = find_initial_candidates(string2, string1, all_rules)

    # print('initial cand', cset_1)
    # print(cset_2)
    #THIS SHOULD BE THE BEGINNING OF A WHILE TRUE LOOP############################
    while True:
        set_1_prime = set(string1.split(' '))
        set_2_prime = set(string2.split(' '))
        for rule in cset_1:
            temp_set = rule[1].split(' ')
            set_1_prime = set_1_prime.union(temp_set)
            # set_1_prime = set_1_prime.union(set(cset_1[rule]))

        for rule in cset_2:
            temp_set = rule[1].split(' ')
            set_2_prime = set_2_prime.union(temp_set)
            # set_2_prime = set_2_prime.union(set(cset_2[rule]))

        theta = jaccard_similarity(set_1_prime, set_2_prime)

        # temp = {**cset_1, **cset_2}
        temp = cset_1 + cset_2

        for rule in temp:
            rg_1 = rule_gain(rule[1], string1, string2, all_rules)
            rg_2 = rule_gain(rule[1], string2, string1, all_rules)

            theta_val = theta / ( 1 + theta )

            if rg_1 < theta_val and rule in cset_1:
                cset_1.remove(rule)

            if rg_2 < theta_val and rule in cset_2:
                cset_2.remove(rule)

        temp_cset_1 = list(cset_1)
        temp_cset_2 = list(cset_2)

        # print('CANDIDATES1: ', cset_1)
        # print('CANDIDATES2: ', cset_2)

        jaccard_of_expanded = expands(string1, string2, temp_cset_1, temp_cset_2, all_rules)
        # print('returned from expands: ', jaccard_of_expanded)
        # print('after expands: ')
        # print(temp_cset_1)
        # print(temp_cset_2)
        if (not temp_cset_1 and not temp_cset_2) or (temp_cset_1 == cset_1 and temp_cset_2 == cset_2):
            break

        cset_1 = temp_cset_1.copy()
        cset_2 = temp_cset_2.copy()
    #THIS SHOULD BE THE END OF THE WHILE TRUE LOOP###############################

    # print('before returning from find c_set', set_1_prime)
    return cset_1, cset_2

def find_gain_effective_rule(cset, string1, string2, all_rules):
    # print('finding current most gain-effective rule')

    max_gain_rule = 0.0
    lhs, rhs = None, None
    for rule in cset:
        temp_gain = rule_gain(rule[1], string1, string2, all_rules)
        if temp_gain > max_gain_rule:
            max_gain_rule = temp_gain
            lhs = rule[0]
            rhs = rule[1]

    return lhs, rhs, max_gain_rule

def expands(string1, string2, cset_1, cset_2, all_rules):
    #change these to expanded sets??
    set_1_prime = set(string1.split(' '))
    set_2_prime = set(string2.split(' '))

    i = 0
    # while {**cset_1, **cset_2}:
    while cset_1 + cset_2:
    # while i != 2:
        lhs1, rhs1, most_gain_1 = find_gain_effective_rule(cset_1, string1, string2, all_rules)
        lhs2, rhs2, most_gain_2 = find_gain_effective_rule(cset_2, string2, string1, all_rules)

        if most_gain_1 > 0:
            temp_set = rhs1.split(' ')
            temp_set = set(temp_set)
            set_1_prime = set_1_prime.union(temp_set)

        try:
            cset_1.remove((lhs1, rhs1))
        except:
            pass

        if most_gain_2 > 0:
            temp_set = rhs2.split(' ')
            temp_set = set(temp_set)
            set_2_prime = set_2_prime.union(temp_set)

        try:
            cset_2.remove((lhs2, rhs2))
        except:
            pass

        i += 1

    return jaccard_similarity(set_1_prime, set_2_prime)

def SE_sim_measure(s1, s2, all_rules):
    cset_1, cset_2 = find_candidate_rule_set(s1, s2, all_rules)
    theta = expands(s1, s2, cset_1, cset_2, all_rules)
    return theta