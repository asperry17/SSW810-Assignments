# -*- coding: utf-8 -*-
from prettytable import PrettyTable
from collections import defaultdict
import unittest
import os
###########################################################################################################################################################################################################                    
class Student:
    '''Setting up information about a single student class'''
    def __init__(self,cwid, name, major): # the special Python name for a method that initializes an individual object from its class definition.
        self.student_cwid = cwid          #Attributes
        self.student_name = name          #Attributes
        self.student_major = major        #Attributes
        self.student_courses = {}        #Course Dictionary | key is the student’s course and the value is the grade
        
    def coursestaken(self,course,lettergrade):         
        ''' Read the grades file and update information about students'''  
        self.student_courses[course] = lettergrade
                                                           
###########################################################################################################################################################################################################                    
class Instructor:
    '''Setting up information about a single instructor class '''
    def __init__(self,cwidi, name, department):
        self.instructor_cwid = cwidi
        self.instructor_name = name
        self.instructor_dept = department
        self.instructor_coursestaught = defaultdict(int)
                        
    def updateinstructor(self,course):
        ''' Read the grades file and update information about instructors'''
        self.instructor_coursestaught[course] += 1 

###########################################################################################################################################################################################################                    
class Repository:
    '''Setting up container class for all three data structures and information about the school'''
    def __init__(self,repo_fhand1,repo_fhand2,repo_fhand3):
        try:
            self.repo_fhand3 = open('C:\Python36\HW09\grades.txt', mode="r", encoding="utf-8")
            self.repo_fhand2 = open('C:\Python36\HW09\instructors.txt', mode="r", encoding="utf-8")
            self.repo_fhand1 = open('C:\Python36\HW09\students.txt', mode="r", encoding="utf-8")       
        except FileNotFoundError:
            print('The file cannot be opened:')
            return (0,0,0,0)
        else:
            with self.repo_fhand1,self.repo_fhand2, self.repo_fhand3:   #Automatically closes the file
                gradesfile = self.repo.fhand3.readlines()       #fhand3 is the grades.txt file
                instructorfile = self.repo.fhand2.readlines()   #fhand2 is the instructors.txt file
                studentfile = self.repo.fhand1.readlines()      #fhand1 is the students.txt file
                           
        self.students = {}       #Initialize an empty dictionary | key is the student’s CWID and the value is an instance of class Student 
        self.instructors = {}    #Initialize an empty dictionary | key is the instructor’s CWID and the value is an instance of class Instructor 
 
        for line in studentfile:
                cwid,name,major = line.strip().split('\t')  # returns a list with three tokens
                self.students[cwid] = Student(cwid,name,major)  #create a new student and store it in self.students.  Creating a new instance of class student and pass these 3 parameters
                                
        for line in instructorfile:
                cwidi, name, department = line.strip().split('\t')
                self.instructors[cwidi] = Instructor(cwidi, name, department)
           
        for line in gradesfile:
                ''' Read the pieces from the each line in the grades file then for each grade, call a new method in the student class that '''
                ''' asks the student to add that class and grade to the dict inside the instance of class student. '''
                cwid,course,lettergrade,cwidi = line.strip().split('\t')
                self.students[cwid].coursestaken(course,lettergrade)
                self.instructors[cwidi].coursestaught(course)
                            
    def ayanaprettytable(self):
        pt = PrettyTable(field_names=['CWID','Names','Major','Courses'])    
        for line in self.studentfile:
            self.cwid,self.names,self.major,self.courses = Student.coursestaken()
            pt.add_row([self.cwid,self.names,self.major,self.courses])
        print(pt) 
        
        pt1 = PrettyTable(field_names=['CWID','Names','Department','Courses','Students'])    
        for line in self.instructorfile:
            self.cwidi,self.names,self.department,self.coursestaught = Instructor.coursestaught()
            pt1.add_row([self.cwidi,self.names, self.department,self.coursestaught,self.instructor_coursestaught[course]])
        print(pt1)  
                         
####################################################################################################################################################################################################  
#Unittest AyanaPrettyTable, Filechecker, Students, Instructors, Grades:
      
class StudentTest(unittest.TestCase):
    def test_Student(self):
        #self.assertEqual(Students('mary','yram'),('silent','listen')) 
        self.assertEqual(Student(10130,'Baldwin, C','SFEN'),)  
        
class InstructorTest(unittest.TestCase):
    def test_Instructor(self):
        #self.assertEqual(Instructors('mary','yram'),('silent','listen')) 
        self.assertEqual(Instructor('dormitory','dirtyroom')) 
        
class RepositoryTest(unittest.TestCase):
    def test_RepositoryTest(self):
        #self.assertEqual(Repository('mary','yram'),('silent','listen')) 
        self.assertEqual(Repository('dormitory','dirtyroom')) 
 
####################################################################################################################################################################################################
#Main function results:
def main():
    p = Repository()
    p.ayanaprettytable(self,'C:\Python36\HW09\students.txt','C:\Python36\HW09\instructors.txt','C:\Python36\HW09\grades.txt')
    #ayanaprettytable(self,'C:\Python36\HW09\students.txt','C:\Python36\HW09\instructors.txt','C:\Python36\HW09\grades.txt')
if __name__ == "__main__":
    main()
        