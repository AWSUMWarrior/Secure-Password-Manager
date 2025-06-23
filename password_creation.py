import json
from password_viewer import PasswordViewer
from password_features import PasswordFeatures
from encryption_manager import EncryptionManager


DATA_FILE: str = "passwords.json"


class PasswordCreation:


    # Creates a list and variables to store values
    def __init__(self):
        self.user_information = []
        self.viewer = PasswordViewer()
        self.features = PasswordFeatures()
        self.encr = EncryptionManager()


    #Method to validate domain input by user
    def domain_validation(self,domain: str) -> bool:
        blocked_characters: list = [ "/", "\\", "<", ">", ":", ";", "'", "|", "[", "]", "{", "}", "(", ")", "?", "=", "+", "*", "~", "!", "^", "%", "#"]
        

        if_domain_isnt_okay: bool = False
        for char in domain:
            if char in blocked_characters:
                print(f"ERROR: You have blocked characters: {char}. Try inputting again.")
                if_domain_isnt_okay = True
                break

        
        if len(domain) > 15:
            print("ERROR: Your domain is too long. Make sure it is less than 15 characters.")
            if_domain_isnt_okay = True
        elif len(domain) == 0:
            print("ERROR: Your domain is empty. Make sure it is less than 15 characters.")
        

        return if_domain_isnt_okay
    

    #Method to validate username input by user
    def username_validation(self,username:str) -> bool:
        blocked_characters: list = [ "/", "\\", "<", ">", ":", ";", "'", "|", "{", "}", "?", "=", "+", "*", "~", "!", "^", "%", "#"]
        username = username.strip()


        if_username_isnt_okay: bool = False
        for char in username:
            if char in blocked_characters:
                print(f"\nERROR: You have a blocked character: {char}. Try inputting again.")
                if_username_isnt_okay = True
                break
        

        if len(username) > 15:
            print("\nERROR: Your username is too long. Make sure it is less than 15 characters.")
            if_username_isnt_okay = True
        elif len(username) == 0:
            print("\nERROR: Your username is empty. Make sure it is between 1 through 15 characters.")
            if_username_isnt_okay = True


        return if_username_isnt_okay
    

    #Method to validate password input by user
    def password_validation(self,password:str) -> bool:
        blocked_characters: list = [ "/", "\\", "<", ">", ":", ";", "'", "|", "[", "]", "{", "}", "(", ")", "?", "=", "+", "~"]
        password = password.strip()


        if_password_isnt_okay: bool = False
        for char in password: 
            if char in blocked_characters:
                print(f"\nERROR: You have a blocked character: {char}. Try inputting again.")
                if_password_isnt_okay = True
                break


        if len(password) > 15:
            print("\nERROR: Your password is too long. Make sure it is less than 15 characters.")
            if_password_isnt_okay = True
        elif len(password) < 10:
            print("\nERROR: Your password is too short. Make sure it is between 10 and 15 characters.")
            if_password_isnt_okay = True


        return if_password_isnt_okay


    #Method to see if user wants their own password or a randomly generated one
    def choice_of_password(self, password_option: str) -> str:
        while(password_option != "1" and password_option != "2"):
                print("You didn't input 1 or 2. Try again")
                password_option: str = input("Press 1 for your own and press 2 for a randomly generated one: ")
                password_option.strip()
        

        if password_option == "1":
            input_password = input("Type in the password you will use (Max: 15 characters): ")
            while self.password_validation(password=input_password):
                input_password = input("Type in the password again (Max: 15 characters): ")
            self.features.password_strength_checker(password=input_password)


            user_repeat = "Y"
            while user_repeat != "N":
                user_repeat = input("Do you want to change your password? (Y/N): ").strip().upper()


                while user_repeat != "Y" and user_repeat != "N":
                    print("Your input is not either Y or N. Try again")
                    user_repeat = input("Do you want to change your password? (Y/N): ").strip().upper()
            

                if user_repeat == "Y":
                    input_password = input("Type in the password you will use (Max: 15 characters): ")
                    while self.password_validation(password=input_password):
                        input_password = input("Type in the password again (Max: 15 characters): ")
                    self.features.password_strength_checker(password=input_password)
                else:
                    continue
                

        elif password_option == "2":
            random_password = self.features.random_password_generator()
            input_password = random_password
                
        

        return input_password


    # Method to ask for user input and insert into list
    def input_information(self):
        print("")


        self.copy_user_info = self.viewer.get_user_info()


        input_domain = input("Type in the domain (website) the password is used for (Max: 15 characters): ")
        while self.domain_validation(domain=input_domain):
            input_domain = input("Type in the domain again (Max: 15 characters): ")



        input_username = input("Type in the username you will use (Max: 15 characters): ")
        while self.username_validation(username=input_username):
             input_username = input("Type in the username again (Max: 15 characters): ")


        print("\nDo you want to create your own password or randomly generate one?")
        print("\nRemember, passwords are recommended to be between 10 to 15 characters long")
        password_option: str = input("Press 1 for your own and press 2 for a randomly generated one: ")
        password_option.strip()


        input_password = self.choice_of_password(password_option=password_option)


        entry = {
            "domain": input_domain, 
            "username": input_username, 
            "password": input_password
            }
            

        self.copy_user_info.append(entry)
        self.viewer.update_user_info(self.copy_user_info)
    
    
    #Method to send information to the json file
    def password_file_insertion(self):
        self.encr.file_decryption(file_inserted=DATA_FILE)
        with open(DATA_FILE, "w") as file:
            json.dump(self.copy_user_info, file, indent=4)
        self.encr.file_encryption(file_inserted=DATA_FILE)


    #Method to display the information as a test
    def password_file_display(self):
        self.viewer.password_viewer()


    # Method to repeat the processes involved with password creatio
    def creation_process_repeated(self):
        self.password_file_display()
        self.input_information()
        self.password_file_insertion()
        self.password_file_display()


    #Method to repeat the password creation process based on user input
    def user_repeated_password_creation(self):


        user_repeats: bool = True


        while user_repeats:
            repeat_input = input("\nDo you want to keep creating passwords? (Y/N) : ").strip().upper()


            if repeat_input == "Y":
                self.creation_process_repeated()
            elif repeat_input == "N":
                user_repeats = False
            else:
                print("You typed in something that is not Y or N. Try again.")