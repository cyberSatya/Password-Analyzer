import re

def password_analyzer(password):
    # Initialize score
    score = 0
    
    # Length check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    
    # Check for digits
    if re.search(r'[0-9]', password):
        score += 1
    
    # Check for special characters
    if re.search(r'[@$!%*?&#]', password):
        score += 1
    
    # Evaluate score
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    # Return result
    return {
        "password": password,
        "score": score,
        "strength": strength,
        "criteria": {
            "length_8": len(password) >= 8,
            "length_12": len(password) >= 12,
            "uppercase": bool(re.search(r'[A-Z]', password)),
            "lowercase": bool(re.search(r'[a-z]', password)),
            "digit": bool(re.search(r'[0-9]', password)),
            "special_char": bool(re.search(r'[@$!%*?&#]', password))
        }
    }

# Example usage
password = "Example@123"
analysis = password_analyzer(password)
print(analysis)
