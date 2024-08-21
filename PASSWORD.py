import hashlib
import getpass
graphical_password_options = ["Tree", "Mountain", "River", "Sun"]
def check_textual_password(stored_password_hash, input_password):
    input_password_hash = hashlib.sha256(input_password.encode()).hexdigest()
    return stored_password_hash == input_password_hash
def check_graphical_password(stored_choice, user_choice):
    return stored_choice == user_choice
def authenticate():
    stored_password_hash = hashlib.sha256("GITAM".encode()).hexdigest()  
    stored_graphical_choice = "Mountain"  
    
    print("** Welcome to the Two-Level Password System **")
 
    input_password = getpass.getpass("Enter your textual password: ")  
    if not check_textual_password(stored_password_hash, input_password):
        print("Textual password incorrect!")
        return False
    print("Textual password verified.")
    print("\nSelect your graphical password from the options below:")
    for idx, option in enumerate(graphical_password_options, 1):
        print(f"{idx}. {option}")
    graphical_choice = int(input("Enter the number corresponding to your graphical choice: "))
    if not check_graphical_password(stored_graphical_choice, graphical_password_options[graphical_choice - 1]):
        print("Graphical password incorrect!")
        return False
    print("Graphical password verified.")
    
    print("\nAuthentication Successful! Welcome!")
    return True
if authenticate():
    print("\nAccess Granted!")
else:
    print("\nAccess Denied!")
