from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'images')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('uploads.html')
    else:
        img_file = request.files.get('pic')
        file_name = img_file.filename
        # 文件名的安全转换
        filename = secure_filename(file_name)
        # 保存文件
        img_file.save(os.path.join(UPLOAD_PATH, filename))
        return render_template('default.html')


if __name__ == '__main__':
    app.run(debug=True)

