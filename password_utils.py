from cryptography.fernet import Fernet

class fakestr(str):
    def __str__(self):
        return "*****"
    def __repr__(self):
        return "*****"


def load_key():
    return open("secret.key","rb").read()

def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return fakestr(decrypted)

def get_decrypted_password():
    encrypted_password='gAAAAABqffVNIPp9AqHjmSRNKsqcszpy9dQfb_j7n9T2zZwshV7dsmmZ_dCNBHdBv4W64GNz4FIn27CNtHrbGfrxhjcMKsXeHA=='
    return decrypt_password(encrypted_password)