import json
import hashlib
import getpass
from pathlib import Path
from encryption_manager import EncryptionManager
from password_features import PasswordFeatures

LOGIN_FILE = "login_authentication.json"

class LoginManager:

    def __init__(self):
        self.encr = EncryptionManager()
        self.features = PasswordFeatures()


    #Method to hash login password
    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()


    #Method to create a new login file for new users
    def login_creation(self):
        print("Hello! Welcome to your password manager!")
        print("You are new, so let's make an account!")


        login_list = []

        with open(LOGIN_FILE, "w") as file:
            json.dump(login_list, file, indent=4)


        user_username = input("Type in your desired username: ")
    
        
        user_repeat = "Y"
        while user_repeat == "Y":
            user_password = getpass.getpass("Type in your desired password (hidden): ")
            self.features.password_strength_checker(password=user_password)
            user_repeat = input("Do you want to change your password? (Y/N): ").strip().upper()
        

        entry = {
            "username": user_username,
            "password": self.hash_password(user_password)
        }


        print("\nUsername and password sucessfully saved!")
        print("\nMake sure to note this information down.")
        print("Login into your password manager.\n")


        login_list.append(entry)
        with open(LOGIN_FILE, "w") as file:
            json.dump(login_list, file, indent = 4)
        self.encr.file_encryption(file_inserted=LOGIN_FILE)
