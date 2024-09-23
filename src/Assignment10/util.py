
def cnt(n):

    fruits = []

    count={}

    for i in  n:
        if i in count:
            count[i] += 1

        else:
            count[i]=1

    # print(count)

    j=[]
    for k,v in count.items():
        j.append(v)

    return j



