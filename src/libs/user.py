from libs.crypto import iterations, create_mnemonic, password_encrypt, secret

def add_user(conn, name: str, master_password: str):
    """[summary]

    Args:
        conn
        name (str): [description]
        master_password (str): [description]
    """
    n_words, seed, entropy = create_mnemonic("english",master_password)
    print("Save the 24 words in offline world:")
    print(f"{n_words}\n")
    
    encrypted_name = password_encrypt(message=name.encode(),password=secret,iterations=iterations)
    encrypted_n_words = password_encrypt(message=n_words.encode(),password=secret,iterations=iterations)
    encrypted_master_password = password_encrypt(message=master_password.encode(),password=secret,iterations=iterations)
    
    conn.execute('''
            CREATE TABLE OWNER (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                master_password TEXT NOT NULL,
                n_words TEXT NOT NULL);''')      
    conn.execute("""
                INSERT INTO OWNER (name, master_password, n_words)
                VALUES (?, ?, ?)
                """, (encrypted_name,encrypted_master_password,encrypted_n_words))  
    conn.commit() 
    print("Your identity has been saved!\nCongratulations!")

def update_user(conn, new_password: str):
    """[summary]

    Args:
        conn
        new_password (str): [description]
    """
    encrypted_new_password = password_encrypt(message=new_password.encode(),password="",iterations=iterations)
    conn.execute("""
        UPDATE OWNER
        SET master_password = ?
        """, (encrypted_new_password,))

    conn.commit()

def verify_user(master_password: str, password: str) -> bool:
    """[summary]

    Args:
        master_password (str): [description]
        password (str): [description]

    Returns:
        bool: [description]
    """
    return master_password == password