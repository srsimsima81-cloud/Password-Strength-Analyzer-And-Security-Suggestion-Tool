import secrets,string
def generate_password(length=20,uppercase=True,lowercase=True,numbers=True,symbols=True):
    pools=[]
    if uppercase:pools.append(string.ascii_uppercase)
    if lowercase:pools.append(string.ascii_lowercase)
    if numbers:pools.append(string.digits)
    if symbols:pools.append('!@#$%^&*()-_=+[]{}?')
    if not pools: raise ValueError('At least one character category must be enabled.')
    out=[secrets.choice(p) for p in pools]; combined=''.join(pools)
    while len(out)<length: out.append(secrets.choice(combined))
    for i in range(len(out)-1,0,-1):
        j=secrets.randbelow(i+1); out[i],out[j]=out[j],out[i]
    return ''.join(out)
