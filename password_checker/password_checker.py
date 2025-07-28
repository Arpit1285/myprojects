def check_length(pas1):
    if len(pas1) < 6:
        score=0
    elif 6 <= len(pas1) < 8:
            score=1
    else: score=2
    return score

def check_upper(pas2):
    point1=0
    for char in pas2:
        if char.isupper():
            point1+=1
    return point1

def check_lower(pas3):
    point2=0
    for char in pas3:
        if char.islower():
            point2+=1
    return point2

def check_number(pas4):
    point3=0
    for char in pas4:
        if char.isdigit():
            point3+=1
    return point3

def check_symbol(pas5):
    point4=0
    symbols = {'!', '@', '#', '$', '%', '^', '&'}
    for char in pas5:
        if char in symbols:
            point4+=1
    return point4

def main():
    password=input("Enter a password: ")
    score = 0
    score += check_length(password)
    if check_upper(password) > 0:
        score += 1
    if check_lower(password) > 0:
        score += 1
    if check_number(password) > 0:
        score += 1
    if check_symbol(password) > 0:
        score += 1

    if score <= 3:
        print("Weak Password")
    elif score <= 5:
        print("Moderate Password")
    else:
        print("Strong Password")

main()