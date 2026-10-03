def analyze_characters(password):
    lo=any(c.islower() for c in password); up=any(c.isupper() for c in password); di=any(c.isdigit() for c in password); sy=any(not c.isalnum() and not c.isspace() for c in password); sp=any(c.isspace() for c in password)
    types=sum([lo,up,di,sy,sp]); unique=len(set(password)); ratio=round(unique/len(password),3) if password else 0.0
    return {'lowercase':lo,'uppercase':up,'digits':di,'symbols':sy,'spaces':sp,'character_type_count':types,'unique_character_count':unique,'unique_character_ratio':ratio}
