# from Jaccard import jaccard_similarity

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
    print('in find initial')

    cset = set()
    for rule in all_rules:
        rg = rule_gain(all_rules[rule], string1, string2, all_rules)
        print('for rule: ', rule, 'RG IS: ', rg)
        if rg > 0 and rule in string1:
            cset.add(rule)

    return cset

def find_candidate_rule_set(string1, string2, all_rules):
    #change these to dictionaries??
    cset_1 = find_initial_candidates(string1, string2, all_rules)
    cset_2 = find_initial_candidates(string2, string1, all_rules)

    print('CANDIDATES1: ', cset_1)
    print('CANDIDATES2: ', cset_2)

    return cset_1, cset_2

def expands(string1, string2, cset_1, cset_2):
    print('expanding')
    set_1 = set(string1.split(' '))
    set_2 = set(string2.split(' '))

    set_1_prime = set_1
    set_2_prime = set_2

    i = 0
    # while len(cset_1.union(cset_2)) != 0:
    while i != 10:
        print(i)
        i += 1

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
