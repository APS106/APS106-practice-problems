# Write a function that takes in a DNA strand and produces its 
# matching counterpart in a double helix. 
#      A <-> T
#      C <-> G

# I decided to create a helper function since the code basically does the 
# same thing for A <-> T and C <-> G
def swap_base_pair(dna, n1, n2):
    '''
    (str, str, str) -> str
    Replace all occurences of n1 with n2 and all occurences of n2 with n1
    in dna string
    '''
    
    dna = dna.replace(n2, "*")  # replace n2 with *
    dna = dna.replace(n1, n2)   # replace n1 with n2
    dna = dna.replace("*", n1)  # replace * with n1
    
    return dna

# Bonus question: Why doesn't the following work?
# dna = dna.replace(n2, n1)  # replace n2 with n1
# dna = dna.replace(n1, n2)   # replace n1 with n2
    
def duplicate_DNA_strand(dna):
    '''
    (string) -> string
    Takes in a string of nuclerotide letters (ATGC)
    and returns the matching DNA where:
      A <-> T
      C <-> G
    '''
    dna = swap_base_pair(dna,"A","T")
    dna = swap_base_pair(dna,"C","G")
    return dna

chrome_4 = "ATGGGCAATCGATGGCCTAATCTCTCTAAG"
print(chrome_4,duplicate_DNA_strand(chrome_4),sep="\n")

    