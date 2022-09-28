from flask import Flask, send_from_directory
from flask import request
from flask import render_template
from flask import Response
from flask import make_response

import os

app = Flask(__name__)
app.config.from_object("project.config.Config")


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    form_data = request.form
    for user in form_data.getlist('nm'):
        res = make_response(f"<h1>Welcome {user}</h1>")
        res.set_cookie('flag', 'fitsec{c00k!3s_r_d3l!c!0us}')
        return res


if __name__ == '__main__':
    app.run()
