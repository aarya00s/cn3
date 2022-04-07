
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# get the default backend
from cryptography.hazmat.backends import default_backend

# Generating the Secret Key
secret_key = "project3"
kdf = PBKDF2HMAC(
    algorithm=SHA256(),
    length=32,
    salt="aasharma".encode(),
    iterations=100000,
    backend=default_backend(),
)
key = urlsafe_b64encode(kdf.derive(secret_key.encode()))

# pass the key
val = Fernet(key)


def encrypt(data):
    return val.encrypt(data)


def decrypt(data):
    return val.decrypt(data)
