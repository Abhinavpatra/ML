
from click import group
from flask import Flask, render_template, request


app = Flask(__name__)
@app.route("/successfor/<int:score>")
def index(score):
    exp = {"score": score, "res":"FAILED"}
    return render_template("jinja.html", results = exp)

@app.route("/successif/<int:score>")
def successif(score):
    return render_template("if.html",score = score)





@app.route("/dynamic", methods=["GET","POST"])
def dynamic():
    if(request.method=="GET"):
        return render_template("marks.html")
    
    if request.method == "POST":
        science = int(request.form["science"])
        maths = int(request.form["maths"])
        english = int(request.form["english"])
        history = int(request.form["history"])
        geography = int(request.form["geography"])
        average = (science + maths + english + history + geography)/5
        if average > 50: 
            result  ="PASSED"
        else:
            result = "FAILED"
        return render_template("output.html", result = result)
    


if __name__=="__main__":
    app.run(debug=True)


