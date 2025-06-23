from cryptography.fernet import Fernet
import json
import os


DATA_FILE: str = "passwords.json"
KEY_FILE: str = "password_key.key"


class EncryptionManager:


    #Method to intialize the key and Fernet class
    def __init__(self):
        

        #Creates the file containing the key if it doesn't exist
        if not os.path.exists(KEY_FILE):
            self.key = Fernet.generate_key()
            with open(KEY_FILE, "wb") as key_file:
                key_file.write(self.key)
        else:
            with open(KEY_FILE, "rb") as key_file:
                self.key = key_file.read()


        self.fernet = Fernet(self.key)


    #Method to encrypt the JSON files by rewriting it
    def file_encryption(self, file_inserted):
        try: 
            with open(file_inserted, "r") as file:
                original_data = json.load(file)

        
            json_string : str = json.dumps(original_data)
            json_bytes = json_string.encode()
            

            encrypted_data = self.fernet.encrypt(json_bytes)


            with open(file_inserted, "wb") as file:
                file.write(encrypted_data)


        except Exception as e:
            print(e)
    
    #Method to decrypt the file by rewriting to its original format
    def file_decryption(self, file_inserted):
        try:
            with open(file_inserted, "rb") as file:
                encrypted = file.read()


            decrypted_bytes = self.fernet.decrypt(encrypted)
            decrypted_string = decrypted_bytes.decode()
            data = json.loads(decrypted_string)

            
            with open(file_inserted, "w") as file:
                json.dump(data, file, indent=4)


        except Exception as e:
            print(e)

