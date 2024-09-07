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
            result = first_num + second_num
        elif request.form['action'] == 'subtract':
            result = first_num - second_num
        elif request.form['action'] == 'multiply':
            result = first_num * second_num
        elif request.form['action'] == 'divide':
            if first_num == 0 or second_num == 0:
                return "Division by 0!"
            else:
                result = first_num // second_num
        return render_template('index.html', result=result)
        
    return render_template('index.html')