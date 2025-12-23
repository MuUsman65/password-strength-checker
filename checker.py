from rules import length_rule
from rules import variety_rule
from rules import uniqueness_rule
from rules import common_password_penalty
from rules import repeat_character_penalty
from rules import sequence_penalty

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

def load_common_passwords(path):
    common_passwords = set()
    
    # Opening The File
    with open(path, "r") as file:
        for line in file:
            line = line.strip().lower()
            if line:
                common_passwords.add(line)
                
    return common_passwords

def strength_label(score: int):
    label = ""
    
    if (0 <= score <= 24):
        label = "Very Weak"
    elif (25 <= score <= 44):
        label = "Weak"
    elif (45 <= score <= 64):
        label = "Medium"
    elif (65 <= score <= 84):
        label = "Strong"
    else:
        label = "Very Strong"
        
    return label

def evaluate(password: str, common_passwords: set[str]):
    total_points = 0
    total_penalty = 0
    positives = []
    negatives = []
    
    # Unpacking
    lp, lpen, lpos, lneg = length_rule(password) # penalty is never applied
    vp, vpen, vpos, vneg = variety_rule(password) # penalty is never applied
    up, upen, upos, uneg = uniqueness_rule(password) # penalty is never applied
    
    cp, cpen, cpos, cneg = common_password_penalty(password, common_passwords) # points are never applied
    rp, rpen, rpos, rneg = repeat_character_penalty(password) # points are never applied
    sp, spen, spos, sneg = sequence_penalty(password) # points are never applied    
   
    # Calculating total points and penalties
    total_points = lp + vp + up
    total_penalty = cpen + rpen + spen
    
    # Positives & Negatives
    positives.extend(lpos + vpos + upos)
    negatives.extend(lneg + vneg + uneg + cneg + rneg + sneg)
    
    raw_score = total_points - total_penalty
    score = clamp(raw_score, 0, 100)
    
    label = strength_label(score)
    
    mock_api = {
        "score": score,
        "label": label,
        "positives": positives,
        "negatives": negatives,
        "points": total_points,
        "penalty": total_penalty
        }
    
    return mock_api
    
# print(load_common_passwords("common_passwords.txt"))





























