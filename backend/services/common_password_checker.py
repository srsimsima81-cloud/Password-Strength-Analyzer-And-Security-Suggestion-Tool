DEFAULT_COMMON={'password','password123','123456','12345678','qwerty','letmein','welcome','admin'}
def is_common_password(password,path=None):
    values=set(DEFAULT_COMMON)
    if path and path.exists():
        try: values.update(x.strip().casefold() for x in path.read_text(encoding='utf-8').splitlines() if x.strip() and not x.startswith('#'))
        except OSError: pass
    found=password.casefold() in values
    return {'is_common':found,'matches':[password.casefold()] if found else [],'findings':[{'type':'common_password','severity':'high','description':'Your password matches a commonly used password pattern and should not be used.'}] if found else []}
