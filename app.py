from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def hello_world():
    if request.method == "POST":
        # Getting first number
        first_num = int(request.form.get('fnum'))
        # Getting second number
        second_num = int(request.form.get('snum'))
        # Conditional for button press
        if request.form['action'] == 'add':
            sum = first_num + second_num
            return "Result : %d" % sum
        elif request.form['action'] == 'subtract':
            difference = first_num - second_num
            return "Restult : %d" % difference
        elif request.form['action'] == 'multiply':
            product = first_num * second_num
            return "Result : %d" % product
        elif request.form['action'] == 'divide':
            if first_num == 0 or second_num == 0:
                return "Division by 0!"
            else:
                quotient = first_num // second_num
                return "Result: %d" % quotient
        return "Your total is: %d" % sum
        
    return render_template('index.html')