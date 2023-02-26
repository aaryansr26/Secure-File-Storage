from cryptography.fernet import Fernet
key = Fernet.generate_key()

fernet = Fernet(key)
file = open('Ananya M .jpg', 'rb')
original_file = file.read()
encrypted = fernet.encrypt(original_file)
file = open('encrypted Ananya M .jpg', 'wb')
file.write(encrypted)
file.close()

#Decrypting
fernet = Fernet(key)
file = open('encrypted Ananya M .jpg', 'rb')
encrypted_file = file.read()
decrypted = fernet.decrypt(encrypted_file)
file = open('decrypted Ananya M .jpg', 'wb')
file.write(decrypted)
file.close()
