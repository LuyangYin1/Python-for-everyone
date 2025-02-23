from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<html><head><body><h1>welcome to python for everyone class</h1></body></head></html>"

if __name__ == "__main__":
    app.run(debug=True)