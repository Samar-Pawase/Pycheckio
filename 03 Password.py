# Based on weather entered password is more than 6 characters or not, return True or False

def passCheck(password):
    return len(password)>6

print(passCheck('SufficientlyBigPassword'))