import SE_sim, FE_sim, Jaccard
import SN_join, SI_join
import matplotlib.pyplot as plt
import time

if __name__ == "__main__":
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

    t1 = []
    t2 = []
    t3 = []

    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:10], 0.8, Jaccard.Jaccard_sim_measure)
    t1.append(time.time() - start_time)
    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:20], 0.8, Jaccard.Jaccard_sim_measure)
    t1.append(time.time() - start_time)
    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:30], 0.8, Jaccard.Jaccard_sim_measure)
    t1.append(time.time() - start_time)
    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:40], 0.8, Jaccard.Jaccard_sim_measure)
    t1.append(time.time() - start_time)
    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:50], 0.8, Jaccard.Jaccard_sim_measure)
    t1.append(time.time() - start_time)
    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:90], 0.8, Jaccard.Jaccard_sim_measure)
    t1.append(time.time() - start_time)

    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:10], 0.8, FE_sim.full_expansion_sim_measure)
    t2.append(time.time() - start_time)
    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:20], 0.8, FE_sim.full_expansion_sim_measure)
    t2.append(time.time() - start_time)
    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:30], 0.8, FE_sim.full_expansion_sim_measure)
    t2.append(time.time() - start_time)
    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:40], 0.8, FE_sim.full_expansion_sim_measure)
    t2.append(time.time() - start_time)
    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:50], 0.8, FE_sim.full_expansion_sim_measure)
    t2.append(time.time() - start_time)
    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:90], 0.8, FE_sim.full_expansion_sim_measure)
    t2.append(time.time() - start_time)
    
    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:10], 0.8, SE_sim.SE_sim_measure)
    t3.append(time.time() - start_time)
    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:20], 0.8, SE_sim.SE_sim_measure)
    t3.append(time.time() - start_time)
    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:30], 0.8, SE_sim.SE_sim_measure)
    t3.append(time.time() - start_time)
    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:40], 0.8, SE_sim.SE_sim_measure)
    t3.append(time.time() - start_time)
    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:50], 0.8, SE_sim.SE_sim_measure)
    t3.append(time.time() - start_time)
    start_time = time.time()
    SN_join.SN_join(Tq, Tt, rule_set[:90], 0.8, SE_sim.SE_sim_measure)
    t3.append(time.time() - start_time)
    print("done SN")
    t4 = []
    t5 = []
    t6 = []

    start_time = time.time()
    SI_join.SI_join(Tq, Tt, rule_set[:10], 0.8, Jaccard.Jaccard_sim_measure)
    t4.append(time.time() - start_time)
    print("done 1")
    start_time = time.time()
    SI_join.SI_join(Tq, Tt, rule_set[:20], 0.8, Jaccard.Jaccard_sim_measure)
    t4.append(time.time() - start_time)
    print("done 1")
    start_time = time.time()
    SI_join.SI_join(Tq, Tt, rule_set[:30], 0.8, Jaccard.Jaccard_sim_measure)
    t4.append(time.time() - start_time)
    print("done 1")
    

    start_time = time.time()
    SI_join.SI_join(Tq, Tt, rule_set[:10], 0.8, FE_sim.full_expansion_sim_measure)
    t5.append(time.time() - start_time)
    print("done 1")
    start_time = time.time()
    SI_join.SI_join(Tq, Tt, rule_set[:20], 0.8, FE_sim.full_expansion_sim_measure)
    t5.append(time.time() - start_time)
    print("done 1")
    start_time = time.time()
    SI_join.SI_join(Tq, Tt, rule_set[:30], 0.8, FE_sim.full_expansion_sim_measure)
    t5.append(time.time() - start_time)
    print("done 1")
    
    start_time = time.time()
    SI_join.SI_join(Tq, Tt, rule_set[:10], 0.8, SE_sim.SE_sim_measure)
    t6.append(time.time() - start_time)
    print("done 1")
    start_time = time.time()
    SI_join.SI_join(Tq, Tt, rule_set[:20], 0.8, SE_sim.SE_sim_measure)
    t6.append(time.time() - start_time)
    print("done 1")
    start_time = time.time()
    SI_join.SI_join(Tq, Tt, rule_set[:30], 0.8, SE_sim.SE_sim_measure)
    t6.append(time.time() - start_time)
    print("done 1")

    num_synonyms_1 = [10, 20, 30, 40, 50, 90]
    num_synonyms_2 = [10, 20, 30]
    fig, axes = plt.subplots(nrows=2)
    axes[0].plot(num_synonyms_1, t1)
    axes[0].plot(num_synonyms_1, t2)
    axes[0].plot(num_synonyms_1, t3)
    axes[1].plot(num_synonyms_2, t4)
    axes[1].plot(num_synonyms_2, t5)
    axes[1].plot(num_synonyms_2, t6)
    plt.legend(['SN(Jaccard)', 'SN(FE)', 'SN(SE)', 'SI(Jaccard)', 'SI(FE)', 'SI(SE)'])
    plt.show()
