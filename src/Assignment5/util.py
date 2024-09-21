
def dt():

    from datetime import datetime
    date=input("Enter date : ")
    date_str = datetime.strptime(date,"%d %m %Y")
    day=date_str.strftime("%A")

    return day

v=dt()
print(v)

