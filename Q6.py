import logging
logging.basicConfig(filename="Q6.log",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s %(message)s')
class Student_details:
    name = "Max" #public variable
    _age = 24    #protected variable
    _job = "Developer" #protected variable

class intern(Student_details):
    #constructor
    def __init__(self):
        logging.info(self.name)
        logging.info(self._age)
        logging.info(self._job)

obj = intern()

logging.info("Name of Student is {}".format(obj.name))
logging.info("Age of Student is {}".format( obj._age))
logging.info("job of student is {} ".format(obj._job))

#private members cant be accessed from outside class,that's making it as protected
#This code shows inheritance public,private,protected,encapsulations,class,object,constructor





