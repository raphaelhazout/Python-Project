
class Student:

    def __init__(self,id,name,dic):
        self.id=id
        self.name=name
        self.dic=dic
        self.dic={}
    def addgrade(self,subject,grade):
        self.dic[subject]=grade

    def calc_factor(self,subject,factor):
        self.dic[subject]=(self.grade*factor)/100+factor
        if self.dic > 100:
            self.dic = 100
            return self.dic
    def average(self):
        sum=0
        for i in self.dic.values():
            sum+=i
            b=sum//len(self.dic)
            return b

    def __str__(self):
        return (f'i am the student {self.name}, my id number is {self.id}, the list of my subjects and grades is {self.dic}')

