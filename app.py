from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["GET","POST"])
def user_feedback():
    if request.method == "GET":
        return "Nothing to see here"
    if request.method == "POST":
        info = request.form
        print(info)
        return f"Thanks"

if __name__=="__main__":
    app.run(debug=True)