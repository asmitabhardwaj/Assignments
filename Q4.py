import logging
logging.basicConfig(filename="Q4.log",level = logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')
class course():

    def _c_intro(self,c_name,c_teacher):
        try:
            logging.info("Name of the course is {} and teacher is {}".format(c_name,c_teacher))
        except Exception as e:
            logging.info(e)


class course_module(course):

    def _no_of_modules(self,nm):
        try:
            logging.info("Number of mudules in the course  is {}".format(nm))
        except Exception as e:
            logging.info(e)

i=course_module()
print(i._no_of_modules(5))
print(i._c_intro("DE", "Sudhanshu"))







