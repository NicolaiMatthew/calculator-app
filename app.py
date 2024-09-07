from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def hello_world():
    if request.method == "POST":
        # Getting first number
        first_num = request.form.get('fnum')
        # Getting second number
        second_num = request.form.get('snum')
        # Adding the number together
        sum = int(first_num) + int(second_num)
        return "Your total is: %d" % sum
        
    return render_template('index.html')