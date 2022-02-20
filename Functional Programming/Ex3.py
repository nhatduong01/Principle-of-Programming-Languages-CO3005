def lessThan(lst,num):
    if lst == []:
        return []
    else:
        if lst[0] < num:
            return [lst[0]] + lessThan(lst[1:], num)
        else:
            return lessThan(lst[1:], num)
print(lessThan([1,2,3,4,5],4))