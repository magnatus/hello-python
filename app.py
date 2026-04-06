from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

answers = []

QUESTIONS = [
    {"id": 1, "text": "Как вас зовут?"},
    {"id": 2, "text": "Сколько вам лет?"},
    {"id": 3, "text": "Какой ваш любимый язык программирования?"},
    {"id": 4, "text": "Что вам нравится в разработке?"},
    {"id": 5, "text": "Какую задачу вы хотели бы решить с помощью кода?"},
]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "").strip() or "Гость"
        return render_template("greet.html", name=name)
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/questionnaire")
def questionnaire():
    return render_template("questionnaire.html")

@app.route("/questions")
def questions():
    return jsonify(QUESTIONS)

@app.route("/answers", methods=["POST"])
def submit_answers():
    data = request.get_json()
    if data:
        answers.append(data)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)