class MainPage:


    # Method to greet the user and guides it to use the options
    def display_greeting(self):
        print("\nHello! Welcome to your password manager!")
        print("Please select from the following options:\n")


    # Method to display the main page listing all the options
    def display_main_menu(self):
        print("------------------------")
        print("| [1] View Passwords   |")
        print("------------------------")
        print("| [2] Create Passwords |")
        print("------------------------")
        print("| [3] Delete Passwords |")
        print("------------------------")
        print("| [4] Exit Program     |")
        print("------------------------")


    #Method to check the user input again in case of invalid input
    def menu_validation(self, user_input) -> str:
        print("Invalid options! Try again")
        user_input = input("\nType in your option: ")
        return user_input

    
    #Method to get user input
    def menu_input(self)-> str:
        user_input = input("\nType in your option: ")
        return user_input


