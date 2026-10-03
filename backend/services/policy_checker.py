DEFAULT_POLICY={'minimum_length':12,'common_password_check':True,'personal_info_check':True,'allow_spaces':True}
def evaluate_policy(password,is_common,personal_overlap,policy=None):
    cfg=DEFAULT_POLICY.copy(); cfg.update(policy or {}); failures=[]
    if len(password)<int(cfg['minimum_length']):failures.append(f"Minimum length is {cfg['minimum_length']} characters.")
    if cfg['common_password_check'] and is_common:failures.append('Common passwords are rejected.')
    if cfg['personal_info_check'] and personal_overlap:failures.append('Personal-information overlap is not permitted.')
    if not cfg['allow_spaces'] and any(c.isspace() for c in password):failures.append('Spaces are not permitted by this policy.')
    return {'status':'PASS' if not failures else 'FAIL','minimum_length':int(cfg['minimum_length']),'failures':failures}
