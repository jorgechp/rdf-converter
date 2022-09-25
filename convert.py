import tempfile

import csv_converter

from flask import Blueprint, request
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename


conversion_router = Blueprint('convert', __name__)


@conversion_router.route("/csv", methods=['POST'])
def convert_csv():
    file: FileStorage = request.files["file"]
    query: FileStorage = request.files["query"]
    is_tab: bool = bool(request.form.get("is_tab")) if "is_tab" in request.form else False

    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = temp_dir + '/' + secure_filename(file.filename)
        query_path = temp_dir + '/' + secure_filename(query.filename)
        file.save(file_path)
        query.save(query_path)

        output = csv_converter.convert(file_path, query_path, is_tab)

        return output, 200, {'Content-Type': 'application/octet-stream; charset=utf-8'}
