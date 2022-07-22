import logging
logging.basicConfig(filename="str1.log", level = logging.DEBUG, format="%(levelname)s %(asctime)s %(message)s")


class str1:

    logging.info("we are accessing class str1")

    def split_str(self, S) :
        """"split a string after conversion of entire string in uppercase"""
        try:
            self.S = S
            S1 = S.upper()
            S2 = S1.split(' ')
            logging.info("string in uppercase: %s", S2)
            return S2
        except Exception as e:
            logging.exception(e)
            return e


    def reverse_string(self, l):
        logging.info("the string entered by user: %s", l)
        try:
            logging.info("extracting data from index one to index 300 with a jump of 3")
            self.l = l
            l1 = l[1:300:3]
            logging.info(l1)
            return l1
        except Exception as e:
                logging.exception(e, "please enter a string")


    def length (self, S):
        '''this is my function for finding length of a string'''
        try:
            self.S = S
            S1 = len(S)
            logging.info('length of string is: %s', S1)
            return  str(S1)
        except Exception as e:
            logging.exception(e, 'please enter a string')


S = "this is My First Python programming class and i am learNING python string and its function"
a = str1()

#print(a.split_str(S))
#print(a.length(S))
print(a.reverse_string(S))