def expanding(l):
    a = 0
    for i in range(1, len(l)):
        if a >= abs(l[i] - l[i - 1]):
            return False
        a = abs(l[i] - l[i - 1])
    else:
        return True

def accordian(l):
    if len(l) < 3:
        return False
    new = []
    for q in range(len(l)-1):
        k = abs(l[q]-l[q + 1])
        new.append(k)
    tep = []
    for i in range(0,len(new)-1):
        if new[i] > new[i + 1]:
            tep.append("L")
        if new[i] < new[i + 1]:
            tep.append("H")
        if new[i] == new[i + 1]:
            tep.append("E")
    if "E" in tep:
        return False
    else:
        for g in range(len(tep) - 1):
            if tep[g] == tep[g + 1]:
                return False
        else:
            return True


def rotate(m):
    n = len(m)
    new = []
    for i in range(n):
        temp = []
        for j in range(n - 1, -1, -1):
            temp.append(m[j][i])
        new.append(temp)

    return new


