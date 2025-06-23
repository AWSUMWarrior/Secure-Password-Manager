import random

class PasswordFeatures:

    UPPERCASE_LETTERS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOWERCASE_LETTERS: str = "abcdefghijklmnopqrstuvwxyz"
    DIGITS: str = "0123456789"
    SYMBOLS: str = "!@#$%^&*"


    #Method to validate user input for length
    def length_validation(self, user_input: str) -> bool:
        if_length_isnt_okay = False
        for char in user_input:
            if char not in self.DIGITS:
                print(f"You have an invalid character: {char}. Make sure you type a number (0-9).")
                if_length_isnt_okay = True
                break
        
        
        return if_length_isnt_okay


    
    #Method to create a random password
    def random_password_generator(self) -> str:
        password_characters = self.UPPERCASE_LETTERS + self.LOWERCASE_LETTERS + self.DIGITS + self.SYMBOLS
        password_length_string = input("\nHow long do you want the password? (The maximum is 15): ").strip()


        while self.length_validation(user_input=password_length_string):
            print("Type in the password again.")
            password_length_string = input("\nHow long do you want the password? (The maximum is 15): ").strip()


        password_length_int = int(password_length_string)


        while(password_length_int > 15 or password_length_int < 10):
            print("You either typed in more than 15 or less than 10. Input a new number.")


            password_length_string = input("\nHow long do you want the password? (The maximum is 15): ").strip()
            password_length_int = int(password_length_string)
        

        digits_and_symbols: list = [random.choice(self.DIGITS), random.choice(self.SYMBOLS)]
        remaining_chars: int  = password_length_int - len(digits_and_symbols)


        added_password = digits_and_symbols + random.choices(password_characters, k=remaining_chars)
        random.shuffle(added_password)

        
        computed_password = "".join(added_password)
        return computed_password
    

    #Method to find password strength
    def password_strength_checker(self, password: str):
        strength: int = 0


        for char in password:
            if char in self.UPPERCASE_LETTERS:
                strength += 2
            elif char in self.LOWERCASE_LETTERS:
                strength += 1
            elif char in self.DIGITS:
                strength += 3
            elif char in self.SYMBOLS:
                strength += 4
        

        match strength:
            case strength if 0 <= strength <= 9:
                print("You password is: Weak")
            case strength if 10 <= strength <= 19:
                print("Your password is: Average")
            case strength if 20 <= strength <= 29:
                print("Your password is: Strong")
            case strength if strength >= 30:
                print("Your password is: Very Strong")
            case _:
                print("Your password strength is invalid.")