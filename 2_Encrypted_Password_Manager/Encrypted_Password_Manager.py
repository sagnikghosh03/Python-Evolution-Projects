from cryptography.fernet import Fernet
from rich.console import Console
from rich.table import Table
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
    console.print("\nChoose what you would like to do:\n\n\t[1] [bold orange_red1]Add[/bold orange_red1] password. \n\t[2] [bold green]View[/bold green] existing passwords. \n\t[3] [bold blue]Quit[/bold blue] the program. ")
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
            table = Table(title="Password Manager")
            table.add_column("Saved On", style="orange_red1")
            table.add_column("Account / Name", style="green")
            table.add_column("Password", style="bright_blue")

            for line in f.readlines():
                data = line.rstrip()
                saved_on, user, enc_pswd = data.split(" ")
                try:
                    dec_pswd = fernet.decrypt(enc_pswd.encode()).decode()
                    table.add_row(saved_on, user, dec_pswd)
                except Exception as e:
                    console.print(f"[red]Error:[/red] Failed to decrypt password for {user}.")

            console.clear()
            console.print(table)
    except FileNotFoundError:
        console.print("[yellow]No file has been created to store the info yet.[/yellow]")

def add(fernet):
    # Get current date and time
    current_datetime = datetime.datetime.now()
    date_added = current_datetime.strftime("%Y-%m-%d_@_%I:%M_%p")

    # Get the info
    name = input("Account / Name: ",)
    while True:
        gen_pass = input("\nDo you want to Generate a Random Password? (y/n): ")
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

def generate(length=None, has_num=None, has_special=None):
    if length is None:
        while True:
            try:
                length = int(input("\nWhat should be the length of the Password? "))
                break
            except Exception as e:
                console.print("[red]Error:[/red]", e)

    if has_num is None:
        while True:
            has_num = input("\nDo you want to include Numbers (y/n)? ").strip().lower()
            if check(has_num):
                break

    if has_special is None:
        while True:
            has_special = input("\nDo you want to include Special Characters (y/n)? ").strip().lower()
            if check(has_special):
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

def check(i):
    choices = ["y", "n"]

    if i not in choices:
        console.print("[red]Invalid choice![/red] Choose one from (y / n)")
        return False
    else:
        return True

if __name__ == "__main__":
    main()
