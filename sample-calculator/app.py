from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        expression = request.form['display']
        try:
            result = eval(expression)
        except Exception as e:
            result = 'Error'
        return render_template('index.html', result=result, expression=expression)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
