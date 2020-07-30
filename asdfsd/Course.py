from asdfsd.Student import *
class Course:

    def __init__(self,cnumber,name1,dic1,slist,smax):
        self.cnumber=cnumber
        self.name1=name1
        self.dic=dic1
        self.dic1={}
        self.slist=slist
        self.slist=[]
        self.smax=smax

    def __str__(self):
        return (f'The Course name is {self.name1}, the number of the course is {self.cnumber}, the list of the Subjects {self.dic1},the list of the Students is {self.slist}, the maximum students in class is {self.smax}')

    def add_student(self,Student):
        self.slists.append(Student)
        if len(self.slist) > self.smax:
            print(True)
        else:
            print(False)

    def add_factor(self,subject,factor):
        for stud in self.slist:
            stud.calc_factor(subject,factor)

    def del_student(self,id1):
        for stud in self.slist:
            if stud.id == id1:
                self.slist.remove(id1)

    def calc_avg(self):
        sum=0
        for students in self.slist:
            sum+=students.average()
        return sum/len(self.slist)
