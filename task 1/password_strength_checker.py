
from __future__ import annotations

import string
import getpass
from typing import Dict, List


def analyze_password(password: str) -> Dict[str, object]:
    
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    # Treat any non-alphanumeric as a special symbol
    has_symbol = any((not c.isalnum()) for c in password)

    types_present = sum([has_lower, has_upper, has_digit, has_symbol])
    missing: List[str] = []
    if not has_lower:
        missing.append("lowercase letter")
    if not has_upper:
        missing.append("uppercase letter")
    if not has_digit:
        missing.append("number")
    if not has_symbol:
        missing.append("special symbol")

    return {
        "length": len(password),
        "has_lower": has_lower,
        "has_upper": has_upper,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "types_present": types_present,
        "missing": missing,
    }


def evaluate_strength(info: Dict[str, object]) -> str:
  
    length = info["length"]
    types_present = info["types_present"]
    missing_count = len(info["missing"])

    if length < 6 or missing_count >= 2:
        return "Weak"

    if length >= 10 and types_present == 4:
        return "Strong"

    if 6 <= length <= 9 and types_present >= 2:
        return "Medium"

    if length >= 10 and types_present >= 2:
        # Long but missing something — still better than short
        return "Medium"

    return "Weak"


def feedback_messages(info: Dict[str, object], strength: str) -> List[str]:
    """Generate user-facing feedback messages to improve the password."""
    messages: List[str] = []
    length = info["length"]
    missing = info["missing"]

    if length < 6:
        messages.append(f"Password is too short ({length} characters). Aim for at least 10 for strong passwords.")
    elif length < 10:
        messages.append("Consider increasing password length to 10+ characters for stronger protection.")

    if missing:
        for m in missing:
            messages.append(f"Missing a {m}.")

    if not messages:
        messages.append("Good job — your password meets the recommended complexity rules.")

    # Small tailored tip
    if strength == "Weak":
        messages.append("Tip: Combine upper+lower letters, digits, and symbols, and increase length.")

    return messages


def prompt_yes_no(prompt: str) -> bool:
    resp = input(prompt + " ").strip().lower()
    return resp in ("y", "yes")


def main() -> None:
    print("Password Strength Checker — interactive CLI")
    print("(Passwords are not stored or logged. Input is hidden for privacy.)")

    while True:
        try:
            password = getpass.getpass("Enter password: ")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

        if password == "":
            print("Empty password — please enter a password.")
            if not prompt_yes_no("Try again? (y/N):"):
                break
            continue

        info = analyze_password(password)
        strength = evaluate_strength(info)
        print(f"\nResult: {strength}")

        print("Feedback:")
        for line in feedback_messages(info, strength):
            print("- " + line)

        if not prompt_yes_no("Test another password? (y/N):"):
            print("Done.")
            break


if __name__ == "__main__":
    main()
