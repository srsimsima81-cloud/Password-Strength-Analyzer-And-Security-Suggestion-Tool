def generate_suggestions(length,chars,detections,policy_result,classification):
    s=[]
    if length['length']<12:s.append('Consider using a longer password or a long, randomly selected passphrase.')
    if detections['common']['is_common']:s.append('Do not use a commonly used password.')
    if detections['keyboard']['matches']:s.append('Avoid predictable keyboard sequences.')
    if detections['sequences']['matches']:s.append('Remove predictable ascending or descending sequences.')
    if detections['repetition']['matches']:s.append('Avoid repeated characters or repeated substrings.')
    if detections['predictable']['matches']:s.append('Avoid common-word-plus-number structures.')
    if detections['dictionary']['matches']:s.append('Avoid relying on common dictionary words unless they are part of a genuinely random passphrase.')
    if detections['date_patterns']['matches']:s.append('Avoid predictable years or dates.')
    if detections['personal']['overlap']:s.append('Avoid including your name, birth year, company, or college information.')
    if chars['character_type_count']<=1 and length['length']<16:s.append('Increase unpredictability rather than relying on one character type.')
    s += ['Use a password manager to create and store unique passwords.','Enable MFA wherever it is available.','Do not reuse passwords across important accounts.']
    if policy_result['status']=='FAIL':s.append('Review failed password-policy requirements separately from the strength score.')
    return list(dict.fromkeys(s))
