
def dist2(lst,n):
    if lst == []:
        return []
    else:
        return [(lst[0],n)] + dist2(lst[1:],n)
def dist(lst,n):
    if lst == []:
        return []
    else:
        return [(lst[0],n)] + dist(lst[1:],n)
print(dist([1,2,3], 4))