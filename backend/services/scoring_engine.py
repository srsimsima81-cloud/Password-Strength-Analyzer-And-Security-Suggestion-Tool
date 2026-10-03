def calculate_score(length,chars,common,sequences,keyboard,repetition,predictable,dictionary,date_patterns,personal,entropy):
    lp=min(35,length['length']*2.2); dp=min(15,chars['character_type_count']*3.75); up=min(10,chars['unique_character_ratio']*10)
    penalty=(8 if sequences['matches'] else 0)+(8 if keyboard['matches'] else 0)+min(12,len(repetition['matches'])*4)+(8 if predictable['matches'] else 0)+(5 if dictionary['matches'] else 0)+(5 if date_patterns['matches'] else 0)+(12 if personal['overlap'] else 0)
    pattern=max(0,20-penalty); common_pts=0 if common['is_common'] else 10; entropy_pts=min(10,entropy['bits']/12)
    raw=lp+dp+up+pattern+common_pts+entropy_pts
    if common['is_common']: raw-=25
    if length['length']<8: raw-=15
    return max(0,min(100,round(raw)))
def classify_score(score):
    return 'VERY WEAK' if score<=20 else 'WEAK' if score<=40 else 'MODERATE' if score<=60 else 'STRONG' if score<=80 else 'VERY STRONG'
