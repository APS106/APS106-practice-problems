
def convert_to_one_line_readlines(filename):
    ''' (str) -> None
    Read in the file in filename and write it out in one line, separated by spaces
    '''
    
    s = ""
    with open(filename) as infile:
        text = infile.readlines()
        for line in text:
            # add line onto s after removing the \n and adding a space
            s = s + line.rstrip('\n') + " "

    return s

def convert_to_one_line_read(filename):
    ''' (str) -> None
    Read in the file in filename and write it out in one line, separated by spaces
    '''
    
    with open(filename) as infile:
        text = infile.read()
        # replace all the \n with spaces
        s = text.replace("\n", " ")

    return s

def convert_to_one_line_readline(filename):
    ''' (str) -> None
    Read in the file in filename and write it out in one line, separated by spaces
    '''
    
    s = ""
    with open(filename) as infile:
        text = infile.readline()
        while text != "":
            # add text onto s after removing the \n and adding a space
            s = s + text.rstrip('\n') + " "
            text = infile.readline()
            
    return s

def convert_to_one_line_for(filename):
    ''' (str) -> None
    Read in the file in filename and write it out in one line, separated by spaces
    '''
    
    s = ""
    with open(filename) as infile:
        for text in infile:
            # add text onto s after removing the \n and adding a space
            s = s + text.rstrip('\n') + " "

    return s

s = convert_to_one_line_readlines("onetwo.txt")
print(s)
s = convert_to_one_line_read("onetwo.txt")
print(s)
s = convert_to_one_line_readline("onetwo.txt")
print(s)
s = convert_to_one_line_for("onetwo.txt")
print(s)
        
        
