# Variation of Q3 from p. 226 of Gries book 3rd edition
# Write a function that takes in two equal size sets with arbitrary 
# element types and returns a set of element pairs containing each element 
# from the input sets in exactly one pair. For example, input {'a','b'} and
# {1,2} could produce output {('a',1), ('b', 2)}.

def generate_corresponding_pairs(s1, s2):
    """ 
    (set, set) -> set of tuple

    Return a set of tuples where each tuple contains an entry from s1
    and an entry from s2.
    """ 

    pairs = set()
    n = len(s1)

    for i in range(n):

        entry1 = s1.pop()
        entry2 = s2.pop()
        pairs.add((entry1, entry2),)

    return pairs

def generate_all_pairs(s1, s2):
    """ 
    (set, set) -> set of tuple

    Return a set of tuples where each tuple contains an entry from s1
    and an entry from s2.
    """ 

    pairs = set()

    for i in s1:
        for j in s2:
            pairs.add((i, j),)

    return pairs

print(generate_corresponding_pairs({'Anne', 'Beatrice', 'Cari'}, 
                                   {'Ali', 'Bob', 'Chen'}))
print(generate_all_pairs({'Anne', 'Beatrice', 'Cari'}, 
                                   {'Ali', 'Bob', 'Chen'}))