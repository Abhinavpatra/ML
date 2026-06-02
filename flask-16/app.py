from flask import Flask

app = Flask(__name__)
'''
multi line
'''

@app.route("/")
def index():
    return "Hello World, welcome!"


@app.route("/index")
def diff_index():
    return "Index route"

if __name__ == '__main__':
    app.run(debug = True)

