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
        self.P = []

def I_list(S, rule_set, theta):
    token_l = {}
    temp = copy.deepcopy(S)
    for i in range(len(temp)):
        temp[i] = SN_join.SN_signatures_gen(temp[i], theta, rule_set)
        for j in temp[i]:
            if j in token_l:
                token_l[j].append(i)
            else:
                token_l[j] = [i]
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
    # print(sID_L_F)

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
    
    for i in root:
        for j in i.P:
            print(i.u, i.v, j.t)
    # leaf entry
    I_L = I_list(S, rule_set, theta)
    print(I_L)
    for i in sID_L_F:
        for j in root:
            if j.u == i[1]:
                for k in j.P:
                    if k.t == i[2]:
                        k.P.append(SN_join.SN_signatures_gen(S[i[0]], theta, rule_set))
    for i in root:
        for j in i.P:
            for k in j.P:
                print(i.u, i.v, j.t, k)

    return root

def SI_join(SI_s, SI_t, theta, rule_set):
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

    S = [q1, q2, q3, q4]
    # I_list(S, rule_set_2)
    # print(SN_join.SN_signatures_gen(q4, 0.7, rule_set_2))
    # print(SN_join.full_expand(q3, rule_set_2))
    print(SI_index(S, rule_set_2, 0.7))