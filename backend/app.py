from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
from flask import send_from_directory
import os
# n7adhrou app
app = Flask(__name__)

#nkhaliwh yconecti bl cors
CORS(app)
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)
def serve_static(path):
    return send_from_directory('../frontend', path)
# njarbou server yekhdem w le
@app.route('/api/test', methods=['GET'])
def test_server():
    return jsonify({
        "status": "success",
        "message": "Flask server is up and running!"
    })
@app.route('/api/sites', methods=['GET'])
def get_sites():
    # 1. نفتح اتصال مع قاعدة البيانات
    conn = sqlite3.connect('database.db')
    
    # هذه الخطوة مهمة لكي تعود البيانات بأسماء الأعمدة (id, name, description) بدلاً من مجرد أرقام
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()
    
    # 2. نطلب من قاعدة البيانات كل شيء في جدول sites
    cursor.execute("SELECT * FROM sites")
    rows = cursor.fetchall()
    
    # 3. نحول البيانات إلى قائمة (List) لكي يقبلها JSON
    sites_list = []
    for row in rows:
        sites_list.append(dict(row))
        
    # 4. نغلق الاتصال
    conn.close()
    
    # 5. نرسل البيانات
    return jsonify(sites_list)
# server
if __name__ == '__main__':
    app.run(debug=True)