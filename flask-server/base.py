import  os
from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt, \
    unset_jwt_cookies, jwt_required, JWTManager

api = Flask(__name__)

api = Flask(__name__)

api.config["JWT_SECRET_KEY"] = "change"
jwt = JWTManager(api)

@api.route('/token', methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return {"msg": "Wrong email or password"}, 401

    access_token = create_access_token(identity=email)
    response = {"access_token":access_token}
    return response

@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Natalia",
        "about" :"testestrest",
        "more": "test",
        "last": "tedfgtdfgst"
    }

    return response_body

