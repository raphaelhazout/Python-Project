from asdfsd.Course import Course
from asdfsd.Student import Student

cnumber=int(input('Whats the number of the Course? '))
name1=input('Whats the name of the Course? ')
subject=input('Put Subject')
teacher=input('Whats the name of the teacher? ')
Course.dic1[subject]=teacher
c1=Course(cnumber,name1)
