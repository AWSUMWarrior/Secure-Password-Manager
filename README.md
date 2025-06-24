# Secure Password Manager
 A beginner-friendly, CLI-based password manager application built using the Python programming language. The app has secure login authentication, random password generation, password strength evaluation, and data encryption.

## Features and Security:
* **Login Authentication:** Uses SHA-256 hashing on login password and hides it from being displayed.
* **Encryption:** All login information and user credentials are encrypted using Fernet module.
* **Secure Storage:** Passwords and login info are stored in JSON files with constant encryption per operation.
* **Random Password Generator:** Generates strong password using customizable length and varied character types (upper/lowercase, digits, and symbols).
* **Password Strength Evaluator:** Estimates passwords based on a scoring system to encourage creating stronger passwords. 
* **Beginner-friendly:** Straightforward menu navigation and prompts.
* **Input Validation:** Integrates input validation to follow format and length rules.
* **Password Display:** Displays username and passwords in an organized and secure table format.
* **Password Deletion:** Removes entries by row input.

## Installation and Usage:

#### 1. Clone the Repo:
```bash
git clone https://github.com/AWSUMWarrior/Secure-Password-Manager.git
cd Secure-Password-Manager
```

#### 2. Install Dependencies: 
```bash
pip install cryptography
```

#### 3. Run the Application:
```bash
py mainpage.py
```

#### 4. Create an Account:
First-time users will be prompted to create an account:
* Create an username.
* Create and confirm a password (**hidden in terminal**).

#### 5. Use the Menu to Navigate:
```bash
            ------------------------
            | [1] View Passwords   |
            ------------------------
            | [2] Create Passwords |
            ------------------------
            | [3] Delete Passwords |
            ------------------------
            | [4] Exit Program     |
            ------------------------
```

## What I Learned:
* Fundamentals of encryption and decryption
* Implementing user login authentication
* Input validation and secure file handling
* Python modular design and classes

## Notice:
The files needed (i.e. passwords.json) will be created once you've viewed or created passwords.
