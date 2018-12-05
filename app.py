from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def loginpage():
    return render_template("Login_Page.html")

@app.route("/Main Page")
def mainpage():
    return render_template("Main Page.html")

@app.route("/CCTV")
def cctv():
    return render_template("CCTV.html")


@app.route("/CCTV_1")
def cctv1():
    return render_template("CCTV_1.html")


@app.route("/CCTV_2")
def cctv2():
    return render_template("CCTV_2.html")


@app.route("/CCTV_3")
def cctv3():
    return render_template("CCTV_3.html")


@app.route("/CCTV_4")
def cctv4():
    return render_template("CCTV_4.html")


if __name__ == "__main__":
    app.run()

