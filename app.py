from flask import Flask, render_template, request, jsonify
from sheets import *
# https://docs.google.com/spreadsheets/d/1VYn5yJwx5jFUe9lJpVJrVJEPiLRhHrpoBBGGybAh4Vg/edit#gid=0
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

appData = ""

@app.route('/', methods =["GET", "POST"])
def index():
    data = getAllData()
    if request.method == "POST" and 'update_cell' in request.form:
        function = request.form.get("function")
        col = request.form.get("column")
        row = request.form.get("row")
        value = request.form.get("data")
        addCell(row,col,value)
        data = getAllData()
        return render_template("index.html", data=data)
    elif request.method == "POST" and 'retrieve_cell' in request.form:
        row_num = int(request.form.get("row"))
        col_num = int(request.form.get("column"))
        cell_value = returnCell(row_num, col_num)
        return render_template('index.html', data=data, cell_value=cell_value, row_num=row_num, col_num=col_num)
    elif request.method == "POST" and 'delete_row' in request.form:
        row_num = int(request.form.get("row"))
        deleteRow(row_num)
        data=getAllData()
        return render_template('index.html', data=data, delete_value=row_num)
    else:
        return render_template("index.html", data=data)


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)