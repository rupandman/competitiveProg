from itertools import groupby

def getPhoneNumber(number):
    ls = [tuple(y) for x, y in groupby(number)]
    res = []
    dic = {'0': "zero", '1':"one", '2':"two", '3':"three", '4':"four", '5':"five", '6':"six", '7':"seven", '8':"eight", '9':"nine"}
    for i in ls:
        if len(i)==1:
            res.append(dic[i[0]])
        if len(i)==2:
            res.append(f"double {dic[i[0]]}")
        if len(i)==3:
            res.append(f"triple {dic[i[0]]}")
        if len(i)>2 and len(i)%2==0:
            res.append((f"double {dic[i[0]]} " * (len(i)//2)).rstrip())
        if len(i)>3 and len(i)%2!=0:
            res.extend(((f"double {dic[i[0]]} " * ((len(i) // 2) - 1)).rstrip(), "triple " + dic[i[0]]))

    return " ".join(res)


n = input("Enter a phone number: ")
print(getPhoneNumber(n))

# dic = {'0': "zero", '1':"one", '2':"two", '3':"three", '4':"four", '5':"five", '6':"six", '7':"seven", '8':"eight", '9':"nine"}
# n = "567"
# ls = [tuple(y) for x, y in groupby(n)]
# for i in ls:
#     print(dic[i[0]], end=" ")