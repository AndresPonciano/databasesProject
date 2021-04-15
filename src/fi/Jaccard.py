def jaccard_similarity(set_1, set_2):
    inter = set_1.intersection(set_2)
    uni = set_1.union(set_2)

    return len(inter)/len(uni)

def Jaccard_sim_measure(s1, s2, rule_set):
    temp1 = set(s1.split(' '))
    temp2 = set(s2.split(' '))

    return jaccard_similarity(temp1, temp2)
