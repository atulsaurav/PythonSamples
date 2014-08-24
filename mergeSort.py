'''Simple Merge Sort Implementation'''

ilist = ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 't', 'h', 'e', ' ',
         'i', 'n', 'p', 'u', 't', ' ', 'l', 'i', 's', 't']

def mySort(inList):
    if len(inList) == 1:
        return inList
    elif len(inList) == 2:
        if inList[0] >= inList[1]:
            return [inList[1], inList[0]]
        else:
            return inList
    else:
        mid = len(inList)//2
        a = inList[0:mid]
        b = inList[mid:]
        srtd = myMerge(mySort(a),mySort(b))
        return srtd

def myMerge(aList, bList):
    rslt = []
    i = 0
    j = 0
    if aList[0] > bList[0]:
        rslt.append(bList[0])
        j += 1
    else:
        rslt.append(aList[0])
        i += 1
    for k in range(1,len(aList) + len(bList)):
        if i < len(aList) and j < len(bList):
            if aList[i] > bList[j]:
                rslt.append(bList[j])
                j += 1
            else:
                rslt.append(aList[i])
                i += 1
        elif j == len(bList):
            rslt += aList[i:]
            break
        else:
            rslt += bList[j:]
            break
    return rslt
            
ans = mySort(ilist)
print (len(ilist),len(ans))
print (ans)
print (sorted(ilist))
