from random import randint
import time
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/main')
def homepage():
    x = randint(0,99)
    y = randint(0,99)
    return render_template('calculate.html.jinja',x=x,y=y)

def getOutput():
    start_time = time.time()
    x = randint(0,100)
    y  = randint(0,100)
    time_taken = int(time.time() - start_time)
    output = x+y
    return x,y,output,time_taken


# while 1:

    # getOutput()
app.run(debug=True  )


# testing remote git
#testing git pull command
