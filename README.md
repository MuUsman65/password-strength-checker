# Password Strength Checker (Python)

A command line password strength checker built in Python that evaluates passwords using multiple security-focused rules and provides a clear score, strength label and actionable feedback.

This project was designed as a clean, well-structured mini-tool to demonstrate rule-based design and security awareness.

## Features
- Scores passwords on a 0-100 scale
- Assigns a clear strength label
      - Very Weak --> Very Strong
- Checks for:
      - Password Length
      - Character Variety (Upper, Lower, Digits, Special)
      - Repetition Patterns
      - Common Insecure Sequences
      - Commonly Used Passwords (via external list)
  - Provides actionable feedback, not just a verdict
  - Works in:
      - CLI Argument Mode
      - Interactive (hidden input) mode

## How the Scoring Works
### Positive Scoring
- Length (up to 40 points)
- Character Variety (up to 25 points)
- Uniqueness / Low Repitition (up to 15 points)
### Penalties
- Common Password Math: -40 points
- Repeated Characters (e.g. aaa): -10 points
- Common Sequences (e.g. 123, qwerty): -10 points
Final score is clamped between 0 and 100

## Project Structure
PasswordStrengthChecker/
│── main.py
│── checker.py
│── rules.py
│── common_passwords.txt
│── README.md
│── requirements.txt

## How to Run
### Argument Mode
Pass the password directly as a command-line argument:
- e.g. "python main.py MyPass123"
- NOTE: If password contains special characters, always wrap in quotes

### Interactive Mode
Runs without arguments:
- e.g. "python main.py"
- You will be prompted to enter a password securely (input will not be displayed)

## Example Output
Score: 74/100
Strength: Strong

Positives:
    + Good length.
    + Includes uppercase letters.
    + Includes digits.
    + Good character variety.

Improvements:
    - Add a special character.
    - Avoid common sequences such as 123 or qwerty.

## Design Decisions
- Rule-based Architecture:
  Each rule is implemented as a pure function, making the system easy to extend or modify
- Separation of Concerns:
    - rules.py --> scoring logic
    - checker.py --> aggregation and evaluation
    - main.py --> user interaction
- Data vs Logic:
    - Common passwords are stored externally (common_passwords.txt)
    - Common sequences are defined in code (part of security logic)

## Possible Future Improvements
- Integration with password breach APIs (e.g. Have I Been Pwned)
- Unit tests for all rules
- Configurable scoring weights
- GUI or Web Interface
- Automatic Generation of Insecure Sequences














