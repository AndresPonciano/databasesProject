def jaccard_similarity(set_1, set_2):
    inter = set_1.intersection(set_2)
    uni = set_1.union(set_2)

    return len(inter)/len(uni)
