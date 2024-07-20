import re

def validate_username(username):
    if username and len(username) <= 50:
        return "Username is valid"
    return "Username is invalid"

def validate_password(password):
    if len(password) >= 8 \
            and re.search(r'[!@#$%^&*(),.?":{}|<>]', password) \
            and re.search(r'\d', password) \
            and re.search(r'[A-Z]', password) \
            and re.search(r'[a-z]', password):
        return "Password is valid"
    return "Password is invalid"

def validate_email(email):
    if '@' in email:
        username_domain = email.split('@')
        if len(username_domain) == 2 and username_domain[0].isalnum():
            domain_parts = username_domain[1].split('.')
            if len(domain_parts) >= 2 and all(part.isalpha() for part in domain_parts):
                return "Email is valid"
    return "Email is invalid"

def main():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")

    print(validate_username(username))
    print(validate_password(password))
    print(validate_email(email))

if __name__ == "__main__":
    main()
