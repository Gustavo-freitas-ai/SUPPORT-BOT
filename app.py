from flask import Flask, render_template, request
from bot import get_bot_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bot_response = ""

    if request.method == "POST":
        user_message = request.form["message"]
        bot_response = get_bot_response(user_message)

    return render_template("index.html", response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)