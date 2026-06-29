import re

def check_password(password):

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 20
    else:
        suggestions.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 20
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 20
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"\d", password):
        score += 20
    else:
        suggestions.append("Add numbers")

    if re.search(r"[!@#$%^&*()_+=<>?/{}~]", password):
        score += 20
    else:
        suggestions.append("Add special characters")

    if score >= 80:
        strength = "Strong 🟢"
    elif score >= 50:
        strength = "Medium 🟡"
    else:
        strength = "Weak 🔴"

    return score, strength, suggestions