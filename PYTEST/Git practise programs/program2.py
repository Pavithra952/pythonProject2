def add_list1(l):
    sum=0
    r=[]
    for i in range(len(l)):
        while l[i]>0:
            m=int(l[i]%10)
            sum=sum+m
            l[i]=int(l[i]/10)
        r.append(sum)
        sum=0
    return r
print(add_list1([342,542,123]))