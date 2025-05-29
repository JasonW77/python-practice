import re
from getpass import getpass

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        'Too Short (<8 chars)': length_error,
        'No Digit': digit_error,
        'No Uppercase Letter': uppercase_error,
        'No Lowercase Letter': lowercase_error,
        'No Symbol': symbol_error,
    }

    passed_checks = sum(not error for error in errors.values())
    if passed_checks == 5:
        strength = "Strong 💪"
    elif passed_checks >= 3:
        strength = "Moderate 🧐"
    else:
        strength = "Weak ⚠️"

    return strength, errors

if __name__ == "__main__":
    password = getpass("Enter your password: ")
    strength, errors = check_password_strength(password)

    print(f"\nPassword Strength: {strength}\n")
    for error, present in errors.items():
        if present:
            print(f"❌ {error}")
        else:
            print(f"✅ {error}")
