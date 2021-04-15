import SE_sim, FE_sim
import SN_join, SI_join

if __name__ == "__main__":
    rule_set = [
            ('WH', 'Wireless Health'),
            ('Intl', 'International'),
            ('Wireless Health', 'WH'),
            ('Conference', 'Conf'),
            ('UK', 'United Kingdom'),
            ('Conf', 'Conference'),
            ('Intl', 'International'),
            ('Conf', 'Conference'),
            ('VLDB', 'Very Large Data Bases'),
            ('Very Large Data Bases', 'VLDB'),
    ]

    q1 = '2013 ACM Intl Conf on Management of Data USA'
    q2 = 'Very Large Data Bases Conf'
    q3 = 'VLDB Conf'
    q4 = 'ICDE 2013'
    q5 = 'Computational Complexity Conference'
    q6 = 'International Symposium on Fundamentals of Computation Theory'
    q7 = 'IEEE Symposium on Foundations of Computer Science'
    q8 = 'International Colloquium on Automata, Languages and Programming'

    S = [q1, q2, q3, q4]
    T = [q3, q4, q1, q2]

# for SN_join testing
    # print(FE_sim.full_expand(q1, rule_set))
    # print(SN_join.SN_signatures_gen(q1, 0.5, rule_set))
    # print(FE_sim.full_expansion_sim_measure(S[1], T[0], rule_set))
    # print(FE_sim.full_expansion_sim_measure(S[1], T[1], rule_set))
    print(SN_join.SN_join(S, T, rule_set, 0.8, FE_sim.full_expansion_sim_measure))
    print(SN_join.SN_join(S, T, rule_set, 0.8, SE_sim.SE_sim_measure))

# for SI_join testing
    # print(SI_join.I_list(S, rule_set, 0.7))
    # print(SN_join.SN_signatures_gen(q4, 0.7, rule_set))
    # print(FE_sim.full_expand(q3, rule_set))
    # print(SI_join.SI_index(S, rule_set, 0.8))
    # print(SI_join.SI_index(T, rule_set, 0.8))
    print(SI_join.SI_join(S, T, 0.8, rule_set, FE_sim.full_expansion_sim_measure))
    print(SI_join.SI_join(S, T, 0.8, rule_set, SE_sim.SE_sim_measure))