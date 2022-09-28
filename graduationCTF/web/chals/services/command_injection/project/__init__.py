from flask import Flask, send_from_directory
from flask import request
from flask import render_template
from flask import Response
from werkzeug.datastructures import ImmutableMultiDict
import os
import subprocess

app = Flask(__name__)
app.config.from_object("project.config.Config")


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/submit_flag', methods=['POST'])
def validate_flag():
    form_data = request.form
    for flag in form_data.getlist('flag'):
        if ";" in flag:
            return render_template("error.html")
        s = subprocess.Popen(f'./validate_flag {flag}', stdout=subprocess.PIPE, shell=True)
        is_valid = s.communicate()
        data = {"results":is_valid[0].decode().strip()}
    return render_template("result.html", result=data)

if __name__ == '__main__':
    app.run()
