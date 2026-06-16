
from password_strength_checker import analyze_password, evaluate_strength, feedback_messages


tests = [
    "",
    "abc",
    "abcdef",
    "Abcdef1",
    "Abcdef1!",
    "Abcd1234!",
    "Abcd1234!X",
]


def run_tests():
    for p in tests:
        info = analyze_password(p)
        strength = evaluate_strength(info)
        print(f"Password: {repr(p)} -> {strength}")
        for msg in feedback_messages(info, strength):
            print("  -", msg)
        print()


if __name__ == "__main__":
    run_tests()
