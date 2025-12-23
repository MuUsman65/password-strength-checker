COMMON_SEQUENCES = [
    # Numeric sequences
    "123",
    "234",
    "345",
    "456",
    "567",
    "678",
    "789",
    "012",

    # Alphabetical sequences
    "abc",
    "bcd",
    "cde",
    "def",
    "efg",
    "xyz",

    # Keyboard patterns
    "qwerty",
    "asdf",
    "zxcv",

    # Reverse sequences
    "321",
    "cba",
    "fed",
]




def length_rule(password: str):
    points = 0
    penalty = 0
    positives = []
    negatives = []
    
    length = len(password)
    
    if (length < 8):
        negatives.append("Too short(aim for at least 12 characters)!")
    elif (length >= 8 and length <= 11):
        points += 15
        negatives.append("Acceptable length, but longer is safer!")
    elif (length >= 12 and length <= 15):
        points += 28
        positives.append("Good length")
    elif (length >= 16 and length <= 19):
        points += 35
        positives.append("Very good length")
    elif (length >= 20):
        points = 40
        positives.append("Excellent length")
    
    return points, penalty, positives, negatives


def variety_rule(password: str):
    points = 0
    penalty = 0
    positives = []
    negatives = []
    
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    for c in password:
        if c.islower():
            has_lower = True
        elif c.isupper():
            has_upper = True
        elif c.isdigit():
            has_digit = True
        else:
            has_special = True
            
        if has_lower and has_upper and has_digit and has_special:
            break
        
    if (has_lower):
        points += 6
        positives.append("Includes Lowercase Letters")
    else:
        negatives.append("Add Lowercase Letters!")
    
    if (has_upper):
        points += 6
        positives.append("Includes Uppercase Letters")
    else:
        negatives.append("Add Uppercase Letters!")
        
    if (has_digit):
        points += 6
        positives.append("Includes Digits")
    else:
        negatives.append("Add Digits!")
        
    if (has_special):
        points += 7
        positives.append("Includes Special Characters")
    else:
        negatives.append("Add Special Characters (e.g. !@#)!")
        
    return points, penalty, positives, negatives

def uniqueness_rule(password: str):
    points = 0
    penalty = 0
    positives = []
    negatives = []
    
    if len(password) == 0:
        negatives.append("Password is empty!")
        return points, penalty, positives, negatives
    
    unique_ratio = len(set(password)) / len(password)
    
    if unique_ratio >= 0.7:
        points += 15
        positives.append("Excellent character variety (low repetition)")
    elif unique_ratio >= 0.5:
        points += 10
        positives.append("Good character variety")
    elif unique_ratio >= 0.3:
        points += 5
        negatives.append("Acceptable character variety, but more variety needed!")
    else:
        negatives.append("Too many repeated characters; use a wider mix!")
    
    return points, penalty, positives, negatives

def common_password_penalty(password: str, common_passwords):
    points = 0
    penalty = 0
    positives = []
    negatives = []
    
    normalised_password = password.lower().strip()
    
    if len(normalised_password) == 0:
        return points, penalty, positives, negatives
    
    if normalised_password in common_passwords:
        penalty = 40
        negatives.append("Exact password match found; this password appears in a list of commonly used passwords!")
            
    return points, penalty, positives, negatives

def repeat_character_penalty(password: str):
    points = 0
    penalty = 0
    positives = []
    negatives = []
    
    has_three_consecutive = False
    
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            has_three_consecutive = True
            break
    
    if has_three_consecutive:
        penalty = 10
        negatives.append("Has 3 or more identical characters in a row!")
            
    return points, penalty, positives, negatives

def sequence_penalty(password: str):
    points = 0
    penalty = 0
    positives = []
    negatives = []
    
    has_common_sequence = False
    normalised_password = password.lower().strip()
            
    for sequence in COMMON_SEQUENCES:
        if sequence.lower() in normalised_password:
            has_common_sequence = True
            break
            
    if has_common_sequence:
        penalty = 10
        negatives.append("Common sequence(s) detected within password!")
        
    return points, penalty, positives, negatives





























