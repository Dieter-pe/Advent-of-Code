
def open_file(filename):
    
    l = []
    
    f = open(filename, "r")
    f = f.readlines()
    
    
    for line in f:
        line = line.strip('\n')
        l.append(line)
           
    return l