import random
import time
numexecutions = int(input('Enter how many sets of numbers is to  be generated .... '))
def some_number():
        random_number = random.randint(0,100)
        return random_number
def timecalc():
    print numexecutions
    for i in range(numexecutions):
        timer = random.random()
        start = time.time()
        for x in range(10):
            print some_number()
        while time.time() - start < timer:
            end = time.time()
            elapsedtime = end - start
        print 'elapsed time is %f' %elapsedtime
timecalc()
