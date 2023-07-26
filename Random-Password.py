import random
# to randomize
import string
# collection of letters
def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
# the rules for the password
    if not characters:
        raise ValueError(" Must contain number, special characters, uppercase and lowercase letters! ")
    # making sure the user implements these so the password can be strong

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
# password will be random characters everytime
if __name__ == "__main__":
    try:
        password = generate_password()
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", str(e))


Source: Python Official Documentation (https://docs.python.org/)
Source: How to Run a Python Script on Mac (https://macosx-faq.com/how-to-run-python-script/)