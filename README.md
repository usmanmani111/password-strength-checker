# Password Strength Checker

A small, offline password strength checker written in Python. It scores a test password from 0 to 5 and explains how to make it stronger.

This is a learning project. It is not a professional security tool.

## What it does

- Scores a password on 5 checks: length (12+ characters), mixed upper- and lower-case letters, numbers, a symbol, and not being a common password
- Gives a verdict: Very weak, Weak, Okay, Good, Strong, or Very strong
- Gives one line of feedback for each check, so you can see exactly what to improve
- Checks a small list of common passwords, such as `password`, `123456`, and `qwerty`

## Technologies

- Python 3 (standard library only — no installation, no dependencies, no API key)

## How to run it

Check the sample passwords, without typing anything:

```bash
python3 password_checker.py --demo
```

Example output:

```
Sample 'password': ********  ->  Very weak (0/5)
  - Okay length, but 12+ characters is much stronger.
  - Mix lower-case and upper-case letters.
  - Add some numbers.
  - Add a symbol, e.g. ! or #.
  - This is a very common password — attackers try it first.

Sample 'Usman123': ********  ->  Good (3/5)
  - Okay length, but 12+ characters is much stronger.
  - Has both lower-case and upper-case letters.
  - Has numbers.
  - Add a symbol, e.g. ! or #.

Sample 'Tr7!kLm9#qZx2': *************  ->  Very strong (5/5)
  - Good length (12+ characters).
  - Has both lower-case and upper-case letters.
  - Has numbers.
  - Has a symbol (!, @, #, ...).
```

Check your own test password (hidden while you type):

```bash
python3 password_checker.py
```

## Safety and responsible use

This checker runs fully offline. Nothing is sent, stored, or logged — the password is checked in memory and then forgotten.

Use test passwords here, not a real password you use anywhere.

## What I learned

- How password strength is actually measured: length matters most, then character variety
- Why a long passphrase beats a short "clever" password
- How common-password lists work — attackers try the most common passwords first
- How to handle sensitive input safely, with hidden input and no logging

## Future improvements

- Use a larger common-password list
- Add an estimated crack-time hint for each score
- Add a passphrase generator
