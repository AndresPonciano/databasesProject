import math

def get_common_signatures(i_list_1, i_list_2):
    G = list()

    for item in i_list_1:
        if item in i_list_2.keys():
            G.append(item)

    return G

def get_upper_bound(i_list_1, i_list_2):
    G = get_common_signatures(i_list_1, i_list_2)

    upper_bound = 0

    for signature in G:
        upper_bound += len(i_list_1[signature]) * len(i_list_2[signature])

    # print(upper_bound)
    return upper_bound

def get_lower_bound(i_list_1, i_list_2):
    G = get_common_signatures(i_list_1, i_list_2)

    lower_bound = 0

    idk = [len(i_list_1[signature])*len(i_list_2[signature]) for signature in G]
    return max(idk)

# division hash function
def hash_func_1(k, num_ids):
    M = pow(2, num_ids-1)

    return k % M

# multiplicative hashing function
def hash_func_2(k, num_ids):
    M = pow(2, num_ids-1)

    # 33 and 34 are used bc they are coprime
    val = ( 33 * k ) % 34
    val = val / ( 34 / M )
    
    val = math.floor(val)

def build_fm_sketh(hf):
    #temporary; this should be given by function
    stringIDs = [1,2,3,1,2,3,1,1,4]

    # hash_map = {}
    bitvect_list = []
    for sid in stringIDs:
        key_val = hf(sid, len(stringIDs))
        # print(key_val, bin(key_val)[2:])
        bitvect = [0] * len(stringIDs)
        tempbit = list(bin(key_val)[2:])
        # print(bitvect, tempbit)
        j = len(bitvect)-1
        for i in range(len(tempbit)-1, -1, -1):
            bitvect[j] = tempbit[i]
            j -= 1
            if j < 0: break
    
        # print(bitvect)
        bitvect_list.append(bitvect)

    # for bruh in bitvect_list: print(bruh)
    #position of ones to build final sketch
    ones = [0]*len(stringIDs)
    for i in range(0, len(bitvect_list)):
        for j in range(0, len(bitvect_list[i])):
            if bitvect_list[i][j] == '1':
                ones[j] = '1'
                break
    # print('---')   
    # print(ones)

def build_2dhs(vgs, vgt):
    dhs2 = [[0 for i in range(len(vgs))] for j in range(len(vgt))]
    print(dhs2)

    for i in range(len(dhs2)):
        print(i)
        for j in range(len(dhs2[i])):
            print(j)
            if vgs[j] == 1 and vgt[i] == 1:
                dhs2[i][j] = 1
        print('---')

    print(dhs2)



if __name__ == "__main__":
    build_fm_sketh(hash_func_1)

    sketch1 = [1,1,1]
    sketch2 = [1,1,0,1]
    build_2dhs(sketch1, sketch2)
    #signatures are the keys
    # i_list_1 = {
    # 'ACM': ['q1'],
    # 'Conf': ['q2', 'q3'], 
    # 'Conference': ['q1', 'q2', 'q3'],
    # 'International': ['q1'],
    # 'on': ['q1'],
    # 'ICDE': ['q4'],
    # }

    # i_list_2 = {
    # 'International': ['q1', 'q2'],
    # 'WH': ['q3'],
    # 'Conf': ['q3', 'q4'],
    # 'Conference': ['q4', 'q5', 'q6'],
    # '2012': ['q7'],
    # }

    # ub = get_upper_bound(i_list_1, i_list_2)
    # print(ub)
    # lb = get_lower_bound(i_list_1, i_list_2)
    # print(lb)