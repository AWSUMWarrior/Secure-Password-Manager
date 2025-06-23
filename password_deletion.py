import json
from password_viewer import PasswordViewer
from encryption_manager import EncryptionManager


DATA_FILE: str = "passwords.json"


class PasswordDeletion:


    #Method to delete a row of info
    def delete_info(self):


        viewer = PasswordViewer()
        copy_user_info = viewer.get_user_info()


        encr = EncryptionManager()


        if len(copy_user_info) > 0:
            viewer.password_viewer()
            print("\nThis is your to-be-edited table.")
            row_number: str = input("\nWhich row on the table do you want to delete?: ")
            row_number_int : int = int(row_number)
        elif len(copy_user_info) == 0:
            print("\nThere are no passwords to delete.")
            return
    

        while row_number_int <= 0 or row_number_int > len(copy_user_info):
            print("The number is out of range.")
            print("Please, pick a different number.") 
            row_number: str = input("\nWhich row on the table do you want to delete?: ")
            row_number_int : int = int(row_number)


        copy_user_info.pop(row_number_int-1)


        encr.file_decryption(file_inserted=DATA_FILE)
        with open(DATA_FILE, "w") as file:
            json.dump(copy_user_info, file, indent=4)
        encr.file_encryption(file_inserted=DATA_FILE)
        

        print("\nThis is your current table:")
        viewer.update_user_info(copy_user_info)
        viewer.password_viewer()
    

    #Method to repeat the password creation process
    def user_repeated_password_deletion(self):
        

        user_repeats: bool = True


        while user_repeats:
            repeat_input = input("\nDo you want to keep deleting passwords? (Y/N) : ").strip().upper()


            if repeat_input == "Y":
                self.delete_info()
            elif repeat_input == "N":
                user_repeats = False
            else:
                print("You typed in something that is not Y or N. Try again.")