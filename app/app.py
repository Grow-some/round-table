from flask import Flask, request, jsonify, render_template
import os
import whisper
from datetime import datetime

app = Flask(__name__)

# サーバプログラムの動作ディレクトリ配下に raw_sound フォルダを作成
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'raw_sound')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 保存ファイル名にタイムスタンプを付与
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    save_path = os.path.join(UPLOAD_FOLDER, f'{timestamp}_{file.filename}')
    file.save(save_path)
    return jsonify({'message': f'File {file.filename} successfully uploaded to {UPLOAD_FOLDER}'}), 200

@app.route('/')
def index():
    return render_template('index.html')  # HTMLページを提供


if __name__ == '__main__':
    app.run(debug=True)
