def secondlrg ():
    scores=[10,20,30,40]
    s=[2,5,7,8,9,7]
    first=scores[0]
    second=0
    for i in s:
        if i > first:
            second=first
            first = i

    return second


v=secondlrg()
print(v)## for print the output ## return kudutha output la show aagathu so vera veriable la store panni print panalam


# sample