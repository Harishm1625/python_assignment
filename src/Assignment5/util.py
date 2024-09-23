
# def dt():
#
#     from datetime import datetime
#     date=input("Enter date : ")
#     date_str = datetime.strptime(date,"%d %m %Y")
#     day=date_str.strftime("%A")
#
#     return day
#
# v=dt()
# print(v)
#

from datetime import datetime

def calender_module(n):

    str_format=datetime.strptime(n,"%d %m %Y")

    res=datetime.strftime(str_format,"%A")
    print(res)
    return res
# sample

