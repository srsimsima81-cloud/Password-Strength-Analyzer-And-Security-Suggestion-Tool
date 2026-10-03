import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'backend'))
from services.password_analyzer import analyze_password
from services.password_generator import generate_password
from services.pattern_detector import detect_sequences,detect_keyboard_patterns,detect_repetition,detect_predictable_structure
from services.context_checker import check_personal_context
from services.length_analyzer import analyze_length
COMMON=Path(__file__).resolve().parents[1]/'data'/'common_passwords.txt'
def test_empty(): assert analyze_password('',common_password_file=COMMON)['score']==0
def test_common():
 r=analyze_password('123456',common_password_file=COMMON); assert r['classification']=='VERY WEAK' and r['metrics']['common_password']
def test_patterns():
 assert detect_sequences('abc1234')['matches']; assert detect_keyboard_patterns('qwerty')['matches']; assert detect_repetition('aaaaaaaa')['matches']; assert detect_predictable_structure('welcome123')['matches']
def test_context(): assert len(check_personal_context('Alex@1998',{'first_name':'Alex','birth_year':'1998'})['overlap'])==2
def test_length(): assert analyze_length('abc')['guidance']=='Very short'
def test_generator():
 p=generate_password(20); assert len(p)==20 and any(c.isupper() for c in p) and any(c.islower() for c in p) and any(c.isdigit() for c in p) and any(not c.isalnum() for c in p)
def test_result_does_not_echo_password():
 secret='SyntheticOnly!4827'; r=analyze_password(secret,common_password_file=COMMON); assert secret not in str(r); assert 'password' not in r
