def even_square(l):
    r=[]
    for i in range(len(l)):
        if i%2==0:
            r.append(l[i]**2)
    return r
print(even_square([1,2,3,4,5,6]))