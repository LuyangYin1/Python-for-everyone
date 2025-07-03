from flask import Flask

name_of_webpage = "MyApp"
app = Flask(name_of_webpage)


@app.route("/")
def hello_world():
    return "<html><head><body><h1>1234567890/h1></body></head></html>"


if __name__ == "__main__":
     app.run(debug=True)
