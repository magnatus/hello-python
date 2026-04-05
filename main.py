from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello, vibe coding on Python 🚀</h1>
    <p>Мое первое веб-приложение на Flask работает.</p>
    """
    
if __name__ == "__main__":
    app.run(debug=True)