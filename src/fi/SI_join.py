import SN_join
import copy

class Fence_Entry:
    def __init__(self, s, rule_set):
        self.u = len(s.split(' '))
        self.v = len(SN_join.full_expand(s, rule_set))
        self.P = []

class Leaf_Entry:
    def __init__(self, s, rule_set):
        self.t = len(SN_join.full_expand(s, rule_set))
        self.P = set()

def I_list(S, rule_set, theta):
    token_l = {}
    temp = copy.deepcopy(S)
    for i in range(len(temp)):
        temp[i] = SN_join.SN_signatures_gen(temp[i], theta, rule_set)
        for j in temp[i]:
            if j in token_l:
                token_l[j].add(i)
            else:
                token_l[j] = {i}
    return token_l
    
def SI_index(S, rule_set, theta):
    # String ID, L, F table
    L = []
    F = []
    L_F = []
    sID_L_F = []
    temp = copy.deepcopy(S)
    for i in temp:
        i = i.split(' ')
        L.append(len(i))
    temp = copy.deepcopy(S)
    for i in temp:
        i = SN_join.full_expand(i, rule_set)
        F.append(len(i))
    for i in range(len(L)):
        L_F.append((L[i], F[i]))
        sID_L_F.append((i, L[i], F[i]))

    # root entry
    temp = copy.deepcopy(S)
    all_Fence_Entry = []
    root = []
    for i in S:
        all_Fence_Entry.append(Fence_Entry(i, rule_set))
    all_Fence_Entry = sorted(all_Fence_Entry, key=lambda x: x.u)
    root.append(all_Fence_Entry[0])
    for i in range(len(all_Fence_Entry)):
        for j in range(len(root)):
            if all_Fence_Entry[i].u == root[j].u:
                if all_Fence_Entry[i].v <= root[j].v:
                    continue
                else:
                    root[j] = all_Fence_Entry[i]
            elif j == len(root) - 1 and all_Fence_Entry[i].u != root[j].u:
                root.append(all_Fence_Entry[i])

    # fence entry
    for i in root:
        for j in sID_L_F:
            if j[1] == i.u:
                i.P.append(Leaf_Entry(S[j[0]], rule_set))
        i.P = sorted(i.P, key=lambda x: x.t)
    
    # for i in root:
    #     for j in i.P:
    #         print(i.u, i.v, j.t)

    # leaf entry
    for i in sID_L_F:
        for j in root:
            if j.u == i[1]:
                for k in j.P:
                    if k.t == i[2]:
                        k.P = SN_join.SN_signatures_gen(S[i[0]], theta, rule_set)
    for i in root:
        for j in i.P:
                print(i.u, i.v, j.t, j.P)

    return root

def SI_join(S, T, theta, rule_set, sim_measure):
    # filtering
    SI_s = SI_index(S, rule_set, theta)
    SI_t = SI_index(T, rule_set, theta)
    C = set()
    for Fs in SI_s:
        for Ft in SI_t:
            if min(Fs.v, Ft.v) >= theta*max(Fs.u, Ft.u):
                for Es in Fs.P:
                    for Et in Ft.P:
                        if min(Es.t, Et.t) >= theta*max(Fs.u, Ft.u):
                            for g in (Es.P and Et.P):
                                Ls = I_list(S, rule_set, theta)[g]
                                Ls = frozenset(Ls)
                                Lt = I_list(T, rule_set, theta)[g]
                                Lt = frozenset(Lt)
                                C = C | {(Ls, Lt)}

    # verification
    result = set()
    for i in C:
        for j in i[0]:
            for k in i[1]:
                if sim_measure(S[j], T[k], rule_set) >= theta: 
                    result.add((S[j], T[k]))
    return result
    
if __name__ == "__main__":
# for SN_join testing
    # synonymPairs = [
    #         ('WH', 'Wireless Health'),
    #         ('Intl', 'International'),
    #         ('Wireless Health', 'WH'),
    #         ('Conference', 'Conf'),
    #         ('UK', 'United Kingdom'),
    #         ('Conf', 'Conference'),
    # ]

    # q1 = 'Intl WH Conf 2012'

    # S = ['Computational Complexity Conference', 'International Symposium on Fundamentals of Computation Theory']
    # T = ['IEEE Symposium on Foundations of Computer Science', 'International Colloquium on Automata, Languages and Programming']
    # print(SN_join.full_expand(q1, synonymPairs))
    # print(SN_join.SN_signatures_gen(q1, 0.5, synonymPairs))
    # print(SN_join.full_expansion_sim_measure(S[1], T[0], synonymPairs))
    # print(SN_join.full_expansion_sim_measure(S[1], T[1], synonymPairs))
    # print(SN_join.SN_join(S, T, synonymPairs, 0.2, SN_join.full_expansion_sim_measure))

# for SI_join testing
    rule_set_2 = [
        ('Intl', 'International'),
        ('Conf', 'Conference'),
        ('VLDB', 'Very Large Data Bases'),
        ('Very Large Data Bases', 'VLDB'),
    ]

    q1 = '2013 ACM Intl Conf on Management of Data USA'
    q2 = 'Very Large Data Bases Conf'
    q3 = 'VLDB Conf'
    q4 = 'ICDE 2013'

    S = [q1, q2, q3, q4]
    T = [q3, q4, q1, q2]
    # print(I_list(S, rule_set_2, 0.7))
    # print(SN_join.SN_signatures_gen(q4, 0.7, rule_set_2))
    # print(SN_join.full_expand(q3, rule_set_2))
    # print(SI_index(S, rule_set_2, 0.8))
    # print(SI_index(T, rule_set_2, 0.8))
    # SI_tree_S = SI_index(S, rule_set_2, 0.8)
    # SI_tree_T = SI_index(T, rule_set_2, 0.8)
    # print(SI_join(S, T, 0.8, rule_set_2, SN_join.full_expansion_sim_measure))
