import logging
logging.basicConfig(filename="Q5.log",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s %(message)s')
from Q4 import course
# abstract base class
logging.info(course)

class Data_Science(course):
    def course_duration(self):
        try:
            logging.info("Course duration for Data Science course is 370 days")
        except Exception as e:
            logging.info(e)
#  overriding abstract method course_duration
class Big_Data(course):
    def course_duration(self):
        try:
            logging.info("Course duration for Big Data course is 3 Months")
        except Exception as e:
            logging.info(e)
#  overriding abstract method course_duration
class Data_Engineer(course)  :
    def course_duration(self):
        try:
            logging.info("Course duration for  Data Engg course is 5 Months")
        except Exception as e:
            logging.info(e)
#  overriding abstract method course_duration


D= Data_Science()
D.course_duration()

B = Big_Data()
B.course_duration()

DE = Data_Engineer()
DE.course_duration()



#This code covers inheritance,abstraction,polymorphism,method overriding
