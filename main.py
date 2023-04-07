from flask import Flask, render_template, request
from sheets import *
# https://docs.google.com/spreadsheets/d/1VYn5yJwx5jFUe9lJpVJrVJEPiLRhHrpoBBGGybAh4Vg/edit#gid=0
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

@app.route('/', methods =["GET", "POST"])
def index():
    data = getAllData()
    if request.method == "POST":
        col = request.form.get("column")
        row = request.form.get("row")
        value = request.form.get("data")
        addCell(row,col,value)
        data = getAllData()
        return render_template("index.html", data=data)
    return render_template("index.html", data=data)
@app.route('/', methods=["POST"])
def fetchCell():
    col = request.form.get("column")
    row = request.form.get("row")
    cell = fetchCell(row,col)
    


if __name__=='__main__':
    app.run(debug = True)