import logging
logging.basicConfig(filename="Q2.log",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s %(message)s')
from datetime import datetime
# importing datetime from datetime module
class ineuron_Students:

  # creating a private method username in class ineuron_Students
    def __username(self,name,mail_id):
        logging.info("username of student {}  is {}".format(name ,mail_id))

class course_type:

# creating a protected method in class course type
    def _course_discount(self,course_name,course_fee):
        try:
            logging.info("Course discount  for {} course is {}".format(course_name,course_fee/10) )
        except Exception as e:
            logging.exception(e)


class Student_Batch(ineuron_Students,course_type):

    def __init__(self,Batch_name,Batch_type):
        self.Batch_name = Batch_name
        self.Batch_type = Batch_type

#creating public method Batch_start_date in class Student_Batch
    def Batch_start_date(self):
        try:
            logging.info("Batch start date  for {} {} Batch is {}".format(self.Batch_name,self.Batch_type,datetime.now().date()))
        except Exception as e:
            logging.info(e)

obj1=Student_Batch("FSDS Bootcamp","Live Class")
print(obj1.Batch_start_date())
print(obj1._course_discount("FSDS",1000))
print(obj1._ineuron_Students__username("Ram","ram@gmail.com"))

#This code shows class object,constructor,inheritance,private,public,protected,package and modules

