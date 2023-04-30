from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hola():
    # return "<h1> Hola mundo </h1>"
    mensaje = "Hola mundo con flask"
    return render_template("index.html", msm=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
