from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def prediction():
    if request.method == "POST":
        model = joblib.load("models/irisLinearSVC.sav")
        sLen = float(request.form.get("sLen"))
        sWid = float(request.form.get("sWid"))
        pLen = float(request.form.get("pLen"))
        pWid = float(request.form.get("pWid"))

        y = model.predict([[sLen, sWid, pLen, pWid]])
        return render_template("main.html", y=y, sLen=str(sLen), sWid=str(sWid), pLen=str(pLen), pWid=str(pWid) )
    else:
        return render_template("main.html", y=4)


if __name__ == '__main__':
    app.run(debug=True)

