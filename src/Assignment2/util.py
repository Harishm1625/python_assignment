def secondlrg ():
    scores=[10,20,30,40]
    skm=[2,5,5,7,8,9,7]
    first=scores[0]
    second=0
    for i in scores:
        if i > first:
            second=first
            first = i

    print(second)


secondlrg()
