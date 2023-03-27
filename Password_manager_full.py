"""this part of the code is meant for user registration, the accounts for the password manager (the platform accounts, not the ones stored in the manager)
are managed by the code starting from the 'users' list below up to and including the delete_account_confirmation function"""

users = [] #the 'users' list stores all the user accounts for the password manager
user = {} #the 'user' dict is 1 user account and is filled with the username as key and password as value, again, these are the accounts for the password manager itself,
          #not the ones stored in the passsword manager

class User:
    
    def __init__(self, username, password):
        self.username = username #username of the password manager account
        self.password = password #password of the password manager account

    def registration_check(self): #this method is meant to check the validity of the username and password and creates the user accounts by filling the 'user' dictionary and adding it to the 'users' list
        
        valid_contents = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890!@#$%^&*' #the username and password can only countain these characters,
                                                                                                  #no other characters, no spaces and the username and password
                                                                                                  #cannot be empty strings

        if all(i in valid_contents for i in self.username) and len(self.username) > 0 and not any(self.username in i for i in users):
            print('username valid')

                    
        if all(j in valid_contents for j in self.password) and len(self.password) > 0 and not any(self.username in i for i in users):
            print('password valid')

        
        if all(i in valid_contents for i in self.username) and all(j in valid_contents for j in self.password) and len(self.username) > 0 and len(self.password) > 0 and not any(self.username in i for i in users):
            print('user account created')
            user = {self.username:self.password}
            users.append(user)

        elif any(self.username in i for i in users):
            print('username already taken')

        else:
            print('username or password invalid')



"""the user class checks the validity of the username and password for the account for the password manager software, creates the accounts and adds them to the list,
in order to check the validity, it checks if both the username and password only contain characters in the 'valid_contents' string (so no spaces, for example), it also
checks if there is already a username key in any 'user' dictionary in the 'users' list that matches the 'username' input thats being evaluated, if there are only characters
in the username and password strings that match characters in the 'valid_contents' string and none of 'user' dictionaries in the 'users' list contain a 'username' key that
is the same as the 'username' input thats being evaluated, than the new account is created by filling the 'user' dictionary with the username as key and password as value
and adding that dictionary to the 'users' list"""



def create_account():
    username = input('enter a username: ')
    password = input('enter a password: ')

    user_test = User(username, password)
    user_test.registration_check()

"""this function is meant for the input of the username and password for the password manager accounts, it also instantiates the 'User' class and calls it's method"""



def login():
    global username_check
    global password_check
    
    username_check = input('enter username: ')
    password_check = input('enter password: ')

    global credentials_match
    credentials_match = False

    for user in users:
        for key, value in user.items():
            if key == username_check and value == password_check:
                print('logged in')
                credentials_match = True
                break
        if credentials_match == True:
            break
    if credentials_match == False:
        print('username and/or password incorrect')

"""this function is meant to allow the user to login to their existing password manager account, it prompts the user to input a username and password and if those
credentials match existing credentials and the existing credentials are in the same dictionary, then the login is successful"""



def delete_account(username_check, password_check):
    username_check_delete = input('enter username: ')
    password_check_delete = input('enter password: ')

    for i in range(len(users)):
        if username_check_delete == username_check:
            if password_check_delete == password_check:
                if users[i].get(username_check_delete) is not None:
                    if users[i][username_check_delete] == password_check_delete:
                        del users[i]
                        break
                    else:
                        print('username and password do not match')
                        break
            else:
                print('username and password do not match')
                break

        else:
            print('username and password do not match')
            break

"""this function is meant to allow the user to delete their password manager account, it does exactly the same as the login funtion, except that it checks if the
logged in user is the one whose account is about to be deleted, if the username and password match the logged in account then it deletes the dictionary"""



def delete_account_confirmation():
    while True:
        are_you_sure = input('You are about to delete your account, are you sure (y/n)?\n')

        if are_you_sure == 'y':
            delete_account(username_check, password_check)
            print('\n') 
            print(user) #print statements just for confirmation of successful test, to be removed
            print(users) #print statements just for confirmation of successful test, to be removed
            print('\n') 
            break
                            

        elif are_you_sure == 'n':
            print('\n') 
            print(user) #print statements just for confirmation of successful test, to be removed
            print(users) #print statements just for confirmation of successful test, to be removed
            print('\n') 
            break

        else:
            print('invalid input')

            print('\n') 
            print(user) #print statements just for confirmation of successful test, to be removed
            print(users) #print statements just for confirmation of successful test, to be removed
            print('\n')

"""all this function does is checking if the user is sure of their decision to delete their account and if so, it calls the function that does that"""





"""this is the password manager part of the code, from the class 'Account' up to and including the 'password_manager_main' function, this code does the work of
the password manager (by which i mean it does the actual password managing), the 'password_manager_main' function also includes a menu which checks what the users
would like to do after logging into their password manager account, this menu starts in the main function by asking for input but the password_manager_main
and account_menu_handling functions actually do things based on the input of the user"""


#a little introduction to all the variables and data structures used in this part of the code:

#saved_account: tuple with name of platform for which the credentials are saved and the credentialls themselves
#account_name: first item in saved_account tuple, name of the platform
#account_credentials: dict with credentials as key-value pair
#stored_username: key of the credentials dict
#stored_password: value of the credentials dict




