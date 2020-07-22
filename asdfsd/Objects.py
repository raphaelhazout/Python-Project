# מאפיינים : name,numcourse,nummax,numlist
class Course:
    def __init__(self):
        self.numlist=int(input('Enter Number of students: '))
        self.name=input('Enter Name: ')
        self.numcourse=int(input('Enter the number of the Course: '))
        self.nummax=int(input('Enter the maximum number of students: '))

    def info(self):
        return (f'\n The name of the course is: {self.name} \n The number of the course is: {self.numcourse} \n The number of the students who sign to the course:{self.numlist} \n The number of the maximum students is: {self.nummax}')

    def yahas(self):
        return self.nummax-self.numlist



C1=Course()
print(C1.info())
print(C1.yahas())