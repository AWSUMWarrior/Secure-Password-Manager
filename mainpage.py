import sys
import os
import json
import getpass
from password_viewer import PasswordViewer
from password_creation import PasswordCreation
from password_deletion import PasswordDeletion
from encryption_manager import EncryptionManager
from login_manager import LoginManager
from mainpage_layout import MainPage


LOGIN_FILE = "login_authentication.json"


#Setting up instances of the classes
main_page = MainPage()
viewer = PasswordViewer()
password_creator = PasswordCreation()
password_deletor = PasswordDeletion()


#Functions for the View Passwords
def password_viewer_channel():
    viewer.get_user_info()
    viewer.password_viewer()


#Functions for the Create Passwords
def password_creation_channel():
    password_creator.creation_process_repeated()
    password_creator.user_repeated_password_creation()


#Functions for the Delete Passwords
def password_deletion_channel():
    password_deletor.delete_info()
    password_deletor.user_repeated_password_deletion()


#Method to ask user if they want to return to the menu
def return_to_menu() -> str:
    return_menu_input = input("\nDo you want to return to the menu? (Y/N): ").strip().upper()


    while(return_menu_input != "Y" and return_menu_input != "N"):
        print("You didn't select either Y or N. Please try again")
        return_menu_input = input("\nDo you want to return to the menu? (Y/N): ").strip().upper()


    return return_menu_input



encr = EncryptionManager()
login = LoginManager()


# Creates a login file for new users
if not os.path.exists(LOGIN_FILE):
    login.login_creation()


check_username: str
check_password: str


encr.file_decryption(file_inserted=LOGIN_FILE)
with open(LOGIN_FILE, "r") as file:
    login_list = json.load(file)
    check_username = login_list[0]["username"]
    check_password = login_list[0]["password"]
encr.file_encryption(file_inserted=LOGIN_FILE)


print("Welcome back! Type in your user and password.")
login_username = input("Type in your username: ")
login_password = getpass.getpass("Type in your password (hidden): ")


attempt:int = 0
while(login_username != check_username or login.hash_password(login_password) != check_password):
    print("\nYour username or password is incorrect. Try again.")
    attempt += 1
    print(f"Your number of attempt: {attempt}. If you reach 3. The app will close.")


    if attempt == 3:
        print("Too many attempts. The system will close.")
        sys.exit()


    login_username = input("Type in your username: ")
    login_password = getpass.getpass("Type in your password (hidden): ")




print(f"\nWelcome, {login_username}. You are logged in")


#Displays each page 
while True:
    #Displays the greeting, the option table, and input
    main_page.display_greeting()
    main_page.display_main_menu()
    menu_input = main_page.menu_input()


    while menu_input not in {"1", "2", "3", "4"}:
        menu_input = main_page.menu_validation(menu_input)


    #Sends the user to destination and main menu
    match menu_input:
        case "1":
            print("You selected: View Passwords\n")
            password_viewer_channel()
            if(return_to_menu() == "N"):
                print("The program will now close.")
                break
        case "2":
            print("You selected: Create Passwords\n")
            password_creation_channel()
            if(return_to_menu() == "N"):
                print("The program will now close.")
                break
        case "3":
            print("You selected: Delete Passwords\n")
            password_deletion_channel()
            if(return_to_menu() == "N"):
                print("The program will now close.")
                break
        case "4":
            print("You selected: Exit Program")
            print("The program will now close.")
            sys.exit()
        case _:
            print("Invalid input. The system will close.")
            sys.exit()