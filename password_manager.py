#! /usr/bin/env python3

from main import Users, Credentials

def create_user(main_user, main_password):
    """
    function for creating new user
    """
    new_usr = Users(main_user, main_password)
    return new_usr

def add_user(Users):
    """
    function for storing new user
    """
    Users.add_user()


def verify_user(main_user, main_password):
    """
    function to verify a user
    """
    confirm_user = Credentials.confirm_user(main_user, main_password)
    return confirm_user


def add_credentials(account, username, password):
    """
    function to create new credentials
    """
    new_cred = Credentials(account, username, password)
    return new_cred

def save_credential(credential):
    """
    Saves the new credentials
    """
    Credentials.save_credential(credential)


def create_random_password():
    """
    function that generates random passwords
    """
    create_pass = Credentials.create_random_password()
    return create_pass

def main():
    print("")
    print("Welcome to Kev-Keep, a passwords manager.")
    print("")
    print("What is your name?")
    person_name = input()
    print(f"Hello {person_name}. What would you like to do today? ")
    print('\n')
    while True:
        print("*"*30)
        print("Choose from these short codes: \n ca - create an account \n si - Sign In \n ex - Exit")
        print("*"*30)
        code= input().lower()
        
        if code == 'ca':
            print('Create a new account: ')
            print('New Username:')
            main_user=input()
            print('New Password:')
            main_password=input()

            add_user(create_user(main_user, main_password))
            print("")
            print(f"Account for {main_user} has been sucessfully created")
            print("")

        elif code == "si":
            print("Enter Username: ")
            
        
        elif code =='ex':
            break




if __name__ == '__main__':
	main()