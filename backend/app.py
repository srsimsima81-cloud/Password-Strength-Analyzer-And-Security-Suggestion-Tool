from flask import Flask, jsonify, request, send_from_directory
from pathlib import Path
from services.password_analyzer import analyze_password
from services.password_generator import generate_password
from models.database import init_db, record_analysis, get_dashboard_stats, get_weakness_stats

BASE_DIR=Path(__file__).resolve().parent.parent
DB_PATH=BASE_DIR/'data'/'analytics.db'; COMMON_PASSWORDS=BASE_DIR/'data'/'common_passwords.txt'
app=Flask(__name__, static_folder=str(BASE_DIR/'frontend'), static_url_path='')
init_db(DB_PATH)

@app.get('/')
def index(): return send_from_directory(BASE_DIR/'frontend','index.html')

@app.post('/api/analyze')
def api_analyze():
    data=request.get_json(silent=True) or {}; password=data.get('password','')
    if not isinstance(password,str): return jsonify(error='Password must be a string.'),400
    if len(password)>4096: return jsonify(error='Input exceeds the safety limit of 4096 characters.'),413
    result=analyze_password(password,data.get('context') or {},COMMON_PASSWORDS,data.get('policy') or {})
    m=result['metrics']; record_analysis(DB_PATH,result['score'],result['classification'],m['length'],m['unique_character_ratio'],len(result['findings']))
    return jsonify(result)

@app.get('/api/dashboard/stats')
def dashboard(): return jsonify(get_dashboard_stats(DB_PATH))
@app.get('/api/analytics/weaknesses')
def weaknesses(): return jsonify(get_weakness_stats(DB_PATH))

@app.post('/api/generate-password')
def generator():
    data=request.get_json(silent=True) or {}
    try: length=int(data.get('length',20))
    except (TypeError,ValueError): return jsonify(error='Length must be an integer.'),400
    if length not in (16,20,24): return jsonify(error='Length must be 16, 20, or 24.'),400
    try: pw=generate_password(length,bool(data.get('uppercase',True)),bool(data.get('lowercase',True)),bool(data.get('numbers',True)),bool(data.get('symbols',True)))
    except ValueError as e: return jsonify(error=str(e)),400
    return jsonify(password=pw)

@app.get('/api/health')
def health(): return jsonify(status='ok')

if __name__=='__main__': app.run(host='127.0.0.1',port=5000,debug=False)
