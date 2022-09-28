from flask import Flask, send_from_directory
from flask import request
from flask import render_template
from flask import Response


import os

app = Flask(__name__)
app.config.from_object("project.config.Config")


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/robots.txt', methods=['GET'])
def robots():
    return Response('User-agent: msnbot\nCrawl-Delay: 120\nDisallow: /*.xml$\nDisallow: /mobile/\nUser-Agent: *\nDisallow: /secret_flag\nDisallow: /super_secret_flag\nDisallow: /other_secret_flag\nDisallow: /really_a_secret_flag_i_promise\nUser-Agent: discobot\nCrawl-Delay: 15\nDisallow: /', mimetype='text/plain')

@app.route('/secret_flag', methods=['GET'])
def secret():
    return render_template('notflag.html')

@app.route('/super_secret_flag', methods=['GET'])
def secret2():
    return render_template('notflag.html')

@app.route('/other_secret_flag', methods=['GET'])
def secret3():
    return render_template('notflag.html')

@app.route('/really_a_secret_flag_i_promise', methods=['GET'])
def secret4():
    return render_template('flag.html')

@app.errorhandler(404)
def nopage(e):
    return render_template('noflag.html')

if __name__ == '__main__':
    app.run()
