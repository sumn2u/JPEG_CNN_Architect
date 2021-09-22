#Taken from stackoverflow https://stackoverflow.com/questions/48959098/how-to-create-a-new-text-file-using-python/48964410#48964410
#Read a file line by line
file = open('path/to/file', 'r') 
count = 0

while True:
    line = file.readline()
    if not line: 
        break
    
    # do something here
    
    count += 1
file.close()