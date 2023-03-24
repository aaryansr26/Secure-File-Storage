import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.fernet import Fernet
from file import window_input, openFile, openFiles
from Keys import*


def AESEncrypt(filepath, key , nonce):
    aad = b'authenticated but unencrypted'
    f = open(filepath, "r")
    content = f.read()
    content = content.encode('utf-8')
    encryptor = AESGCM(key)
    ciphertext = encryptor.encrypt(nonce, content, aad)
    return ciphertext

def ChaChaPolyencrypt(filepath, key, nonce, ce):
    f = open("test2", 'r')
    data = f.read()
    f.close()
    datab = data.encode('utf-8')
    aad = b"authenticated but unencrypted data"
    key = ChaCha20Poly1305.generate_key()
    chacha = ChaCha20Poly1305(key)
    nonce = os.urandom(12)
    ce = chacha.encrypt(nonce, datab, aad)
    print(ce)
    cd = chacha.decrypt(nonce, ce, aad)
    print(cd)


def FernetEncrypt(filepath, key):
    f = open(filepath, "r")
    content = f.read()
    content = content.encode('utf-8')
    f = Fernet(key)
    ciphertext = f.encrypt(content)
    return ciphertext
    
    
def generateKeys():
    f = open("EncryptedKeys.txt","w")    
    for key in key_list:
        f.write("{} \n".format(key))

def encryption():
    filepath = openFile()
    AESct = AESEncrypt(filepath,key = AESGCMKey , nonce= AESnonce)
    f = open("AESenc.txt", "wb")
    f.write(AESct)

def main():
    # key, iv , aad = AESalgo() 
    # encryptFile(key, iv, aad)
    
    # print("Choose your encryption, bitches!")
    # print("1 - AESGCM \n 2 - Fernet \n 3 - SEED \n 4 - CAMELLIA")
    # choice = int(input())
    # if(choice == 1):
    #     key, iv, aad = AESalgo()
    #     encryptGCM(key,iv,aad)
    # if(choice==2):
    #     key = FernetEnc()
    #     encryptFernet(key)    
    generateKeys()
    encryption()
    
main()

    


