from random import randint
import time
from flask import Flask,render_template , request
app = Flask(__name__)

@app.route('/main',methods=["GET","POST"])
def homepage():
    if request.method=='GET':
        x = randint(10,99)
        y = randint(10,99)
        result = None
        # if int(request.form["x"])+int(request.form["y"]==int(request.form["result"])):
            # result = "Correct"
        # else:
            # result = "Incorrect"
        return render_template('calculate.html.jinja',x=x,y=y)
    else:
        return render_template('calculate.html.jinja',x=x,y=y,result=x+y)

def getOutput():
    start_time = time.time()
    x = randint(10,100)
    y  = randint(10,100)
    time_taken = int(time.time() - start_time)
    output = x+y
    return x,y,output,time_taken


# while 1:

    # getOutput()
app.run(debug=True  )


# testing remote git
#testing git pull command
