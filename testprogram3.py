def sc(l,found):
    count=0
    for i in range(len(l)):
        if l[i]==found:
            count+=1
        if count==2:
            return i
    return 0
print(sc([1,2,1,3,4,4],3))