import math
def estimate_theoretical_entropy(password):
    pool=(26 if any(c.islower() for c in password) else 0)+(26 if any(c.isupper() for c in password) else 0)+(10 if any(c.isdigit() for c in password) else 0)+(33 if any(not c.isalnum() and not c.isspace() for c in password) else 0)+(1 if any(c.isspace() for c in password) else 0)
    return {'bits':round(len(password)*math.log2(pool),2) if password and pool else 0.0,'pool_size':pool}
