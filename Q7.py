import logging
logging.basicConfig(filename="Q7.log",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s %(message)s')

from datetime import datetime
class Company:
    def company_type(self):
        try:
            logging.info("Company is a Product Based ")
        except Exception as e:
            logging.info(e)
    def revenue(self):
        try:
            logging.info("Annual Revenue of company is 5 Billion USD")
        except Exception as e:
            logging.info(e)

class Job(Company):
    def Job_Role(self):
        try:
            logging.info("Job Role is Developer")
        except Exception as e:
            logging.info(e)
    def Job_hiring(self):
        try:
            logging.info("Job hiring date will be {}  ".format(datetime.now().date()))
        except Exception as e:
            logging.info(e)

class Employee(Job):
    def intro(self,emp_name,emp_id,emp_mail):
        try:
            logging.info("Name of employee is {}, id = {} and mail = {}" .format(emp_name,emp_id,emp_mail))
        except Exception as e:
            logging.info(e)

E=Employee()
E.intro("Harry",344,"acd@gmail.com")
logging.info(E.Job_hiring())
E.Job_Role()
E.company_type()