from random import randint
import time
from flask import Flask
app = Flask(__name__)


def getOutput():
    start_time = time.time()
    x = randint(0,100)
    y  = randint(0,100)
    print("{} + {} = ?".format(x,y))
    if int(input())==x+y:
        print("Correct")
        print("--- %s seconds" % int(time.time() - start_time))
    else:
        print("Wrong")
        print("--- %s seconds" % int(time.time() - start_time))


while 1:

    getOutput()
app.run()


# testing remote git