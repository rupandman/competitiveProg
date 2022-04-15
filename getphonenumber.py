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
        if len(i)==4:
            res.append((f"double {dic[i[0]]} "*2).strip())
        if len(i)>4 and (len(i)+1)%3==0:
            res.extend(((f"triple {dic[i[0]]} " * (len(i) // 3)).rstrip(), "double " + dic[i[0]]))
        if len(i)>4 and (len(i)+2)%3==0:
            res.extend(((f"triple {dic[i[0]]} " * (len(i) // 3)).rstrip(),dic[i[0]]))
        if len(i)>4 and len(i)%3==0:
            res.append((f"triple {dic[i[0]]} " * (len(i) // 3)).rstrip())

    return " ".join(res)


n = input("Enter a phone number: ")
print(getPhoneNumber(n))
