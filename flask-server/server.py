from flask import Flask


app = Flask(__name__)

# base api route


@app.route('/')
def home():
    return{
        "items": [
            "fist", "second", "third", "etc..."
        ]
    }

if __name__ == "__main__":
    app.run(debug=True)