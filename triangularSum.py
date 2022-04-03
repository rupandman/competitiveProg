def triangularSum(ls):
    if len(ls) == 1:
        return ls[0]
    while(len(ls)>1):
        ls = [(ls[i]+ls[i+1])%10 for i in range(len(ls)-1)]
    return ls[0]
l = [1,2,3,4,5]
print(triangularSum(l))


