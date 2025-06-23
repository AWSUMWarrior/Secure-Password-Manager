import json
import os 
from encryption_manager import EncryptionManager


DATA_FILE: str = "passwords.json"


class PasswordViewer:


    def __init__(self):
        self.user_information = []
        self.encr = EncryptionManager()


    #Method to get information from the JSON into a list
    def get_user_info(self) -> list:
        if not os.path.exists(DATA_FILE):
            self.user_information = []


            with open(DATA_FILE, "w") as file:
                json.dump(self.user_information, file, indent=4)
            self.encr.file_encryption(file_inserted=DATA_FILE)


        self.encr.file_decryption(file_inserted=DATA_FILE)
        with open(DATA_FILE, "r") as file:
            self.user_information = json.load(file)
        self.encr.file_encryption(file_inserted=DATA_FILE)
            
    
        copy_user_info = self.user_information
        return copy_user_info
    

    #Method to update class' user info file
    def update_user_info(self, user_info: list):
        self.user_information = user_info
        
    
    #Method to check if the user info file is empty
    def check_empty_user_info(self) -> bool:
        not_empty_list: bool = len(self.user_information) != 0
        if not_empty_list:
            return False

        print("                This is the Passwords Table:                  ")
        print("--------------------------------------------------------------")
        print(f"| {'#':<4} | {'Domain':<15} | {'Username':<15} | {'Password':<15} |")
        print("--------------------------------------------------------------")
        print("                     You have no data                         ")
        
        print("\nYou have no data to display and delete.")
        print("Make sure to create passwords.")
        return True


    #Method to list down user information in a list down
    def password_viewer(self):
        

        file_doesnt_exist: bool = not os.path.exists(DATA_FILE)
        if file_doesnt_exist:
            print("You do not have a passwords file\n")
            print_table: bool = self.check_empty_user_info()
            return
        

        self.user_information = self.get_user_info() 
        list_status = self.check_empty_user_info()


        if list_status:
            return


        print("")
        print("                This is the Passwords Table:                  ")
        print("--------------------------------------------------------------")
        print(f"| {'#':<4} | {'Domain':<15} | {'Username':<15} | {'Password':<15} |")
        print("--------------------------------------------------------------")
     

        num: int = 1
        for info in self.user_information:
            print(f"| {num:<3}. | {info['domain']:<15} | {info['username']:<15} | {info['password']:<15} |")
            num = num + 1
