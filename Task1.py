#1st import os.path,json and regex

from os.path import exists
import json
import re


email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
START_DELIMETER = "\n\n###############\n"
END_DELIMETER = "\n###############\n\n"


class FileDatabase:
    def __init__(self) -> None:
        self.users = dict()
        
        if exists("./USERS.data"):
            with open("./USERS.data") as reader:
                try:
                    self.users = json.loads(reader.read())
                except json.decoder.JSONDecodeError:
                    pass
        else:
            with open("./USERS.data", "w") as _:
                pass
            
    def save(self):
        with open("./USERS.data", "w") as writer:
            json.dump(self.users, writer)
            
    def write_new_user_data(self, username, password) -> None:
        if self.check_user_exists(username):
            return False
        
        self.users[username] = password
        self.save()
        
        return True
    
    def check_user_exists(self, username) -> bool:
        return username in self.users
    
    def update_user_exists(self,username, password) -> bool:
        if self.check_user_exists(username):
            self.users[username] = password
            self.save()
            return True
        
        return False
    def login(self, username, password) ->bool:
        if username in self.users and self.users[username] == password:
            return True
        
        return False
    
class inputData:
    def username_input(self) -> str:
        valid_email = False
        
        while not valid_email:
            username = input(
                "Enter a valid username (email) or Enter EXIT to go back to menu: ").strip()
            valid_email = re.fullmatch(email_regex, username)
            
            if username == "EXIT":
                break
            
            if valid_email:
                return username
            else:
                print_message("ENTER A VALID USERNAME (EMAIL)")
                
        return username if username == "EXIT" else None
    
    def password_input(self) -> str:
        return input("Enter the password: ").strip()
    
def print_message(message):
    print(START_DELIMETER + message + END_DELIMETER)
    
def main():
    f = FileDatabase()
    inp = inputData()
    
    while True:
        print("1)New Account\n2)Login\n3)Forget Password\n4)EXIT\n")
        user_choice = None
        
        try:
            user_choice = int(input("Enter your choice: ").strip())
            
            if user_choice == 1:
                username = inp.username_input()
                
                if username == "EXIT":
                    print_message("CANCLED")
                    
                elif username:
                    password = inp.password_input()
                    user_creation_status = f.write_new_user_data(username, password)
                    
                    if user_creation_status:
                        print_message("USER CREATED SUCCESSFULL")
                    else:
                        print_message("USERNAME ALREADY EXISTS")
                        
                else:
                    print_message("ENTER VALID DETAILS")
                    
            elif user_choice == 2:
                username == inp.username_input()
                
                if username == "EXIT":
                    print_message("CANCLED")
                    
                elif username:
                    password = inp.password_input()
                    login_status = f.login(username, password)
                    
                    if login_status:
                        print_message("LOGIN SUCCESSFUL")
                    else:
                        print_message("INVALID CREDS")
                else:
                    print_message("ENTER VALID DETAILS")
                    
            elif user_choice == 3:
                username = inp.username_input()
                
                if username:
                    user_check = f.check_user_exists(username=username)
                    
                    if user_check:
                        password = input("Enter Your current password: ")
                        creds_check = f.login(username, password)
                        
                        if creds_check:
                            while True:
                                new_password = input("Enter a new password: ")
                                
                                if new_password == input("Enter the new password again: "):
                                    f.update_user_password(
                                        username, new_password)
                                    break
                                else:
                                    print_message(
                                        "Password do not match.Enter the password again!!!")
                                    
                            print_message(
                                "PASSWORD UPDATED SUCCESSFULLY for USER: " + username)
                        else:
                            print_message("INVALID CREDENTIALS")
                    else:
                        print_message("USER DOSE NOT EXISTS")
                            
                else:
                    print_message("ENTER A VALID USERNAME")
                    
            elif user_choice == 4:
                break
            else:
                print_message("1) Please enter a number from above menu!!!!!")
        except Exception as e:
            print_message("2) Please enter a number from above menu!!!!!")
            
    print_message("Think you using my login system :)")
        
if __name__ == "__main__":
    main()
        
    
                                        