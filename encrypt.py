import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.ciphers.algorithms import SEED

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from file import window_input, openFile, openFiles


def SEED():
    # filepath = openFile()
    # f = open(filepath, "r")
    # content=f.read()
    # f.close()
    # content=content.encode()
    # print(content)
    # b = len(content)
    # if(b%16!=0):
    #    while(b%16!=0):
    #         content += " ".encode()
    # key = os.urandom(16)
    # iv = os.urandom(16)
    # backend = default_backend
    # cipher = Cipher(algorithms.SEED(key), modes.CBC(iv), backend = backend)
    # encryptor = cipher.encryptor()
    # ct = encryptor.update(content) + encryptor.finalize()
    # print(content, ct)
    iv = os.urandom(16)
    key = SEED.key_size()
    filepath = openFile()
    f = open(filepath, "r")
    content = f.read()
    content = content.encode()
    print(content)
    
    
    
    

def CAMELLIA():
    filepath = openFile()
    f = open(filepath, "r")
    content=f.read()
    f.close()
    content=content.encode()
    b=len(content)
    if(b%16!=0):
       while(b%16!=0):
            content += " ".encode()
    key = os.urandom(16)
    iv = os.urandom(16)
    backend = default_backend()
    cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ct = encryptor.update(content) + encryptor.finalize()
    print(content, ct)


def AESalgo():
    key = AESGCM.generate_key(bit_length=128)
    iv = os.urandom(16)
    aad = b'authenticated but encrypted data'
    return key, iv, aad

# def key_encrypt(plaintext, key, iv, add): 

def FernetEnc():
    key = Fernet.generate_key()
    return key
 
def encryptGCM(key, iv, aad):
    filepath = openFile()
    f = open(filepath, "r")
    content = f.read()
    f.close()
    content = content.encode('utf-8')
    cipher = AESGCM(key)
    ciphertext = cipher.encrypt(iv,content,aad)
    print(content, ciphertext)
    
def encryptFernet(key):
    filepath = openFile()
    f = open(filepath, "r")
    content = f.read()
    f.close()
    content = content.encode('utf-8')
    cipher = Fernet(key)
    encoded = cipher.encrypt(content)
    print(content, encoded)
    
    

def main():
    # key, iv , aad = AESalgo() 
    # encryptFile(key, iv, aad)
    
    print("Choose your encryption, bitches!")
    print("1 - AESGCM \n 2 - Fernet \n 3 - SEED \n 4 - CAMELLIA")
    choice = int(input())
    if(choice == 1):
        key, iv, aad = AESalgo()
        encryptGCM(key,iv,aad)
    if(choice==2):
        key = FernetEnc()
        encryptFernet(key)    
    if(choice==3):
        SEED()
    if(choice==4):
        CAMELLIA()

    
main()

    


    
