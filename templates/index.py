from flask import Flask, render_template
from Saleapp import app
# app = Flask(__name__)
@app.route("/")
#test git
def index():
     return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
