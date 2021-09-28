




def kuo(a):
    l = []
    for i in a :
        if i == "[" or i == "(" or i == "{":
            l.append(i)
        elif i =="]":
            if len(l) ==0 or l.pop() != "[":
                return False
        elif i ==")":
            if len(l) ==0 or l.pop() != "(":
                return False
        elif i =="}":
            if len(l) ==0 or l.pop() != "{":
                return False
    if len(l) != 0:
        return False
    else:
        return True
a = "{{([{}])}"
print(kuo(a))