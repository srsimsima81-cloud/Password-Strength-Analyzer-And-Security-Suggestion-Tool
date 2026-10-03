def analyze_length(password):
    n=len(password)
    guidance='Very short' if n<8 else 'Short' if n<=11 else 'Better length' if n<=15 else 'Strong length contribution'
    return {'length':n,'guidance':guidance,'score_hint':min(35,round(n*2.2)) if n else 0}
