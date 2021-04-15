from SE_sim import find_candidate_rule_set, expands
from FE_sim import full_expansion_sim_measure
from Jaccard import jaccard_similarity

if __name__ == "__main__":
    s1 = "Proceedings of the VLDB Endowment 2012 38th International Conference on Very Large Databases Turkey"
    s2 = "PVLDB 2012 Turkey"

    synonym_pairs = [('PVLDB', 'Proceedings of the VLDB Endowment'), ('PVLDB', 'International Conference on Very Large Databases')]

    print('For strings: ')
    print(s1)
    print(s2)
    print('and rules: ')
    print(synonym_pairs)
    cset_1, cset_2 = find_candidate_rule_set(s1, s2, synonym_pairs)
    # print('hi', idk1, idk2)
    theta = expands(s1, s2, cset_1, cset_2, synonym_pairs)
    print('SE:', theta)
    val2 = full_expansion_sim_measure(s1, s2, synonym_pairs)
    print('Full', val2)
    val3 = jaccard_similarity(set(s1.split(';')), set(s2.split(';')))
    print('Jaccard', val3)

    s1 = 'University of Washington 1705 NE Pacific St Seattle, WA 98195'
    s2 = 'UW'

    synonym_pairs = [('UW', 'University of Washington'), ('UW', '1705 NE Pacific St Seattle, WA 98195'), ('UW', 'University of Waterloo')]
    
    print('')
    print('For strings: ')
    print(s1)
    print(s2)
    print('and rules: ')
    print(synonym_pairs)
    
    cset_1, cset_2 = find_candidate_rule_set(s1, s2, synonym_pairs)
    # print('hi', idk1, idk2)
    theta = expands(s1, s2, cset_1, cset_2, synonym_pairs)
    print('SE:', theta)
    val2 = full_expansion_sim_measure(s1, s2, synonym_pairs)
    print('Full', val2)
    val3 = jaccard_similarity(set(s1.split(';')), set(s2.split(';')))
    print('Jaccard', val3)

    s1 = 'P93214'
    s2 = '14339_SOLL 14-3-3 protein 9'

    synonym_pairs = [('P93214', '14339_SOLL'), ('P93214', '14-3-3 protein 9'), ('14339_SOLL', 'UPI0000124DEC')]
    
    print('')
    print('For strings: ')
    print(s1)
    print(s2)
    print('and rules: ')
    print(synonym_pairs)
    
    cset_1, cset_2 = find_candidate_rule_set(s1, s2, synonym_pairs)
    # print('hi', idk1, idk2)
    theta = expands(s1, s2, cset_1, cset_2, synonym_pairs)
    print('SE:', theta)
    val2 = full_expansion_sim_measure(s1, s2, synonym_pairs)
    print('Full', val2)
    val3 = jaccard_similarity(set(s1.split(';')), set(s2.split(';')))
    print('Jaccard', val3)