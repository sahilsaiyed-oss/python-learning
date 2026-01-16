f = open("file.txt")

print(f.read())

f.close()

# this same can be written by using this statemenet  like this : 
with open("file.txt") as f :
    print(f.read())

# you don't have to ex[plicitly  close the file     