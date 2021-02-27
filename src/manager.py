import sqlite3

from libs.user import add_user, update_user, verify_user 
from libs.crypto import password_decrypt, password_encrypt, verify_words, secret
from libs.services import add_password, update_password, read_password, service_exists

def main():
    
    try:
        conn = sqlite3.connect('file:db/fortknox.db?mode=rw', uri=True)
        first_acess = False
    except:
        conn = sqlite3.connect('db/fortknox.db')
        first_acess = True
    
    if first_acess:
        name = input("Please enter your name: ")
        master_password = input("Please chose your master password: ")        
        
        add_user(conn=conn,name=name,master_password=master_password)   

    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM OWNER;
        """)

    db_entry = cursor.fetchone()

    name = password_decrypt(token=db_entry[1],password=secret).decode() 
    master_password = password_decrypt(token=db_entry[2],password=secret).decode() 
    n_words = password_decrypt(token=db_entry[3],password=secret).decode() 
    
    password = input("Please enter the master password: ")
    while not verify_user(master_password=master_password,password=password):
        print("Invalid password\n")
        password = input("Please enter the master password: ") 
    
    print(f"Welcome Back sir {name}!")

    try:
        conn.execute('''
            CREATE TABLE KEYS (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL,
                hash TEXT NOT NULL);''') 
        print("Your safe has been created!\nWhat would you like to store in it today?")
    except:
        print("You have a safe, what would you like to do today?")
        
    while True:
        print("\n")
        print("Commands:")
        print("Press 1 : to recover your master password")
        print("Press 2 : to save a new password")
        print("Press 3 : to get a stored password")
        print("Press 4 : to quit")
        print("\n")
        input_ = input("Enter: ")

        if input_ == "1":
            words = input("What is yours 24 words in order?\n")
            response = verify_words(n_words=n_words,words=words)
            if response:
                print("Yours 24 words are corrects!")
                new_password = input("Now, please enter your new master password: \n")
                update_user(conn=conn,new_password=new_password)
            else:
                print("Sorry, but yours words doesn't match!\nBye Bye")

        elif input_ == "2":
            service_name = input("What is the name of the service?\n")
            service_password = input("What is the password of the service?\n")
            if service_exists(conn=conn,service_name=service_name,master_password=master_password):   
                print(f"Service {service_name} already exists. Now, enter the new password:")     
                update_password(conn=conn,service_name=service_name,service_password=service_password,master_password=master_password)
            else:
                add_password(conn=conn,service_name=service_name,service_password=service_password,master_password=master_password)
                 
        elif input_ == "3":
            service_name = input("What is the name of the service?\n")
            if service_exists(conn=conn,service_name=service_name,master_password=master_password): 
                service_password = read_password(conn=conn,service_name=service_name,master_password=master_password)
                print(f"Your {service_name} password is: {service_password}")
            else:
                print(f"Service {service_name} not found in database!")
        elif input_ == "4":
            break
            
        else:
            print("Wrong input, please try again")

if __name__== "__main__":
    main()