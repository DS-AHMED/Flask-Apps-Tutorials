from flask import Flask, request
from timestwo import timestwo
app = Flask(__name__)


@app.route('/')
def double():
    number = request.args.get('number', type = int)
    a = timestwo(number)
    return "{}".format(a)

if __name__ == "__main__":
    app.run( debug = True , port = 8080)
