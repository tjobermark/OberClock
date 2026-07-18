GREAT = 5
GOOD = 3
POOR = 1

def thick_divider():
    print("===================================")

def thin_divider():
    print("-----------------------------------")

def space(lines=1):
    for _ in range(lines):
        print()

def percentage(value, total):
    return (value / total) * 100

def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        
        if answer in ["yes", "no"]:
            return answer
        
        print("Please enter 'yes' or 'no'.")

def rate_high_good(item, high_score, medium_score):
    if item >= high_score:
        return GREAT
    elif item >= medium_score:
        return GOOD
    else:
        return POOR

def rate_low_good(item, low_score, medium_score):
    if item <= low_score:
        return GREAT
    elif item <= medium_score:
        return GOOD
    else:
        return POOR