# Password Strength Checker

Simple interactive CLI tool to evaluate password strength and provide
feedback to help users improve passwords.

Usage
- Run the script with Python 3.8+: `python "password_strength_checker.py"`
- The script uses a hidden prompt (no echo) to collect the password.

Strength Rules
- Weak: length < 6 OR missing multiple character types
- Medium: length 6–9 with at least 2 character types, or length 10+ with some but not all types
- Strong: length >= 10 AND contains uppercase, lowercase, digits, and symbols

Security
- The script does not store or log passwords. It uses `getpass.getpass()` so
  input is not echoed to the terminal.

Files
- `password_strength_checker.py` — the main CLI script

License
- Unlicensed, use as you wish.
