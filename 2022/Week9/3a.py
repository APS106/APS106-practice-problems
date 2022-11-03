def copy_file_readlines(out_name, in_name="grades.txt"):
    ''' (str,str) -> None
    Read the file in in_name and output it to out_name
    '''
    
    out_file = open(out_name, 'w')
    with open(in_name, 'r') as in_file:
        text = in_file.readlines()
        for line in text:
            out_file.write(line)

    out_file.close()

def copy_file_read(out_name, in_name="grades.txt"):
    ''' (str,str) -> None
    Read the file in in_name and output it to out_name
    '''
    
    out_file = open(out_name, 'w')
    with open(in_name, 'r') as in_file:
        out_file.write(in_file.read())

    out_file.close()

def copy_file_readline(out_name, in_name="grades.txt"):
    ''' (str,str) -> None
    Read the file in in_name and output it to out_name
    '''
    
    out_file = open(out_name, 'w')
    with open(in_name, 'r') as in_file:        
        text = in_file.readline()
        while text != "":
            out_file.write(text)
            text = in_file.readline()

    out_file.close()

def copy_file_for(out_name, in_name="grades.txt"):
    ''' (str,str) -> None
    Read the file in in_name and output it to out_name
    '''
    
    out_file = open(out_name, 'w')
    with open(in_name, 'r') as in_file:        
        for text in in_file:    
            out_file.write(text)

    out_file.close()

copy_file_readlines("readlines.txt")
copy_file_read("read.txt")
copy_file_readline("readline.txt")
copy_file_readline("for.txt")
