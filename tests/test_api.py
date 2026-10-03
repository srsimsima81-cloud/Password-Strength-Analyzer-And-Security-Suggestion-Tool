import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'backend'))
from app import app
def test_health(): assert app.test_client().get('/api/health').status_code==200
def test_api_does_not_echo_password():
 secret='SyntheticApiDemo!9283'; r=app.test_client().post('/api/analyze',json={'password':secret}); assert r.status_code==200 and secret not in str(r.get_json())
def test_generator_api():
 r=app.test_client().post('/api/generate-password',json={'length':16}); assert r.status_code==200 and len(r.get_json()['password'])==16
