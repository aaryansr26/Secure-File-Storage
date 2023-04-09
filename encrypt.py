import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.fernet import Fernet
from file import window_input, openFile, openFiles
from Keys import * 



# AES Encryption 
def AESEncrypt(filepath, key , nonce):
    aad = b'authenticated but unencrypted'
    f = open(filepath, "r")
    content = f.read()
    f.close()
    content = content.encode('utf-8')
    encryptor = AESGCM(key)
    ciphertext = encryptor.encrypt(nonce, content, aad)
    return ciphertext

# ChaChaPoly Encryption
def ChaChaPolyencrypt(filepath, key, nonce):
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    data = data.encode('utf-8')
    aad = b"authenticated but unencrypted data"
    encryptor = ChaCha20Poly1305(key)
    ciphertext = encryptor.encrypt(nonce, data, aad)
    return ciphertext

# Fernet Encryption
def FernetEncrypt(filepath, key):
    f = open(filepath, "r")
    content = f.read()
    content = content.encode('utf-8')
    f = Fernet(key)
    ciphertext = f.encrypt(content)
    return ciphertext

# File Creation 
def fileCreate(ciphertext, category):
    if not os.path.exists("EncryptedFiles"):
        os.mkdir("EncryptedFiles")
        if category == "AES":
            with open("EncryptedFiles/AES.txt", "wb") as f:
                f.write(ciphertext)
        elif category == "ChaChaPoly":
            with open("EncryptedFiles/ChaChaPoly.txt", "wb") as f:
                f.write(ciphertext)
        elif category == "Fernet":
            with open("EncryptedFiles/Fernet.txt", "wb") as f:
                f.write(ciphertext)
    else: 
        if category == "AES":
            with open("EncryptedFiles/AES.txt", "wb") as f:
                f.write(ciphertext)
        elif category == "ChaChaPoly":
            with open("EncryptedFiles/ChaChaPoly.txt", "wb") as f:
                f.write(ciphertext)
        elif category == "Fernet":
            with open("EncryptedFiles/Fernet.txt", "wb") as f:
                f.write(ciphertext)
        
# Generate Keys 
def generateKeys():
    f = open("EncryptedKeys.txt","w")    
    for key in key_list:
        f.write("{} \n".format(key))

# Encryption Function
def encryption():
    filepath = openFile()
    AESct = AESEncrypt(filepath,key = AESGCMKey , nonce= nonce_12)
    ChaChact = ChaChaPolyencrypt(filepath, key = ChaChaPolyKey, nonce = nonce_12) 
    Fernetct = FernetEncrypt(filepath, key = FernetKey) 
    fileCreate(AESct, "AES")
    fileCreate(ChaChact, "ChaChaPoly")
    fileCreate(Fernetct, "Fernet")  
    print("Encryption Successful!")
    listdir = os.listdir("EncryptedFiles")
    for file in listdir: 
        with open("EncryptedFiles/" + file, "rb") as f:
            print(f.read())
    
    

def main():
    generateKeys()
    encryption()
    
main()

    


