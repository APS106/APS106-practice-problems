import csv

    
def load_bb_file(bb_file):
    ''' (str) -> dictionary {id : mark}
    Return a dictionary containing a subset of the the elements of 
    the CSV file bb_file indexed by row[id_index]
    '''
    
    id_index = 1
    mark_index = 3
    
    print("*** Processing", bb_file)
    
    database = {}
    with open(bb_file, 'r') as csvfile:
        grades_reader = csv.reader(csvfile)
    
        for row in grades_reader:  
            if row[0] != "Last Name": # skip header
                
                # get the two fields that we want and stick them into the dictionary
                id = row[id_index]
                mark = float(row[mark_index])
                #print(id, mark)
                
                database[id] = mark
    
    print("*** Done processing", bb_file)
    return database

def load_crowdmark_file(crowdmark_file):
    ''' (str) -> dictionary {id : mark}
    Return a dictionary containing a subset of the the elements of 
    the CSV file crowdmark_file indexed by row[id_index]
    '''
    
    print("*** Processing", crowdmark_file)
    
    id_index = 2
    mark_index = 11
    
    database = {}
    with open(crowdmark_file, 'r') as csvfile:
        grades_reader = csv.reader(csvfile)
    
        for row in grades_reader:  
            if row[0] != "Crowdmark ID": # skip header

                # get the two fields that we want and stick them into the dictionary
                id = row[id_index]
                mark = float(row[mark_index])
                #print(id, mark)
                
                database[id] = mark
    
    print("*** Done processing", crowdmark_file)
    return database


# read in the two files 
crowdmarks = load_crowdmark_file("crowdmarks.csv")
bb_marks = load_bb_file("bb.csv")

for student in bb_marks.keys():
    # for each students in bb_marks, check existence and mark accuracy in the
    # crowdmarks file
    if student not in crowdmarks:
        print(student, "not in Crowdmark file.")
    elif bb_marks[student] != crowdmarks[student]:
        print("Error: Mark mismatch for", student, bb_marks[student], crowdmarks[student])