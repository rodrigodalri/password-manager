import sqlite3
from hashlib import sha256
from mnemonic import Mnemonic

def create_mnemonic(language,master_password):
    mnemo = Mnemonic(language)
    n_words = mnemo.generate(strength=256)
    seed = mnemo.to_seed(n_words, passphrase=master_password)
    entropy = mnemo.to_entropy(n_words)   
    
    return (n_words,seed,entropy)

def add_user(conn,name,master_password):
    
    n_words, seed, entropy = create_mnemonic("english",master_password)
    print("Save the 24 words in offline world:")
    print(f"{n_words}\n")
    
    conn.execute('''
            CREATE TABLE OWNER (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                master TEXT NOT NULL,
                n_words TEXT NOT NULL);''')      
    conn.execute("""
                INSERT INTO OWNER (name, master, n_words)
                VALUES (?, ?, ?)
                """, (name,master_password,n_words))  
    conn.commit() 
    print("Your identity has been saved!\nCongratulations!")

def update_user(conn,new_password):
    conn.execute("""
        UPDATE OWNER
        SET master = ?
        """, (new_password,))

    conn.commit()

def verify_user(master_password, password):
    return True if master_password == password else False

def verify_words(n_words,words):
    return True if n_words == words else False

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
        
        add_user(conn,name,master_password)
           

    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM OWNER;
        """)

    db_entry = cursor.fetchone()
    name = db_entry[1]
    master_password = db_entry[2]
    n_words = db_entry[3]
    
    password = input("Please enter the master password: ")
    while not verify_user(master_password, password):
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
            response = verify_words(n_words,words)
            if response:
                print("Yours 24 words are corrects!")
                new_password = input("Now, please enter your new master password: \n")
                update_user(conn,new_password)
            else:
                print("Sorry, but yours words doesn't match!\nBye Bye")

        #TODO save password
        elif input_ == "2":
            service = input("What is the name of the service?\n")
            service_password = input("What is the password of the service?\n")
            
        #TODO read password      
        elif input_ == "3":
            service = input("What is the name of the service?\n")
            
                
        elif input_ == "4":
            break
            
        else:
            print("Wrong input, please try again")

if __name__== "__main__":
    main()