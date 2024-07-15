from cryptography.fernet import Fernet
from rich.console import Console
import datetime
import random
import string
import os

# Create a Console instance
console = Console()

def main():
    # Clear the console
    console.clear()
    if not os.path.exists("key.key"):
        generate_master_password()

    key = load_key()
    fernet = Fernet(key)
    while True:
        master_pwd = input("\nEnter the Master Password: ")

        if not verify_master_password(fernet, master_pwd):
            console.print("[red]Incorrect Master Password!!![/red]")
            continue
        else:
            break
    console.clear()
    console.print("\nChoose what you would like to do:\n\n\t[1] Add password. \n\t[2] View existing passwords. \n\t[3] Quit the program. ")
    while True:
        mode = input("\nWhat would you like to do? (1 / 2 / 3): ")
        if mode == '3':
            break
        if mode == '2':
            view(fernet)
        elif mode == '1':
            add(fernet)
        else:
            console.print("[red]Invalid mode choice![/red] Choose one from (1 / 2 / 3)")
            continue

def generate_master_password():
    master_pwd = input("Set your Master Password: ")
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)
    fernet = Fernet(key)
    encrypted_master_pwd = fernet.encrypt(master_pwd.encode())
    with open("master.key", "wb") as f:
        f.write(encrypted_master_pwd)

def load_key():
    return open("key.key", "rb").read()

def verify_master_password(fernet, master_pwd):
    with open("master.key", "rb") as f:
        encrypted_master_pwd = f.read()
    decrypted_master_pwd = fernet.decrypt(encrypted_master_pwd).decode()
    return decrypted_master_pwd == master_pwd

def view(fernet):
    try:
        with open("passwords.txt", 'r') as f:
            print("-"*33)
            for line in f.readlines():
                data = line.rstrip()
                saved_on, user, enc_pswd = data.split(" ")
                try:
                    dec_pswd = fernet.decrypt(enc_pswd.encode()).decode()
                    print(f"\nSaved On: {saved_on} || Account Name: {user} || Password: {dec_pswd}")
                except Exception as e:
                    print(f"Error: {e}")
            print("\n","-"*33, sep="", end="")
    except FileNotFoundError:
        print("No file has been created to store the info yet.")

def add(fernet):
    # Get current date and time
    current_datetime = datetime.datetime.now()
    date_added = current_datetime.strftime("%Y-%m-%d_@_%I:%M_%p")

    # Get the info
    name = input("Account Name: ",)
    while True:
        gen_pass = input("\nDo you want to Generate a random password? (y/n): ")
        choices = ["y", "n"]

        if gen_pass not in choices:
            console.print("[red]Invalid choice![/red] Choose one from (y / n)")
            continue
        else:
            break      

    if gen_pass == "y":
        pwd = generate()
    else:
        pwd = input("Password: ")

    encrypted_pwd = fernet.encrypt(pwd.encode()).decode()

    with open("passwords.txt", 'a') as f:
        f.write(date_added + " " + name + " " + encrypted_pwd + "\n")
    print("\nDONE!")

def generate():
    while True:
        try:
            length = int(input("\nWhat should be the length of the Password? "))
            break
        except Exception as e:
            console.print("[red]Error:[/red]", e)
    
    while True:
        has_num = input("Do you want to include Numbers (y/n)? ").strip().lower()
        has_special = input("Do you want to include Special Characters (y/n)? ").strip().lower()
        choices = ["y", "n"]

        if has_num not in choices or has_special not in choices:
            console.print("[red]Invalid choice![/red] Choose one from (y / n)\n")
        else:
            break

    letters = string.ascii_letters
    num = string.digits
    special = string.punctuation
    characters = letters

    if has_num == "y":
        characters += num

    if has_special == "y":
        characters += special

    pwd = ""
    for i in range(length):
        pwd += random.choice(characters)

    return pwd

if __name__ == "__main__":
    main()
