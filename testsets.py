


def main():
    blue_eyes = {'Olivia', 'Harry', 'Lilly', 'Jack', 'Amelia'}
    blonde_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Josh'}
    smell_hcn = {'Harry', 'Amelia'}
    taste_ptc = {'Harry', 'Lilly', 'Amelia', 'Lola'}
    o_blood = {'Mia','Josh','Lily', 'Olivia'}
    b_blood = {'Amelia', 'Jack'}
    a_blood = {'Harry'}
    ab_blood = { 'Lola'}

    #test for union
    print(blue_eyes.union(blonde_hair))
    # intersection
    print(smell_hcn.intersection(taste_ptc))
    # difference
    print(smell_hcn.difference(b_blood))
    # symmetric difference
    print(blue_eyes.symmetric_difference(o_blood))

    print(ab_blood.issubset(taste_ptc))

if __name__ == '__main__':
    main()