
def convert_to_one_line_readlines(filename, sep=" "):
    ''' (str) -> None
    Read in the file in filename and write it out in one line, separated by spaces
    '''
    
    s = ""
    with open(filename) as infile:
        text = infile.readlines()
        for line in text:
            s = s + line.rstrip('\n') + sep

    return s

def convert_to_one_line_read(filename, sep=" "):
    ''' (str) -> None
    Read in the file in filename and write it out in one line, separated by spaces
    '''
    
    with open(filename) as infile:
        text = infile.read()
        s = text.replace("\n", sep)

    return s

def convert_to_one_line_readline(filename, sep=" "):
    ''' (str) -> None
    Read in the file in filename and write it out in one line, separated by spaces
    '''
    
    s = ""
    with open(filename) as infile:
        text = infile.readline()
        while text != "":
            s = s + text.rstrip('\n') + sep
            text = infile.readline()
            
    return s

def convert_to_one_line_for(filename, sep=" "):
    ''' (str) -> None
    Read in the file in filename and write it out in one line, separated by spaces
    '''
    
    s = ""
    with open(filename) as infile:
        for text in infile:
            s = s + text.rstrip('\n') + sep

    return s

s = convert_to_one_line_readlines("onetwo.txt", "/")
print(s)
s = convert_to_one_line_read("onetwo.txt", ".")
print(s)
s = convert_to_one_line_readline("onetwo.txt", "?")
print(s)
s = convert_to_one_line_for("onetwo.txt", "*")
print(s)
        
        
