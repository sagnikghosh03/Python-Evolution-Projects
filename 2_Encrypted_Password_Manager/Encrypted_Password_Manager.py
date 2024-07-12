import random
import string

def main():
    master_pwd = input("\nEnter the Master Password: ")


    while True:
        mode = input("\nWould you like to Add password or View existing passwords? Press 'q' to Quit. (add / view / q): ")
        
        if mode == 'q':
            break
        if mode == 'view':
            view()
        elif mode == 'add':
            add()
        else:
            print("Invalid mode. Choose one from (add / view / q)")
            continue

def view():
    try:
        with open("passwords.txt", 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                saved_on, user, enc_pswd = data.split(" ")
                print(f"\nSaved On: {saved_on} || Account Name: {user} || Password: {dec_pswd}")
    except FileNotFoundError:
        print("No file has been created to store the info yet.")

def add():
    # Get current date and time
    current_datetime = datetime.datetime.now()
    date_added = current_datetime.strftime("%Y-%m-%d_@_%I:%M_%p")
    
    name = input("Account Name: ")
    while True:
        gen_pass=input("Do you want to Generate a random password? (y/n): ")
        choices=["y","n"]

        if gen_pass not in choices:
            print("Invalid choice. Choose one from (y / n)\n")
            continue
        else:
            break      

    if gen_pass == "y":
        pwd = generate()
    else:
        pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:
        f.write(date_added + " " + name + " " + encrypted_pwd + "\n")
    print("DONE!")

def generate():
    while True:
        try:
            length=int(input("\nWhat should be the length of the Password? "))
            break
        except Exception as e:
            print("Error:", e)
    while True:
        has_num=input("Do you want to include Numbers (y/n)? ").strip().lower()
        has_special=input("Do you want to include Special Characters (y/n)? ").strip().lower()
        choices=["y","n"]

        if has_num not in choices and has_special not in choices:
            print("Invalid choice. Choose one from (y / n)\n")
        else:
            break

    letters=string.ascii_letters
    num=string.digits
    special=string.punctuation

    characters=letters

    if has_num == "y":
        characters += num

    if has_special == "y":
        characters += special

    pwd=""    
    for i in range(length):
        pwd += random.choice(characters)

    return pwd

if __name__=="__main__":
    main()
