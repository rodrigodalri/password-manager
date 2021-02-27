from libs.db import connect_db, get_user_info
from libs.user import update_user, verify_user 
from libs.crypto import password_encrypt, verify_words
from libs.services import add_password, update_password, read_password, service_exists, list_services

def recover_master(conn,n_words):
    """[summary]

    Args:
        conn ([type]): [description]
        n_words ([type]): [description]
    """
    words = input("What is yours 24 words in order?\n")
    response = verify_words(n_words=n_words,words=words)
    if response:
        print("Yours 24 words are corrects!")
        new_password = input("Now, please enter your new master password: \n")
        update_user(conn=conn,new_password=new_password)
    else:
        print("Sorry, but yours words doesn't match!\nBye Bye")
        
def save_new_password(conn,master_password):
    """[summary]

    Args:
        conn ([type]): [description]
        master_password ([type]): [description]
    """
    service_name = input("What is the name of the service?\n")
    service_password = input("What is the password of the service?\n")
    if service_exists(conn=conn,service_name=service_name):   
        print(f"Service {service_name} already exists. Now, enter the new password:")     
        update_password(conn=conn,service_name=service_name,service_password=service_password,master_password=master_password)
    else:
        add_password(conn=conn,service_name=service_name,service_password=service_password,master_password=master_password)
    
def get_stored_password(conn,master_password):
    """[summary]

    Args:
        conn ([type]): [description]
        master_password ([type]): [description]
    """
    service_name = input("What is the name of the service?\n")
    if service_exists(conn=conn,service_name=service_name): 
        service_password = read_password(conn=conn,service_name=service_name,master_password=master_password)
        print(f"Your {service_name} password is: {service_password}")
    else:
        print(f"Service {service_name} not found in database!")
        
def list_stored_services(conn):
    """[summary]

    Args:
        conn ([type]): [description]
    """
    services = list_services(conn=conn)
    for service in services:
        print(f"Service: {service}")

def cli_interface(conn,name,master_password,n_words):
    
    print(f"Welcome Back sir {name}!")
        
    while True:
        print("--------------------------------------------")
        print("Commands:")
        print("Press 1 : to recover your master password")
        print("Press 2 : to save a new password")
        print("Press 3 : to get a stored password")
        print("Press 4 : to list all stored services")
        print("Press 5 : to quit")
        print("--------------------------------------------")

        input_ = input("Enter: ")

        if input_ == "1":
            recover_master(conn=conn,n_words=n_words)

        elif input_ == "2":
            save_new_password(conn=conn,master_password=master_password)
                 
        elif input_ == "3":
            get_stored_password(conn=conn,master_password=master_password)
        
        elif input_ == "4":
            list_stored_services(conn=conn)
        
        elif input_ == "5":
            print(f"Good Bye sir {name}!")
            break
            
        else:
            print("Wrong input, please try again")
         
def main():
    
    conn = connect_db() 
    name,master_password,n_words = get_user_info(conn=conn)
    
    password = input("Please enter the master password: ")
    while not verify_user(master_password=master_password,password=password):
        print("Invalid password\n")
        password = input("Please enter the master password: ") 
    
    cli_interface(conn,name,master_password,n_words)

if __name__== "__main__":
    main()