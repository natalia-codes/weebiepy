# import os
# try:
#     from collections.abc import Mapping
# except ImportError:
#     from collections import Mapping
from flask import Flask, request, jsonify, url_for, send_from_directory
# from flask_jwt_extended import JWTManager



app = Flask(__name__)


# app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET')
# jwt = JWTManager(app)

# base api route


@app.route('/test')
def items():
    return {"itemsTest": ["fist", "second", "third", "etc..."]}

if __name__ == "__main__":
    app.run(debug=True)


