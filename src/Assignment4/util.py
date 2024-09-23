

# n=5



# def ags (n):
# #     h = []
# #     for i in range(1,n+1):
# #         lis= f"{i} {oct(i)[2:]} {hex(i)[2:]} {bin(i)[2:]}"
# #         h.append(lis)
# #     return h
# # s=ags(n)
# # print(s)
#

# #
# n = 5
#
# def ags():
#     result = []
#     for i in range(1, n):
#         result.append(f"{i}\t{oct(i)[2:]}\t{hex(i)[2:]}\t{bin(i)[2:]}")
#     return "\n".join(result)
#
# s = ags()
# print(s)


def str_format(n):
    res = []
    for i in range(1, n + 1):
        format_str = f"{i} {oct(i)[2:]} {hex(i)[2:]} {bin(i)[2:]}"
        res.append(format_str)
        print(res)
    return res

# sample

