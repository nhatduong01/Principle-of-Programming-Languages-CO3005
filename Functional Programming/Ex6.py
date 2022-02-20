from functools import reduce


def flatten(mylist):
    return reduce(lambda x,y: x+ y, mylist,[])
print(flatten([[1,2,3],[4,5],[6,7]]))