"""
Name: Zackery Vering
Project: Lab 2H
Date: 6 Sept 2018
"""
#create dictionary for students and grades
student_grades = {}
i = 0
#for the purpose of this lab, there will be 10 students. a more advanced version can be made to call a function
#that will ask the user if they'd like to input another student allowing for more dynamic input
for i in range(10):
    student = raw_input("Input the student's name.\n")
    grade = int(raw_input("Input the student's grade.\n"))
    student_grades[student] = grade
    i +=1
#print the list of students to show the order they were put in
print ("Here is the list of students in the order that they were input.")
for key in sorted(student_grades.iterkeys()):
    print ("{}:{}").format(key, student_grades[key])
#print the list of students after sorting by their grades
print ("Here is the list of students sorted by grade high to low.")
for key, value in sorted(student_grades.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print ("{}:{}").format(key, value)
#calculate and print the average for the class
average = sum(student_grades.values())
average = average/(len(student_grades))
print ("The average for the class is {}.").format(average)
