from Jaccard import jaccard_similarity

def get_applicable_rules(set_1, all_rules):
    #for applicable rules
    rules_prime = set()
    # for lhs in all_rules:
    #     for temp_str in set_1:
    #         if lhs in temp_str:
    #             rules_prime = rules_prime.union(set(all_rules[lhs]))

    # return rules_prime

    for rule in all_rules:
        for temp_str in set_1:
            if rule[0] in temp_str:
                rules_prime.add(rule[1])

    return rules_prime

def full_expansion(string1, string2, all_rules):
    print('hey')
    set_1 = set(string1.split(';'))
    set_2 = set(string2.split(';'))


    rules_prime_1 = get_applicable_rules(set_1, all_rules)
    rules_prime_2 = get_applicable_rules(set_2, all_rules)
    # print(rules_prime_1)
    # print(rules_prime_2)

    set_1_prime = set_1.union(rules_prime_1)
    set_2_prime = set_2.union(rules_prime_2)
    print(set_1_prime)
    print(set_2_prime)

    return jaccard_similarity(set_1_prime, set_2_prime)


if __name__ == "__main__":

    # s1 = 'Proceedings of the VLDB Endowment;2012;38th;International Conference on Very Large Databases;Turkey'
    # s2 = 'PVLDB;2012;Turkey'

    # synonymPairs = {
    #     'PVLDB': ['International Conference on Very Large Databases', 'Proceedings of the VLDB Endowment'],
    # }

    s1 = 'University of Washington;1705 NE Pacific St Seattle, WA 98195'
    s2 = 'UW'
    
    synonymPairs = [('UW', 'University of Washington'), ('UW', '1705 NE Pacific St Seattle, WA 98195'), ('UW', 'University of Waterloo')]
    # synonymPairs = {
    #     'UW': ['University of Washington', '1705 NE Pacific St Seattle, WA 98195', 'University of Waterloo']
    # }

    idk = full_expansion(s1, s2, synonymPairs)
    print(idk)
    
