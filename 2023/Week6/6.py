# Write a function that takes in a DNA strand and produces its 
# matching counterpart in a double helix. 
#      A <-> T
#      C <-> G

    
def duplicate_DNA_strand(dna):
    '''
    (string) -> string
    Takes in a string of nucleotide letters (ATGC)
    and returns the matching DNA where:
      A <-> T
      C <-> G
    '''
    matching_dna = ""
    for ch in dna:
        if ch == "A":
            matching_dna += "T"
        elif ch == "T":
            matching_dna += "A"
        if ch == "C":
            matching_dna += "G"
        elif ch == "G":
            matching_dna += "C"

    return matching_dna

chrome_4 = "ATGGGCAATCGATGGCCTAATCTCTCTAAG"
print(chrome_4,duplicate_DNA_strand(chrome_4),sep="\n")

    