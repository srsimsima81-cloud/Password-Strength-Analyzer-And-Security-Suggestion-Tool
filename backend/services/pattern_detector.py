import re
KEYBOARD_PATTERNS=('qwerty','asdf','zxcv','qwerty123','asdfgh','yuiop','hjkl','zxcvbnm')
COMMON_WORDS={'password','welcome','admin','letmein','hello','football','monkey','dragon','login','user','secret','summer','winter','college','company'}
def detect_sequences(password,minimum=4):
    s=password.casefold(); matches=[]
    for i in range(len(s)-minimum+1):
        x=s[i:i+minimum]
        if len(x)==minimum and x.isalnum() and (all(ord(x[j])+1==ord(x[j+1]) for j in range(minimum-1)) or all(ord(x[j])-1==ord(x[j+1]) for j in range(minimum-1))):
            if x not in matches: matches.append(x)
    return {'matches':matches,'findings':[{'type':'sequence','severity':'medium','description':'A predictable ascending or descending character sequence was detected.'}] if matches else []}
def detect_keyboard_patterns(password):
    s=password.casefold(); m=[p for p in KEYBOARD_PATTERNS if p in s]
    return {'matches':m,'findings':[{'type':'keyboard_pattern','severity':'medium','description':'A predictable keyboard pattern was detected.'}] if m else []}
def detect_repetition(password):
    m=[]
    if re.search(r'(.)\1{3,}',password): m.append('repeated-character-run')
    for size in range(1,max(2,len(password)//2+1)):
        for i in range(len(password)-size*2+1):
            u=password[i:i+size]
            if u and password[i:i+size*2]==u*2:
                tag=f'repeated:{u}'
                if tag not in m:m.append(tag)
                break
    return {'matches':m,'findings':[{'type':'repetition','severity':'medium','description':'Repeated characters or repeated substrings reduce unpredictability.'}] if m else []}
def detect_predictable_structure(password):
    s=password.casefold(); m=[]
    if re.search(r'(password|welcome|admin|hello|letmein)\d{1,6}[!@#$%^&*]*$',s): m.append('common-word-plus-number')
    if re.search(r'(password|welcome|admin|hello|letmein|qwerty)\d{4}',s): m.append('word-plus-year-like-number')
    return {'matches':m,'findings':[{'type':'predictable_structure','severity':'high','description':'A common word followed by a predictable number/suffix was detected.'}] if m else []}
def detect_dictionary_words(password):
    s=password.casefold(); m=sorted([w for w in COMMON_WORDS if w in s and len(w)>=4],key=len,reverse=True)[:5]
    return {'matches':m,'findings':[{'type':'dictionary_word','severity':'medium','description':'A common dictionary word appears in the password.'}] if m else []}
def detect_date_year_patterns(password):
    m=sorted(set(re.findall(r'(?<!\d)(?:19\d{2}|20\d{2})(?!\d)',password)))
    return {'matches':m,'findings':[{'type':'date_year','severity':'medium','description':'A year-like value appears in the password and may be predictable.'}] if m else []}
