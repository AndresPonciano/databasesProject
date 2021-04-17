The dataset that we scrap includes all the txt files.
We mainly use the TagetTable.txt and QueryTable.txt for doing experiment with synonyms.txt as our rule set. 

This python code can be run in any environment with python 3 installed since we do not use special library.

To see each of the small test for each function we wrote: run "test.py"

For the evaluation of similarity measures: run "Evaluate_sim_measure.py"

For the evaluation of join: run "Evaluate_Join.py"

The 2 evaluations will take a couple minutes to run but should not be exceeding 30 minutes.

To get loose upper and lower bounds, all you need is two I-lists and run (return ints): 

    get_upper_bound(i_list_1, i_list_2):
    get_lower_bound(i_list_1, i_list_2):
    
To use the Estimation Signature Selection for upper and lower bounds.
With two I-lists available, you can get the attributes necessary to get the witness probabilities.

    rs, rt, miu_s, miu_t = get_rs_rt(i_list_1, i_list_2)
    ps_hat, pt_hat, x, y = get_witness_probabilites(rs, rt, dhs1, dhs1)
    
Then, with that information you can retrieve the tight upper and lower bounds (return ints)

    get_tight_ub(x, y, ps_hat, pt_hat, rs, rt, miu_s, miu_t):
    get_tight_lb(x, y, ps_hat, pt_hat, rs, rt, miu_s, miu_t):
