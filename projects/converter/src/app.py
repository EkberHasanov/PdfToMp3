from flask import Flask

app = Flask(__name__)

@app.route('/')
def index() -> tuple:
    return "hello", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
