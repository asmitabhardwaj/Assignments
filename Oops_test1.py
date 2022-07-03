#l=[[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,6,7,5,4,5]),{'k1':"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron","data science"]]
#q3: Try to extract all the list entity
#q6: Try to extract all the neumerical data it may be a part of dict key and values
#q7: Try to give summation of all the neumerical data
#q8: Try to filter out all the odd values out all neumeric data which is part of a list
#q12: Try to filter out all the string data
#q11:Try to find out the number of keys in dict element
#q15. Try to unwrap all the collection inside collection and create a flat list
l=[[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,6,7,5,4,5]),{'k1':"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron","data science"]]

import logging
logging.basicConfig(filename="List_oops.log",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s %(message)s')
l=[[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,6,7,5,4,5]),{'k1':"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron","data science"]]

class List:

    def entity(self,l):
        logging.info("This function will find all the list entity")
        try:
            for i in l :
                if type(i) == list:
                    logging.info("The list entity is %s", i)
        except Exception as e:
            logging.exception(e)



    def odd(self,l):
        logging.info("This function is to be used to find the odd numbers of the list")
        try:
            for i in l:
                if type(i) == list:
                    for j in i:
                        if type(j) == int and j % 2 == 1:
                            logging.info(j)
        except Exception as e:
            logging.info(e)

    def string_data(self,l):
        try:
            for i in l:
                if type(i) == list or type(i) == tuple or type(i)== set:
                    for j in i :
                        if type(j) == str:
                            logging.info(j)

                if type(i) == dict:
                    for k,v in i.items():
                        if type(k) == str:
                            logging.info(k)
                        if type(v) == str:
                            logging.info(v)
        except Exception as e:
            logging.info(e)

    def sum1(self,l):
        logging.info("This function will find out the sum of all the integers from list l")
        ls=[]
        try:
            for i in l :
                if type(i) == list or type(i) == tuple or list(i) == set:
                    for j in i :
                        if type(j) == int:
                         ls.append(j)



                if type(i) == dict:
                    for k,v in i.items():
                        if type(k) == int:
                            ls.append(k)
                        if type(v) == int:
                            ls.append(v)

            logging.info("All the numerical data can be found in list %s", ls)
            logging.info("Sum of all the integers of list l is %s ", sum(ls))
            logging.info("After unwrapping flat list %s", ls)
        except Exception as e:
            logging.info(e)





l=[[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,6,7,5,4,5]),{'k1':"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron","data science"]]
l1=List()
l3=List()
l4=List()
l5=List()
logging.info(l1.entity(l))
logging.info(l3.odd(l))
logging.info(l4.string_data(l))
logging.info(l5.sum1(l))


class Tuple:

    def entity(self,l):
        logging.info("This function will find all the list entity")
        try:
            for i in l :
                if type(i) == tuple:
                    logging.info("The list entity is %s", i)
        except Exception as e:
            logging.exception(e)

l12 = Tuple()
logging.info(l1.entity(l))

class Dict:

    def entity(self,l):
        logging.info("This function will find all the list entity")
        try:
            for i in l :
                if type(i) == dict:
                    logging.info("The list entity is %s", i)
        except Exception as e:
            logging.exception(e)

# q11:Try to find out the number of keys in dict element
    def key1(self,l):
        try:
            for i in l:
                if type(i) == dict:
                    logging.info("Count of all the keys of list l is %s", len(i.keys()))
        except Exception as e:
            logging.info(e)

l13 = Dict()
l14=  Dict()
logging.info(l13.entity(l))
logging.info(l14.key1(l))





