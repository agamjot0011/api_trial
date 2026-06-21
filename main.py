from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return {
        "success": True,
        "message": "Hello from Flask API"
    }

if __name__ == "__main__":
    app.run(debug=True)
