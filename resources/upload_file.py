from datetime import datetime

import img2pdf
from flask import jsonify, request
from flask_restful import Resource, reqparse
import os

path = os.getcwd()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'svg'}
parser = reqparse.RequestParser();
parser.add_argument("username")


def allowed_files(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class UploadFile(Resource):
    UPLOAD_FOLDER = os.path.join(path, 'uploads')

    @staticmethod
    def post():
        if 'files' not in request.files:
            res = jsonify({
                "message": "No file part"
            })
            res.status_code = 400
            return res
        files = request.files.getlist("files")
        images = []
        for file in files:
            if files and allowed_files(file.filename):
                images.append(file)
        user_args = parser.parse_args()
        with open(os.path.join(UploadFile.UPLOAD_FOLDER, user_args['username'],
                               "digitalized"+datetime.now().strftime("%d%m%Y%H%M%S") + ".pdf"), "wb") as f:
            f.write(img2pdf.convert(images))
            res = jsonify({
                "status": True,
                "message": "File(s) successfully uploaded."
            })

            res.status_code = 201
            return res
