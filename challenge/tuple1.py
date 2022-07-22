import logging
logging.basicConfig(filename = "tuple1.log", level = logging.DEBUG, format = "%(levelname)s %(asctime)s %(message)s")

class tuple1:

    logging.info("we are accessing tuple1 class")

    def addition (self, *x) :
        """find the sum of all integers inside a tuple"""
        try:
            self.x = x
            self.n = 0
            for i in x:
                if type(i) == int:
                    self.n += i
                    logging.info("sum of all items inside tuple: %s", self.n)
                    return str(self.n)
        except Exception as e:
            logging.exception(e)
            return e


x = (100, 200, 300, 400, 500, 600, 700, 800, 900)
a = tuple1()
print(a.addition(x))


