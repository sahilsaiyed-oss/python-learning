
def rem(l,word):
    for item in l:
        l.remove(word)
        return l

l = ["harry","rohan", "shubham", "an"]
print(rem(l,"an"))    