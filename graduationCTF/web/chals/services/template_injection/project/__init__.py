from flask import Flask, abort, request, render_template_string
import jinja2, re, hashlib
from flask import render_template

app = Flask(__name__)
app.secret_key = b'fitsec{j!nj4_!s_vuln3r4bl3}'


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def no_filter():
        
        payload = request.form.get('password')

        template = '''
        <!DOCTYPE html>
        <html>
          <head>
            <title>No Filter</title>
          </head>
          <body>
            <p>''' + "Hello " + payload + '''</p>
            <p>Welcome to my super secure website. Pls don't steal my flags :(</p>
          </body>
        </html>'''

        return render_template_string(template)

if __name__ == '__main__':
        app.run()


