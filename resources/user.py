from flask import abort, jsonify
from flask_restful import Resource

from model.user_model import User


class UserResource(Resource):
    def get(self):
        users = User.query.all() or abort(204)
        return jsonify({
            "users": [
                user.to_dict() for user in users
            ]
            })

