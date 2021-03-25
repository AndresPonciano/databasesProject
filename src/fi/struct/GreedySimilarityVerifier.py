from Jaccard import jaccard_similarity

def rule_gain(rhs, string1, string2, all_rules):
    rhs = set(rhs)
    set_1 = set(string1.split(' '))

    U = rhs.difference(set_1)

    if not U:
        return 0

    set_2 = set(string2.split(' '))

    #finding applicable rulles of set_2
    rules_prime = set()
    for lhs in all_rules:
        for temp_str in set_2:
            if lhs in temp_str:
                rules_prime.add(lhs)
        
    set_2_prime = set_2.union(rules_prime)

    G = (rhs.intersection(set_2_prime)).difference(set_1)
    
    # print('g is: ', G)
    # print('u is: ', U)

    # print(len(G), len(U), len(G)/len(U))

    return len(G)/len(U)

def find_initial_candidates(string1, string2, all_rules):
    # print('in find initial')

    cset = dict()
    for rule in all_rules:
        rg = rule_gain(all_rules[rule], string1, string2, all_rules)
        # print('for rule: ', rule, 'RG IS: ', rg)
        if rg > 0 and rule in string1:
            cset[rule] = all_rules[rule]
            # cset.add(rule)

    return cset

def find_candidate_rule_set(string1, string2, all_rules):
    #change these to dictionaries??
    cset_1 = find_initial_candidates(string1, string2, all_rules)
    cset_2 = find_initial_candidates(string2, string1, all_rules)

    #THIS SHOULD BE THE BEGINNING OF A WHILE TRUE LOOP############################
    set_1_prime = set(string1.split(' '))
    set_2_prime = set(string1.split(' '))
    for rule in cset_1:
        set_1_prime = set_1_prime.union(set(cset_1[rule]))

    for rule in cset_2:
        set_2_prime = set_2_prime.union(set(cset_2[rule]))

    theta = jaccard_similarity(set_1_prime, set_2_prime)

    # print('theta is: ', theta)

    # print('merging dictionaries: ')
    temp = {**cset_1, **cset_2}
    # print(temp)

    for rule in temp:
        # print(rule)
        rg_1 = rule_gain(temp[rule], string1, string2, all_rules)
        rg_2 = rule_gain(temp[rule], string2, string1, all_rules)
        # print('hey', rg_1, rg_2)
        theta_val = theta / ( 1 + theta )
        # print(theta_val)

        if rg_1 < theta_val and rule in cset_1.keys():
            del cset_1[rule]

        if rg_2 < theta_val and rule in cset_2.keys():
            del cset_2[rule]

    temp_cset_1 = dict(cset_1)
    temp_cset_2 = dict(cset_2)




    print('CANDIDATES1: ', cset_1)
    print('CANDIDATES2: ', cset_2)


    #THIS SHOULD BE THE END OF THE WHILE TRUE LOOP###############################

    return cset_1, cset_2

def find_gain_effective_rule(cset, string1, string2, all_rules):
    print('finding current most gain-effective rule')

    max_gain_rule = 0.0
    lhs, rhs = None, None
    for rule in cset:
        temp_gain = rule_gain(cset[rule], string1, string2, all_rules)
        if temp_gain > max_gain_rule:
            max_gain_rule = temp_gain
            lhs = rule
            rhs = cset[rule]

    return lhs, rhs, max_gain_rule

def expands(string1, string2, cset_1, cset_2, all_rules):
    print('expanding')
    set_1_prime = set(string1.split(' '))
    set_2_prime = set(string2.split(' '))


    i = 0
    # while len(cset_1.union(cset_2)) != 0:
    while i != 2:
        lhs1, rhs1, most_gain_1 = find_gain_effective_rule(cset_1, string1, string2, all_rules)
        lhs2, rhs2, most_gain_2 = find_gain_effective_rule(cset_2, string2, string1, all_rules)

        if most_gain_1 > 0:
            set_1_prime = set_1_prime.union(rhs1)

        if lhs1 in cset_1.keys():
            del cset_1[lhs1]

        if most_gain_2 > 0:
            set_2_prime = set_2_prime.union(rhs2)
        
        if lhs2 in cset_2.keys():
            del cset_2[lhs2]

        print(i)
        i += 1
    
    return jaccard_similarity(set_1_prime, set_2_prime)

if __name__ == "__main__":

    q1 = 'Intl WH Conf 2012'
    t2 = 'Intl Wireless Health Conference 2012 UK'

    synonymPairs = {
        'WH': ['Wireless Health'],
        'Intl': ['International'],
        'Wireless Health': ['WH'],
        'Conference': ['Conf'],
        'UK': ['United Kingdom'],
        'Conf': ['Conference'],
    }

    #this is how we would do a single rule?
    lhs = 'WH'
    rhs = ['Wireless Health']

    rule_gain1 = rule_gain(rhs, q1, t2, synonymPairs)
    # print(rule_gain1)
    idk1, idk2 = find_candidate_rule_set(q1, t2, synonymPairs)
