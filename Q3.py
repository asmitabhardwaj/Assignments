import logging
logging.basicConfig(filename="Q3.log",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s %(message)s')
from Q2 import ineuron_Students

class student:
    def SOI(self,subject_name):
        try:
            logging.info("Subject of interest of student is {}".format(subject_name))
        except Exception as e:
            logging.info(e)
    def intro(self):
        try:
            logging.info("These students are learning from online program" )
        except Exception as e:
            logging.info(e)

class Kids_Neuron(student):

    def intro(self):
        try:
            logging.info("Kids neuron is to upskill the kids")
        except Exception as e:
            logging.info(e)

objs = student()
objK = Kids_Neuron()
print(objK.SOI("Big Data"))
print(objK.intro())
print(objs.intro())

#we have implement the method intro() in the child class and parent class which shows method overriding
#This program shows class ,objects ,polymorphism,method-overriding,inheritance & import
