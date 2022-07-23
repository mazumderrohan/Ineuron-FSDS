#Write a fun which will take input as a dict and give me out as a list of all the values
#even in case of 2 level nesting it should work
import logging
logging.basicConfig(filename = "dict1.log", level = logging.DEBUG, format = "%(levelname)s %(asctime)s %(message)s")


class dict1:

    logging.info("we are accessing class dict 1")

    def dic_to_list(self,d):
        '''function taking input from dict with 2 level nesting & returning list'''
        logging.info("inside level2 nesting function")
        try:
            self.d = d
            self.l = []
            if type (self.d) != dict:
                raise ValueError("only dict input is allowed")
            else:
                logging.info("input provided is dict")
                for i in d.values:
                    if type(i) != dict:
                        self.l.append(i)
                        if type(i) == dict:
                            for j in i.values():
                                self.l.append(j)
            logging.info("values inside dict: %s", self.l)
            return self.l
        except ValueError as v:
            logging.error(v)
            return v
        except Exception as e:
            logging.error(e)
            return e


d = {'k1': '1', 'k2': '2', 'k3': '3', 'k4': {'k4': 'rohan', 'k5': 'mazumder'}}
a = dict1()
a.dic_to_list(d)



