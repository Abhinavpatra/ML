from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return"<html> <h1>Inside h1<h1> <h2>Inside h2<h2> </html>"



@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/form", methods = ["GET","POST"])
def form():
    if(request.method == 'POST'):
        name = request.form['name']
        return f'<h1>hello {name}</h1>'
    return render_template("form.html")


@app.route("/successfor/<int:score>")
def successres(score):
    if(score > 50):
        res = "SUCCESS"
    else:
        res = "FAILED"
    exp = {"score":score,"res":res}
    
    return render_template("result.html", results = exp)



if __name__ == "__main__":
    app.run(debug = True)

