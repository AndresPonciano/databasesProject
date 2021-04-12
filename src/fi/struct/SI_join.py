import SN_join

def SI_join():
    pass

if __name__ == "__main__":
# for SN_join testing
    # synonymPairs = {
    #         'WH': 'Wireless Health',
    #         'Intl': 'International',
    #         'Wireless Health': 'WH',
    #         'Conference': 'Conf',
    #         'UK': 'United Kingdom',
    #         'Conf': 'Conference',
    #     }

    # q1 = 'Intl WH Conf 2012'

    # S = ['Computational Complexity Conference', 'International Symposium on Fundamentals of Computation Theory']
    # T = ['IEEE Symposium on Foundations of Computer Science', 'International Colloquium on Automata, Languages and Programming']
    # print(full_expand(q1, synonymPairs))
    # print(SN_signatures_gen(q1, 0.5, synonymPairs))
    # print(full_expansion_sim_measure(S[1], T[0], synonymPairs))
    # print(full_expansion_sim_measure(S[1], T[1], synonymPairs))
    # print(SN_join(S, T, synonymPairs, 0.2, full_expansion_sim_measure))

# for SI_join testing
    rule_set_2 = {
        'Intl': 'International',
        'Conf': 'Conference',
        'VLDB': 'Very Large Data Bases',
        'Very Large Data Bases': 'VLDB',
    }

    q1 = '2013 ACM Intl Conf on Management of Data USA'
    q2 = 'Very Large Data Bases Conf'
    q3 = 'VLDB Conf'
    q4 = 'ICDE 2013'

    print(SN_join.SN_signatures_gen(q1, 0.8, rule_set_2))
