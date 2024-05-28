from flask import Flask, request, jsonify, send_from_directory
import sqlite3
import os

app = Flask(__name__, static_folder='.')

def get_faq(language):
    conn = sqlite3.connect('faq1.db')
    c = conn.cursor()
    if language == 'ru':
        c.execute("SELECT id, question_ru, answer_ru FROM faq1")
    else:
        c.execute("SELECT id, question_kg, answer_kg FROM faq1")
    faq_data = c.fetchall()
    conn.close()
    return faq_data

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/faq1', methods=['GET'])
def faq():
    language = request.args.get('language')
    if language not in ['ru', 'kg']:
        return jsonify({"error": "Invalid language"}), 400
    faq_data = get_faq(language)
    return jsonify(faq_data)

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True)
