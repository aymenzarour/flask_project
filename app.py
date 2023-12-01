from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, welcome to the input form!'

@app.route('/input', methods=['GET', 'POST'])
def input_form():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return f'You entered: {user_input}'
    return render_template('input_form.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
