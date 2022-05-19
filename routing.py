from flask import Flask
app = Flask(__name__)

@app.route('/a')
def a():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def say(name):
    return "Hi " + name + "!"

@app.route('/repeat/<int:num>/<name>')
def repeat(num, name):
    return f"{name * num}"

if __name__=="__main__":
    app.run(debug=True)
