from datetime import datetime, time
from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    # var
    count = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    # time
    now = datetime.now()
    date =now.strftime("%c")
    # prints..
    print(request.form)
    print(date)
    print ('count:', count)
    print ('charging', request.form['first_name'], request.form['last_name'], 'for', count, 'fruit(s)')
    return render_template("checkout.html" , count=count, date=date)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    