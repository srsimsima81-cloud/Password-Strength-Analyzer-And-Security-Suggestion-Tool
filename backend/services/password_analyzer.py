from services.length_analyzer import analyze_length
from services.character_analyzer import analyze_characters
from services.pattern_detector import detect_sequences,detect_keyboard_patterns,detect_repetition,detect_predictable_structure,detect_dictionary_words,detect_date_year_patterns
from services.common_password_checker import is_common_password
from services.entropy_estimator import estimate_theoretical_entropy
from services.scoring_engine import calculate_score,classify_score
from services.suggestion_engine import generate_suggestions
from services.context_checker import check_personal_context
from services.policy_checker import evaluate_policy

def analyze_password(password,context=None,common_password_file=None,policy=None):
    context=context or {}; policy=policy or {}
    length=analyze_length(password); chars=analyze_characters(password); sequences=detect_sequences(password); keyboard=detect_keyboard_patterns(password); repetition=detect_repetition(password); predictable=detect_predictable_structure(password); dictionary=detect_dictionary_words(password); dates=detect_date_year_patterns(password); common=is_common_password(password,common_password_file); personal=check_personal_context(password,context); entropy=estimate_theoretical_entropy(password)
    detections={'common':common,'sequences':sequences,'keyboard':keyboard,'repetition':repetition,'predictable':predictable,'dictionary':dictionary,'date_patterns':dates,'personal':personal}
    score=calculate_score(length,chars,common,sequences,keyboard,repetition,predictable,dictionary,dates,personal,entropy); classification=classify_score(score)
    findings=[]
    for d in detections.values(): findings.extend(d.get('findings',[]))
    policy_result=evaluate_policy(password,common['is_common'],personal['overlap'],policy)
    suggestions=generate_suggestions(length,chars,detections,policy_result,classification)
    metrics={'length':length['length'],'length_guidance':length['guidance'],'uppercase':chars['uppercase'],'lowercase':chars['lowercase'],'digits':chars['digits'],'symbols':chars['symbols'],'spaces':chars['spaces'],'character_type_count':chars['character_type_count'],'unique_character_count':chars['unique_character_count'],'unique_character_ratio':chars['unique_character_ratio'],'theoretical_entropy_bits':entropy['bits'],'estimated_character_pool':entropy['pool_size'],'pattern_count':sum(len(d.get('matches',[])) for d in detections.values()),'common_password':common['is_common'],'sequence_matches':sequences['matches'],'keyboard_matches':keyboard['matches'],'repetition_matches':repetition['matches'],'dictionary_words':dictionary['matches'],'date_year_matches':dates['matches'],'personal_overlap':personal['overlap']}
    return {'score':score,'classification':classification,'findings':findings,'suggestions':suggestions,'metrics':metrics,'policy':policy_result,'education':{'entropy_note':'The entropy-style value assumes random character selection and can be optimistic for human-created passwords.','strength_note':'This score is a project-defined educational model, not a universal security standard.'}}
