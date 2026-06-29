from urllib.parse import urlparse

def analyze_url(url):

    risk = []

    if not url.startswith("https://"):
        risk.append("❌ Website is not using HTTPS")

    if len(url) > 75:
        risk.append("⚠ Very long URL")

    if "@" in url:
        risk.append("⚠ Contains @ symbol")

    if "-" in url:
        risk.append("⚠ Contains hyphen (-)")

    suspicious_words = [
        "login",
        "verify",
        "secure",
        "update",
        "bank",
        "paypal",
        "free",
        "gift"
    ]

    lower = url.lower()

    for word in suspicious_words:
        if word in lower:
            risk.append(f"⚠ Suspicious keyword: {word}")

    if len(risk) == 0:
        return "🟢 Safe URL\n\nNo suspicious indicators found."

    output = "🔴 Suspicious URL\n\n"

    for item in risk:
        output += item + "\n"

    return output