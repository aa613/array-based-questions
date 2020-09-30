def sum3(ar,targetsum):
    vp1={}
    rtn=[]
    z=ar
    for a in ar:
        o1=targetsum-a
        vp1[a]=o1
        ar.remove(a)
        vp2={}
        for i in ar:
            o2=o1-i
            vp2[i]=o2
            if o2 in vp2 and o2 in z:
                result=[o2,i,a]
                result.sort()
                rtn+=[result,]
            else:
                vp2[i]=o2

    return rtn
print(sum3([78,34,37,2,3,4,-2,-1],39))


                