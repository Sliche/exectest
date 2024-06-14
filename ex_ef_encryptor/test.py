from cryptography.fernet import Fernet


class Encryptor:
    def __init__(self, secret_key=None):
        self.key = secret_key

    def generate_key(self):
        self.key = Fernet.generate_key()

    def encrypt_dict(self, data):
        if not self.key:
            raise ValueError("Key not generated. Call generate_key() first.")
        f = Fernet(self.key)
        serialized_data = str(data).encode('utf-8')
        encrypted_data = f.encrypt(serialized_data)
        encrypted_string = encrypted_data.decode('utf-8')
        return encrypted_string

    def decrypt_dict(self, encrypted_data):
        if not self.key:
            raise ValueError("Key not generated. Call generate_key() first.")
        f = Fernet(self.key)
        encrypted_data = encrypted_data.encode('utf-8')
        decrypted_data = f.decrypt(encrypted_data)
        serialized_data = decrypted_data.decode('utf-8')
        return eval(serialized_data)



key = Fernet.generate_key()
print(key)

enc = Encryptor(key)


data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Encrypt the data
encrypted_data = enc.encrypt_dict(data)
print("Encrypted Data:", type(encrypted_data))

decrypted_data = enc.decrypt_dict(encrypted_data)
print("Decrypted Data:", type(decrypted_data))
