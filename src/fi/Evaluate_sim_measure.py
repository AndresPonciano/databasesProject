import SE_sim, FE_sim, Jaccard 

def Precision(TP, FP):
    return TP/float((TP + FP))

def Recall(TP, FN):
    return TP/float((TP + FN))

def F_measure(P, R):
    if P + R != 0:
        return (2 * P * R)/float((P + R))
    else:
        return 0
def Quality_of_Measures(S, T, sim_measure, theta, rule_set, validation):
    TP = 0
    TN = 0
    FP = 0
    FN = 0

    for s in S:
        for t in T:
            if sim_measure(s, t, rule_set) >= theta and (s, t) in validation:
                TP += 1
            elif sim_measure(s, t, rule_set) >= theta and (s, t) not in validation:
                FP += 1
            elif sim_measure(s, t, rule_set) < theta and (s, t) in validation:
                FN += 1
            elif sim_measure(s, t, rule_set) < theta and (s, t) not in validation:
                TN += 1
    
    # print(TP, TN, FP, FN)
    precision = Precision(TP, FP)
    recall = Recall(TP, FN)
    f_measure = F_measure(precision, recall)

    print('Theta:', theta)
    print('Precision: ', precision)
    print('Recall: ', recall)
    print('F_measure: ', f_measure)

if __name__ == "__main__":

# Figure 10
    s1 = "Proceedings of the VLDB Endowment 2012 38th International Conference on Very Large Databases Turkey"
    s2 = "PVLDB 2012 Turkey"

    rule_set = [('PVLDB', 'Proceedings of the VLDB Endowment'), ('PVLDB', 'International Conference on Very Large Databases')]

    print('Strings: ')
    print(s1)
    print(s2)
    print('Rules_set: ')
    print(rule_set)

    print('Jaccard: ', Jaccard.Jaccard_sim_measure(s1, s2, rule_set))
    print('Full: ', FE_sim.full_expansion_sim_measure(s1, s2, rule_set))
    print('SE:', SE_sim.SE_sim_measure(s1, s2, rule_set))

    s1 = 'University of Washington 1705 NE Pacific St Seattle, WA 98195'
    s2 = 'UW'

    rule_set = [('UW', 'University of Washington'), ('UW', '1705 NE Pacific St Seattle, WA 98195'), ('UW', 'University of Waterloo')]
    
    print('')
    print('Strings: ')
    print(s1)
    print(s2)
    print('Rules_set: ')
    print(rule_set)

    print('Jaccard: ', Jaccard.Jaccard_sim_measure(s1, s2, rule_set))
    print('Full: ', FE_sim.full_expansion_sim_measure(s1, s2, rule_set))
    print('SE:', SE_sim.SE_sim_measure(s1, s2, rule_set))

    s1 = 'P93214'
    s2 = '14339_SOLL 14-3-3 protein 9'

    rule_set = [('P93214', '14339_SOLL'), ('P93214', '14-3-3 protein 9'), ('14339_SOLL', 'UPI0000124DEC')]
    
    print('')
    print('Strings: ')
    print(s1)
    print(s2)
    print('Rules_set: ')
    print(rule_set)

    print('Jaccard: ', Jaccard.Jaccard_sim_measure(s1, s2, rule_set))
    print('Full: ', FE_sim.full_expansion_sim_measure(s1, s2, rule_set))
    print('SE:', SE_sim.SE_sim_measure(s1, s2, rule_set))

# Figure 9
    Tq = open("src/fi/QueryTable.txt", "r")
    Tt = open("src/fi/TargetTable.txt", "r")
    synonym_text = open("src/fi/synonyms.txt", "r")
    Tq = [line.strip() for line in Tq]
    Tt = [line.strip() for line in Tt]
    synonym_text = [line.strip() for line in synonym_text]
    temp = []
    matching_rec = []
    for i in range(0, len(Tt), 2):
        temp.append(Tt[i])
    for i in range(len(Tq)):
        matching_rec.append((Tq[i], temp[i]))
    lhs = []
    rhs = []
    rule_set = []    
    for i in synonym_text:
        i = i.split(': ')
        lhs.append(i[0])
        rhs.append(i[1])
        rule_set.append((i[0], i[1]))
    # print(rule_set)
    print('Jaccard similarity')
    Quality_of_Measures(Tq, Tt, Jaccard.Jaccard_sim_measure, 0.5, rule_set, matching_rec)
    Quality_of_Measures(Tq, Tt, Jaccard.Jaccard_sim_measure, 0.6, rule_set, matching_rec)
    Quality_of_Measures(Tq, Tt, Jaccard.Jaccard_sim_measure, 0.7, rule_set, matching_rec)
    Quality_of_Measures(Tq, Tt, Jaccard.Jaccard_sim_measure, 0.8, rule_set, matching_rec)
    Quality_of_Measures(Tq, Tt, Jaccard.Jaccard_sim_measure, 0.9, rule_set, matching_rec)

    print('Full expansion similarity')
    Quality_of_Measures(Tq, Tt, FE_sim.full_expansion_sim_measure, 0.5, rule_set, matching_rec)
    Quality_of_Measures(Tq, Tt, FE_sim.full_expansion_sim_measure, 0.6, rule_set, matching_rec)
    Quality_of_Measures(Tq, Tt, FE_sim.full_expansion_sim_measure, 0.7, rule_set, matching_rec)
    Quality_of_Measures(Tq, Tt, FE_sim.full_expansion_sim_measure, 0.8, rule_set, matching_rec)
    Quality_of_Measures(Tq, Tt, FE_sim.full_expansion_sim_measure, 0.9, rule_set, matching_rec)

    print('Selective expansion similarity')
    Quality_of_Measures(Tq, Tt, SE_sim.SE_sim_measure, 0.5, rule_set, matching_rec)
    Quality_of_Measures(Tq, Tt, SE_sim.SE_sim_measure, 0.6, rule_set, matching_rec)
    Quality_of_Measures(Tq, Tt, SE_sim.SE_sim_measure, 0.7, rule_set, matching_rec)
    Quality_of_Measures(Tq, Tt, SE_sim.SE_sim_measure, 0.8, rule_set, matching_rec)
    Quality_of_Measures(Tq, Tt, SE_sim.SE_sim_measure, 0.9, rule_set, matching_rec)

