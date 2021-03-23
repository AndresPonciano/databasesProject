def rule_gain(rule, string1, string2, all_rules):
    rhs = set(rule[1].split(' '))
    set_1 = set(string1.split(' '))

    U = rhs.difference(set_1)

    if not U:
        return 0

    set_2 = set(string2.split(' '))

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



if __name__ == "__main__":

    q1 = 'Intl WH Conf 2012'
    t2 = 'Intl Wireless Health Conference 2012 UK'

    synonymPairs = {
        'WH': 'Wireless Health',
        'Intl': 'International',
        'Wireless Health': 'WH',
        'Conference': 'Conf',
        'UK': 'United Kingdom',
        'Conf': 'Conference',
    }

    rule = ('WH', 'Wireless Health')

    rule_gain1 = rule_gain(rule, q1, t2, synonymPairs)
