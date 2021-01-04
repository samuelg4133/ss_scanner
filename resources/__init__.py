from flask import Blueprint
from flask_restful import Api

from .upload_file import UploadFile
from .user import UserResource

bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(bp)


def init_app(app):
    api.add_resource(UploadFile, "/upload")
    api.add_resource(UserResource, '/user')
    app.config['UPLOAD_FOLDER'] = UploadFile.UPLOAD_FOLDER
    app.register_blueprint(bp)
