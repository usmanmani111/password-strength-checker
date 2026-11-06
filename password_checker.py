#!/usr/bin/env python3
"""Password Strength Checker — student learning project (Python stdlib only).

Runs fully offline. Nothing is sent, stored or logged — the password
you type is checked in memory and then forgotten.

Run it:
    python3 password_checker.py            # type a test password (hidden as you type)
    python3 password_checker.py --demo     # checks sample passwords, no typing needed

Tip: use test passwords here, not a real password you use anywhere.
What it teaches: length, character variety, common-password lists,
and why a long passphrase beats a short "clever" password.
"""
import argparse
import getpass
import re

# A small list of the most common weak passwords. Real checkers use
# much bigger lists; this one is enough to learn the idea.
COMMON_PASSWORDS = {
    "password", "123456", "123456789", "12345678", "12345", "qwerty",
    "abc123", "letmein", "admin", "welcome", "monkey", "dragon",
    "iloveyou", "football", "123123", "111111", "000000",
}


def check(password: str) -> tuple[int, list[str]]:
    """Return (score 0-5, list of feedback lines)."""
    score = 0
    notes: list[str] = []

    if len(password) >= 12:
        score += 1
        notes.append("Good length (12+ characters).")
    elif len(password) >= 8:
        notes.append("Okay length, but 12+ characters is much stronger.")
    else:
        notes.append("Too short — aim for 12+ characters.")

    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
        notes.append("Has both lower-case and upper-case letters.")
    else:
        notes.append("Mix lower-case and upper-case letters.")

    if re.search(r"\d", password):
        score += 1
        notes.append("Has numbers.")
    else:
        notes.append("Add some numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
        notes.append("Has a symbol (!, @, #, ...).")
    else:
        notes.append("Add a symbol, e.g. ! or #.")

    if password.lower() not in COMMON_PASSWORDS and len(password) >= 8:
        score += 1
    else:
        notes.append("This is a very common password — attackers try it first.")

    return score, notes


def verdict(score: int) -> str:
    return ["Very weak", "Weak", "Okay", "Good", "Strong", "Very strong"][score]


def report(password: str, label: str = "Password") -> None:
    score, notes = check(password)
    print(f"{label}: {'*' * len(password)}  ->  {verdict(score)} ({score}/5)")
    for note in notes:
        print(f"  - {note}")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Password Strength Checker (offline)")
    parser.add_argument("--demo", action="store_true",
                        help="check sample passwords instead of asking for one")
    args = parser.parse_args()

    if args.demo:
        for sample in ["password", "Usman123", "Tr7!kLm9#qZx2"]:
            report(sample, label=f"Sample {sample!r}")
        print("Demo done. Try your own test password with: python3 password_checker.py")
        return

    password = getpass.getpass("Type a TEST password (hidden): ")
    if not password:
        print("No password typed.")
        return
    report(password)


if __name__ == "__main__":
    main()
