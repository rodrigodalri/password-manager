import secrets
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from mnemonic import Mnemonic

secret="ahsauhsuahsuahsuhau"

backend = default_backend()
iterations = 100_000

def create_mnemonic(language: str, master_password: str) -> (str,str,str):
    """[summary]

    Args:
        language (str, master_password): [description]
        str ([type]): [description]
        str ([type]): [description]

    Returns:
        [type]: [description]
    """
    mnemo = Mnemonic(language)
    n_words = mnemo.generate(strength=256)
    seed = mnemo.to_seed(n_words, passphrase=master_password)
    entropy = mnemo.to_entropy(n_words)   
    
    return (n_words,seed,entropy)

def verify_words(n_words: str, words: str) -> bool:
    """[summary]

    Args:
        n_words (str): [description]
        words (str): [description]

    Returns:
        bool: [description]
    """
    return n_words == words

def _derive_key(password: bytes, salt: bytes, iterations: int = iterations) -> bytes:
    """[summary]

    Args:
        password (bytes): [description]
        salt (bytes): [description]
        iterations (int, optional): [description]. Defaults to iterations.

    Returns:
        bytes: [description]
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt,
        iterations=iterations, backend=backend)
    
    return b64e(kdf.derive(password))

def password_encrypt(message: bytes, password: str, iterations: int = iterations) -> bytes:
    """[summary]

    Args:
        message (bytes): [description]
        password (str): [description]
        iterations (int, optional): [description]. Defaults to iterations.

    Returns:
        bytes: [description]
    """
    salt = secrets.token_bytes(16)
    key = _derive_key(password.encode(), salt, iterations)
    
    return b64e(
        b'%b%b%b' % (
            salt,
            iterations.to_bytes(4, 'big'),
            b64d(Fernet(key).encrypt(message)),
        )
    )

def password_decrypt(token: bytes, password: str) -> bytes:
    """[summary]

    Args:
        token (bytes): [description]
        password (str): [description]

    Returns:
        bytes: [description]
    """
    decoded = b64d(token)
    salt, iter, token = decoded[:16], decoded[16:20], b64e(decoded[20:])
    iterations = int.from_bytes(iter, 'big')
    key = _derive_key(password.encode(), salt, iterations)
   
    return Fernet(key).decrypt(token)