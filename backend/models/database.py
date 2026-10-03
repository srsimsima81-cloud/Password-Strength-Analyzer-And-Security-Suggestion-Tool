import sqlite3
from pathlib import Path
def connect(path):
    Path(path).parent.mkdir(parents=True,exist_ok=True); c=sqlite3.connect(path); c.row_factory=sqlite3.Row; return c
def init_db(path):
    c=connect(path); c.execute('''CREATE TABLE IF NOT EXISTS analyses(analysis_id INTEGER PRIMARY KEY AUTOINCREMENT,score INTEGER NOT NULL,classification TEXT NOT NULL,password_length INTEGER NOT NULL,unique_character_ratio REAL NOT NULL,weakness_count INTEGER NOT NULL,created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)'''); c.commit(); c.close()
def record_analysis(path,score,classification,password_length,unique_character_ratio,weakness_count):
    c=connect(path); c.execute('INSERT INTO analyses(score,classification,password_length,unique_character_ratio,weakness_count) VALUES(?,?,?,?,?)',(score,classification,password_length,unique_character_ratio,weakness_count)); c.commit(); c.close()
def get_dashboard_stats(path):
    c=connect(path); rows=c.execute('SELECT classification,COUNT(*) count FROM analyses GROUP BY classification').fetchall(); avg=c.execute('SELECT AVG(score) average FROM analyses').fetchone()['average']; total=c.execute('SELECT COUNT(*) total FROM analyses').fetchone()['total']; lengths=c.execute('SELECT password_length length,COUNT(*) count FROM analyses GROUP BY password_length ORDER BY password_length').fetchall(); scores=c.execute('SELECT score FROM analyses ORDER BY analysis_id').fetchall(); c.close()
    d={'VERY WEAK':0,'WEAK':0,'MODERATE':0,'STRONG':0,'VERY STRONG':0}
    for r in rows:d[r['classification']]=r['count']
    return {'total_analyses':total,'average_score':round(avg or 0,2),'strength_distribution':d,'length_distribution':[dict(r) for r in lengths],'score_distribution':[r['score'] for r in scores]}
def get_weakness_stats(path):
    c=connect(path); rows=c.execute("""SELECT CASE WHEN weakness_count=0 THEN 'No detected weakness' WHEN weakness_count=1 THEN '1 weakness' WHEN weakness_count BETWEEN 2 AND 3 THEN '2-3 weaknesses' ELSE '4+ weaknesses' END category,COUNT(*) count FROM analyses GROUP BY category""").fetchall(); c.close(); return [dict(r) for r in rows]
