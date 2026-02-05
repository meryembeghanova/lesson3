# Password Validator using a WHILE loop
# The program keeps asking the user for a password
# until all conditions for a strong password are met.

print("🔐 Welcome to the Password Validator!")
print("Your password must:")
print("- Be at least 8 characters long")
print("- Contain at least one number")
print("- Contain at least one uppercase letter")
print("- Contain at least one lowercase letter\n")

while True:
    password = input("Enter a password: ")

    # Conditions
    length_ok = len(password) >= 8
    has_number = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)

    if length_ok and has_number and has_upper and has_lower:
        print("✅ Strong password accepted! 🎉")
        break
    else:
        print("❌ Weak password. Please try again.\n")
        if not length_ok:
            print("• Password must be at least 8 characters")
        if not has_number:
            print("• Password must include a number")
        if not has_upper:
            print("• Password must include an uppercase letter")
        if not has_lower:
            print("• Password must include a lowercase letter")
        print()
