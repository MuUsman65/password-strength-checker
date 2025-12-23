import sys
import getpass

from checker import load_common_passwords
from checker import evaluate
from pathlib import Path

# Getting "main.py" directory
script_dir = Path(__file__).parent
file_path = script_dir / "common_passwords.txt" # creating path to "common_passwords.txt"

def main():
    # Input Handling - 2 Modes
    if len(sys.argv) > 1:                           # Argument Mode
        password = sys.argv[1]
    else:                                           # Interactive Mode
        password = getpass.getpass("Enter password: ")
        
    try:
        common_passwords = load_common_passwords(file_path)
    except FileNotFoundError:
        print("common_passwords.txt not found. Make sure it’s in the same folder as main.py.")
        common_passwords = set()

    result = evaluate(password, common_passwords)

    # Print score and label
    print(f"Score: {result['score']}/100")
    print(f"Strength: {result['label']}")
    print()

    # Print Positives
    if result['positives']:
        print("Positives:")
        for item in result['positives']:
            print(f"    + {item}")
        print()
        
    # Print Negatives
    if result['negatives']:
        print("Improvements:") # Changed from "Negatives" to make it more user-friendly
        for item in result['negatives']:
            print(f"    - {item}")
        print()
    
if __name__ == "__main__":
    main()

















