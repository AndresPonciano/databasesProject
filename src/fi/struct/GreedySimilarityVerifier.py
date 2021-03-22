def rule_gain(rule, string1, string2, all_rules):
    print('finding rule gain')

    rhs = set(rule[1].split(' '))
    print(string1)
    set1 = set(string1.split(' '))
    print(rhs, set1)

    U = rhs.difference(set1)
    print(U)
    if not U:
        return 0


    



    return 1



if __name__ == "__main__":

    q1 = 'Intl WH Conf 2012'
    t2 = 'Intl Wireless Health Conference 2012 UK'

    synonymPairs = {
        'WH': 'Wireless Health',
        'Intl': 'International',
        'Wireless Health': 'WH',
        'Conference': 'Conf',
        'UK': 'United Kingdom',
        'Conf': 'Conference',
    }

    rule = ('WH', 'Wireless Health')

    rule_gain1 = rule_gain(rule, q1, t2, synonymPairs)
