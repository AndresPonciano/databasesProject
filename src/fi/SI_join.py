import SN_join
import copy
import FE_sim
import SE_sim
class Fence_Entry:
    def __init__(self, s, rule_set):
        self.u = len(s.split(' '))
        self.v = len(FE_sim.full_expand(s, rule_set))
        self.P = []

class Leaf_Entry:
    def __init__(self, s, rule_set):
        self.t = len(FE_sim.full_expand(s, rule_set))
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
        i = FE_sim.full_expand(i, rule_set)
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
    
    # leaf entry
    for i in sID_L_F:
        for j in root:
            if j.u == i[1]:
                for k in j.P:
                    if k.t == i[2]:
                        k.P = SN_join.SN_signatures_gen(S[i[0]], theta, rule_set)
    # Show the tree
    # for i in root:
    #     for j in i.P:
    #             print(i.u, i.v, j.t, j.P)

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
    

