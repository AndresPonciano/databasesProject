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

def get_tight_ub(x, y, ps_hat, pt_hat, rs, rt, miu_s, miu_t):
    phi_1 = 1.43

    temp = ( 1 - ( 1 / ( math.pow(2, rs) ) ) )
    temp2 = 1- math.pow(temp, miu_s)
    ps = ps_hat / temp2


    temp = ( 1 - ( 1 / ( math.pow(2, rt) ) ) )
    temp2 = 1- math.pow(temp, miu_t)
    pt = pt_hat / temp2

    u1 = miu_s * ( (math.log( 1 - ps ) ) / ( math.log( 1 - ( 1 /  ( math.pow(2, y) ) ) ) ) )
    u2 = miu_t * ( (math.log( 1 - pt ) ) / ( math.log( 1 - ( 1 /  ( math.pow(2, x) ) ) ) ) )

    return phi_1 * min(u1, u2)

def get_tight_lb(x, y, ps_hat, pt_hat, rs, rt, miu_s, miu_t):
    phi_2 = 0.8

    part1 = 1 - math.pow( ( 1 - ( 1 / ( math.pow(2, rs) + y) ) ), miu_s )
    part2 = ( 1 / math.pow(2, y) ) * ( 1 - math.pow( ( 1 - ( 1 / ( math.pow(2, rs) ) ) ), miu_s ) )
    triangle_p = part1 - part2

    ps_prime = ( ps_hat - triangle_p ) / ( 1 - math.pow( ( 1 - ( 1 / (math.pow(2, rs)) ) ), miu_s) ) 

    to_return = math.log(1 - ps_prime) / math.log( 1 - ( 1 / math.pow(2, y)))

    return phi_2 * miu_s * to_return

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

#return 2d matrix built from two diff 2dhs arrays
def build_2dhs(vgs, vgt):
    dhs2 = [[0 for i in range(len(vgs))] for j in range(len(vgt))]
    # print(dhs2)

    for i in range(len(dhs2)):
        for j in range(len(dhs2[i])):
            if vgs[j] == 1 and vgt[i] == 1:
                dhs2[i][j] = 1
        # print('---')

    # print(dhs2)
    return dhs2

def get_rs_rt(i_list_1, i_list_2):
    G = get_common_signatures(i_list_1, i_list_2)
    # print(G)
    miu_s = 0
    miu_t = 0

    for g in G:
        if g in i_list_1.keys():
            miu_s += len(i_list_1[g])

        if g in i_list_2.keys():
            miu_t += len(i_list_2[g])

    rs = math.log(miu_s, 2)
    rs = math.floor(rs)

    rt = math.log(miu_t, 2)
    rt = math.floor(rt)

    return rs, rt, miu_s, miu_t

#pass rs, rt and as many sketches as u have
def get_witness_probabilites(rs, rt, *sketches):
    # print(rs, rt)
    # print(len(sketches))
    w = len(sketches)
    f = 0.3 * w

    ps_hat = 0
    for y in range(0, rt):
        count = 0
        for i in range(1, w):
            for sketch in sketches:
                if sketch[rs][y] == 1:
                    count += 1

        if count <= f:
            ps_hat = count / w
            break

    pt_hat = 0    
    for x in range(0, rs):
        count = 0
        for i in range(1, w):
            for sketch in sketches:
                if sketch[x][rt] == 1:
                    count += 1

        if count <= f:
            pt_hat = count / w
            break

    return ps_hat, pt_hat, y, x

if __name__ == "__main__":
    build_fm_sketh(hash_func_1)

    sketch1 = [1,1,1]
    sketch2 = [1,1,0,1]
    dhs1 = build_2dhs(sketch1, sketch2)

    sketch3 = [1,1,0]
    sketch4 = [1,1,1,0]
    dhs2 = build_2dhs(sketch3, sketch4)

    #signatures are the keys
    i_list_1 = {
    'ACM': ['q1'],
    'Conf': ['q2', 'q3'], 
    'Conference': ['q1', 'q2', 'q3'],
    'International': ['q1'],
    'on': ['q1'],
    'ICDE': ['q4'],
    }

    i_list_2 = {
    'International': ['q1', 'q2'],
    'WH': ['q3'],
    'Conf': ['q3', 'q4'],
    'Conference': ['q4', 'q5', 'q6'],
    '2012': ['q7'],
    }

    rs, rt, miu_s, miu_t = get_rs_rt(i_list_1, i_list_2)

    get_witness_probabilites(rs, rt, dhs1, dhs1)

    # ub = get_upper_bound(i_list_1, i_list_2)
    # print(ub)
    # lb = get_lower_bound(i_list_1, i_list_2)
    # print(lb)