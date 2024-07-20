#!/usr/bin/env python3
# Author ID: iaoluwajuwon

class Student:
     # Define the name and number when a student object is created, ex. student1 = Student('john', 025969102)
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)
        self.courses = {}


        # Return student name and number
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number


    # Add a new course and grade to students record
    def addGrade(self, course, grade):
        self.courses[course] = grade


        # Calculate the grade point average of all courses and return a string
    def displayGPA(self):
        if not self.courses:
            return 'GPA of student ' + self.name + ' is 0.0'

        total_grades = sum(self.courses.values())
        num_courses = len(self.courses)

        try:
            gpa = total_grades / num_courses
            return 'GPA of student ' + self.name + ' is ' + str(gpa)
        except ZeroDivisionError:
            return 'Error: Division by zero occurred while calculating GPA.'

        # Return a list of course that the student passed (not a 0.0 grade)
    def displayCourses(self):
        passed_courses = [course for course, grade in self.courses.items() if grade > 0.0]
        return passed_courses

if __name__ == '__main__':
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    student2 = Student('Jessica', '123456')
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())

