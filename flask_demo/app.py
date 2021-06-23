from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    try:

        if (request.method=='POST'):
            operation=request.form['operation']
            num1=int(request.form['num1'])
            num2 = int(request.form['num2'])


            if(operation=='add'):
                r=num1+num2
                result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
            if (operation == 'subtract'):
                r = num1 - num2
                result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            if (operation == 'multiply'):
                r = num1 * num2
                result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            if (operation == 'divide'):
                r = num1 / num2
                result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
            return render_template('results.html',result=result)
    except ValueError:
            result = 'Not an integer value !  Try it again'
            return render_template('results.html',result = result)

@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    try:

        if (request.method=='POST'):
            operation=request.json['operation']
            num1=int(request.json['num1'])
            num2 = int(request.json['num2'])
            if(operation=='add'):
                r=num1+num2
                result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
            if (operation == 'subtract'):
                r = num1 - num2
                result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            if (operation == 'multiply'):
                r = num1 * num2
                result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            if (operation == 'divide'):
                r = num1 / num2
                result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
            return jsonify(result)
    except ValueError:
        result = 'Not an integer value !  Try it again'
        return jsonify(result)


@app.route('/even_odd',methods=['POST']) # for calling the API from Postman
def find_Even_Odd(): # function 1
    try:
        if(request.method == 'POST'):
            num = int(request.json['num'])
            if num % 2 == 0:
                result = "Entered number is Even"
                return jsonify(result)
            else:
                result = "Entered number is Odd"
                return jsonify(result)
    except ValueError:
        result = 'Not a valid value'
        return jsonify(result)


@app.route('/swap',methods=['POST'])
def swap_two_nums(): # function 2
    try:
        if(request.method == 'POST'):
            num1 = int(request.json['num1'])
            num2 = int(request.json['num2'])
            temp = num1
            num1 = num2
            num2 = temp
            result = 'The new value of num1 and num2 after swaping is ' + str(num1) +','+ str(num2)
            return jsonify(result)
    except ValueError:
        result = 'Enter the valid number'
        return jsonify(result)


@app.route('/reverse',methods=['POST'])
def reverse_num():
    try:
        if(request.method == 'POST') :
            num = int(input(request.json['num']))
            reversed_num = 0
            while num != 0:
                rem = num % 10
                reversed_num = reversed_num * 10  + rem
                num //= 10
            result = ' Reversed number is ' + str(reversed_num)
            return jsonify(result)
    except:
        result = 'Please Enter valid number'
        return jsonify(result)

if __name__ == '__main__':
    app.run()
