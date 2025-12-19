import random
import string

def generate_password(length=12, use_special_chars=True):
    characters = string.ascii_letters + string.digits 
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the desired password length (default is 12): ") or 12)
    use_special_chars = input("Include special characters? (yes/no, default is yes): ").strip().lower() in ['yes', 'y', '']

    password = generate_password(length, use_special_chars)
    print(f"Generated Password: {password}")
    save_choice = input("Do you want to save
        with open("generated_password.txt",  this password to a file? (yes/no): ").strip().lower()
    if save_choice in ['yes', 'y']:"w") as file:
            file.write(password)
        print("Password saved to generated_password.txt")
    else:
        print("Password not saved.")
    if __name__ == "__main__":

        print("Thank you for using the Random Password Generator!")