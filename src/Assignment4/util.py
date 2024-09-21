
#
# n=5
#
#
# h=0
# def ags ():
#     for i in range(1,n):
#         print( i," ",oct(i)[2:]," ",hex(i)[2:]," ", bin(i)[2:])
#         # i=h
#         # return h
# s=ags()
# print(s)


n = 5

def ags():
    result = []
    for i in range(1, n):
        result.append(f"{i}\t{oct(i)[2:]}\t{hex(i)[2:]}\t{bin(i)[2:]}")
    return "\n".join(result)

s = ags()
print(s)
