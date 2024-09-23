
def fnd_avg():
    student={
    "raj":[25,40,30],
    "vijay":[50.45,20],
    "krish":[35,30,32]
    }

    student_name=input("enter the student name:")
    marks=student[student_name]
   # total=sum(marks)
    #avg=total/3
    lst=0
    for i in marks:
        lst+=i
    avg=lst/3
    return avg

l=fnd_avg()
print(l)


