def check_personal_context(password,context):
    s=password.casefold(); overlaps=[]
    for key,label in {'first_name':'name','birth_year':'birth year','company_college':'company/college'}.items():
        value=str(context.get(key,'') or '').strip()
        if len(value)>=3 and value.casefold() in s: overlaps.append(label)
    return {'overlap':overlaps,'findings':[{'type':'personal_information','severity':'high','description':'Password appears to contain personal information supplied for this analysis.'}] if overlaps else []}
