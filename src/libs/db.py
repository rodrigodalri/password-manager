import sqlite3
from libs.user import add_user
from libs.crypto import password_decrypt, secret

def connect_db():
    """[summary]

    Returns:
        Connection: [description]
    """
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
        create_keys_table(conn=conn)
    
    return conn

def get_user_info(conn) -> (str,str,str):
    """[summary]

    Args:
        conn ([type]): [description]

    Returns:
        [str]: [description]
        [str]: [description]
        [str]: [description]
    """
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM OWNER;
        """)

    db_entry = cursor.fetchone()

    name = password_decrypt(token=db_entry[1],password=secret).decode() 
    master_password = password_decrypt(token=db_entry[2],password=secret).decode() 
    n_words = password_decrypt(token=db_entry[3],password=secret).decode() 
    
    return (name,master_password,n_words)

def create_keys_table(conn):
    """[summary]

    Args:
        conn ([type]): [description]
    """
    try:
        conn.execute('''
            CREATE TABLE KEYS (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL,
                hash TEXT NOT NULL);''') 
        print("Your safe has been created!\nWhat would you like to store in it today?")
    except:
        print("You have a safe, what would you like to do today?")