class Account:

    def __init__(self, account_name, stored_username, stored_password, account_credentials):
        self.account_name = account_name #first item in saved_account tuple, name of the platform
        self.stored_username = stored_username #key of the credentials dict
        self.stored_password = stored_password #value of the credentials dict
        self.account_credentials = {stored_username:stored_password} #credentials dict
        self.saved_account = (account_name, account_credentials) #tuple for the name of the platform and the credentials

"""the 'Account' class only defines the various variables used in the password manager: the name of the platform the user would like to store the credentials for
(a string), the username of the account for which the credentails are stored in the password manager (a string), the password of the account for which the credentails 
are stored in the password manager (a string), the account_credentials dictionary where the username is the key and the password the value and the 
saved_account tuple which stores the name of the account and the account_credentials dictionary"""



class Password_vault:
    
    def __init__(self):
        self.stored_passwords = []

    def create_account_object(self, account_name, stored_username, stored_password, account_credentials):
        Account_obj = Account(account_name, stored_username, stored_password, account_credentials)
        return Account_obj

    def fill_vault(self, Account_obj):
        self.stored_passwords.append(Account_obj.saved_account)

"""the Password_vault class is responsible for the creation of the 'stored_passwords' list, which stores the 'saved_account' tuples, it also instantiates the 'Account'
class and adds the 'saved_account' tuple to the 'stored_passwords' list"""






def password_manager_main():
    
    global vault_test

    global account_menu_option

    global print_statement_stopper

    print_statement_stopper = False
    
    if account_menu_option == '1':
        account_name = input('Whats the name of the platform you would like to save your credentials for? ')
        stored_username = input('Enter the username of the account: ')
        stored_password = input('Enter the password of the account: ')

        account_credentials = {stored_username: stored_password}
        account_object = vault_test.create_account_object(account_name, stored_username, stored_password, account_credentials)
        vault_test.fill_vault(account_object)

        print_statement_stopper = True
            
        print('\n')    
        print(f"Account name: {account_name}")
        print(f"Username: {stored_username}")
        print(f"Password: {stored_password}")
        print(f"Paired credentials: {account_object.account_credentials}")
        print(f"Saved account: {account_object.saved_account}")
        print(f"Password_vault: {vault_test.stored_passwords}")
        print('\n')


    if account_menu_option == '2':
        account_name_to_delete = input('Enter the name of the platform of which you would like to delete the account from the vault: ')

        for i in vault_test.stored_passwords:
            if i[0] == account_name_to_delete:
                vault_test.stored_passwords.remove(i)

                print_statement_stopper = True
        
        
        print(f"Password_vault: {vault_test.stored_passwords}")
        print('\n')

"""this function checks if the input of 'account_menu_option' (defined in the main() function) has to do with the password managing part of the code (so either adding
a password (or rather a pair of credentials) to the vault or removing one), if so it prompts the user for some inputs and depending on what the input of 'account_menu_option'
was, it either asks the user for the platform name, username and password of the account they would like to store the credentials for, calls some methods and prints all of the
inputs and data structures or it asks the user for a platform name, removes the saved_account tuple where the platform name matches the input and prints just the stored_passwords
list"""







def account_menu_handling(account_menu_option):
    password_manager_main()

    if account_menu_option == '3':
        print('you are logged out')

        print('\n')
        print(user) #print statements just for confirmation of successful test, to be removed
        print(users) #print statements just for confirmation of successful test, to be removed
        print('\n')
        return 'break'
                    
                    
    elif account_menu_option == '4':
        delete_account_confirmation()
        return 'break'

    else:
        if print_statement_stopper == False:
            print('invalid input')

            print('\n')
            print(user) #print statements just for confirmation of successful test, to be removed
            print(users) #print statements just for confirmation of successful test, to be removed
            print('\n')

"""this function checks if the input of 'account_menu_option' (defined in the main() function) has to do with the user account managing part of the code and if so,
it either logs out the user that was logged in or calls the delete_account_confirmation() function, it also checks for any invalid input"""






def main():

    print('Welcome to Python Password Manager!')
    
    while True:
        main_menu_option = input('What would you like to do?\n[1] create an account\n[2] log in\n')

        if main_menu_option == '1':
            create_account()

            print('\n')
            print(user) #print statements just for confirmation of successful test, to be removed
            print(users) #print statements just for confirmation of successful test, to be removed
            print('\n')


        elif main_menu_option == '2':
            login()

            print('\n')
            print(user) #print statements just for confirmation of successful test, to be removed
            print(users) #print statements just for confirmation of successful test, to be removed
            print('\n')

            if credentials_match == True:

                global vault_test
                vault_test = Password_vault()

                while True:

                    global account_menu_option

                    account_menu_option = input('What would you like to do?\n[1] Save new account in vault\n[2] Delete account from vault (by platform name)\n[3] log out\n[4] delete user account\n')

                    
                    break_variable = account_menu_handling(account_menu_option)

                    if break_variable == 'break':
                        break

"""this function prompts the user for input for the main menu where the user has to either create an account or log into an existing one, it then proceeds to call functions
based on the input, it also instantiates the 'Password_vault' class and prompts the user for input for the account menu (the first menu that the user gets after logging in),
then it calls another function"""
                    


if __name__ == "__main__":
    main()
