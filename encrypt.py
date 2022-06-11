import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import file

def AESalgo():
    key = AESGCM.generate_key(bit_length=128)
    iv = os.urandom(12)
    aad = b'authenticated but encrypted data'
    return key, iv, aad

# def key_encrypt(plaintext, key, iv, add):
    
def AESGCM_encrypt(plaintext):
    aad = b'authenticated but encrypted data'
    iv = os.urandom(12) #96-bit initialization vector
    key = AESGCM.generate_key(bit_length=128)    #128-bit key
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(iv, plaintext, aad)
    return ciphertext, iv, key

def decrypt(ciphertext,key,iv):
    aad = b'authenticated but encrypted data'
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(iv, ciphertext, aad) 
    return plaintext




    
