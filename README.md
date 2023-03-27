# Python-Password-Manager

Introduction:

This code is the source code for a simple password manager written in python. It is a console-based application, so it runs in the python prompt. Because of this,
in order to run the application you would need to have python installed on your machine. Other than that, it doesn't have any external dependancies (so no modules and
no libraries).


Summary:

The password manager allows users to create an account for the password manager, log in and out of that account, save account credentials in their own password vault,
remove credentials if they don't want to have them stored anymore (or they made a typo or something) en delete their user account if they choose to not use the password manager anymore. 


Limitations and security notice:

Be aware that this password manager is not meant for serious use as it does not implement any method for permanent storage (so the user accounts don't get saved between runs and the saved passwords don't even get saved between logins), nor does it implement any measures for security other than the account credentials (so the only security measure is the fact that you need an existing username and password that are of the same user to login). This program was only meant as a personal project and not as a consumer-grade software.


Overview program:

The program starts off by asking users whether they want to create a new account or log into an existing account. This account is the account for the password manager. If the user chooses to create an account, they would need to enter a username and a password. The program checks the validity of the username and password so that the user hasn't for example entered a space for either the username or password or both. After creating their account, the program returns to the main menu where it again asks the user whether they want to create a new password manager account or log into an existing one. After choosing to log in the program checks the credentials and logs the user in. After logging into their recently created account, users can store their passwords (along with the name of the account and the username) in their own so-called 'password vault' (the password vault is an object with a list instance variable, so really they're being stored in that list). The users can add credentials to their password vault, remove them, log in and out of their password manager account and delete their password manager account. After choosing to add an account to the password vault, the program asks the user to enter the name of the platform that the credentials are for, the username and the password of the account they're about to save in the list. After putting in all the information, the program creates a dictionary with the username as a key and the password as value and creates a tuple with the account name as first item and the dictionary as the second item, it then proceeds to add the tuple to the list mentioned before. This list is constantly displayed while using the program within the logged in state. After choosing to remove an account from the list the program proceeds to ask the user for the account name, after the user puts in the account name, the program removes the tuple where the first item matches the input from the list. After choosing to log out, the program returns to the main menu. After choosing to delete their account, the program asks the user if they're sure of their decision, if the user enters anything other than 'y' or 'n', the question repeats, if they enter 'n', the program just logs them out, if they enter 'y', the program deletes their credentials from the storage and logs them out. 


Structure:

The code is divided into multiple classes and functions. There are classes for instantiating user accounts, 'password vaults' (which are meant to save the credentials of accounts users decide to save in the password manager) and saved accounts in the password vault. There are functions to handle creating and deleting user accounts, logging in and out, entering and removing credentials in and from the list that stores them and the various menu's the program has. 


minimum python version required to run code: unknown, code made and tested in python 3.9
