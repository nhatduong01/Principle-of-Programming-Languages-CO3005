def flatten(mylist):
    return [x for y in mylist for x in y]
print(flatten([[1,2,3],[4,5],[6,7]]))
