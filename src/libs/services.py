from libs.crypto import password_decrypt, password_encrypt

def add_password(conn, service_name: str, service_password: str, master_password: str):
    """[summary]

    Args:
        conn
        service_name (str): [description]
        service_password (str): [description]
        master_password (str): [description]
    """
    encypted_password = password_encrypt(service_password.encode(), master_password)
    conn.execute("""
                INSERT INTO KEYS (service, hash)
                VALUES (?, ?)
                """, (service_name,encypted_password))  
    conn.commit() 
    print(f"Your password from {service_name} has been saved!\nCongratulations!")

def update_password(conn, service_name: str, service_password: str, master_password: str):
    """[summary]

    Args:
        conn
        service_name (str): [description]
        service_password (str): [description]
        master_password (str): [description]
    """
    encypted_password = password_encrypt(service_password.encode(), master_password)
    conn.execute("""
        UPDATE KEYS
        SET hash = ? WHERE service=?
        """, (encypted_password,service_name,))

    conn.commit()
    print(f"Your password from {service_name} has been saved!\nCongratulations!")
    
def read_password(conn, service_name: str, master_password: str) -> str:
    """[summary]

    Args:
        conn: [description]
        service_name (str): [description]
        master_password (str): [description]

    Returns:
        str: [description]
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM KEYS WHERE service=?", (service_name,))

    row = cursor.fetchone()
    token = row[2]
    
    return password_decrypt(token, master_password).decode()

def service_exists(conn, service_name: str, master_password: str) -> bool:
    """[summary]

    Args:
        conn ([type]): [description]
        service_name (str): [description]
        master_password (str): [description]

    Returns:
        bool: [description]
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM KEYS WHERE service=?", (service_name,))

    row = cursor.fetchone()
    return row != None