from Keys import *
from processing import split, merge
from encrypt import *
from decrypt import *
from file_checker import *
from threads import *
# import time 
import glob
from config import *
from aws_config import * 
  
def count_file(path):
    pattern  = path + "/*"
    file_paths = glob.glob(pattern)
    count = len(file_paths)
    print(count)
    return count
    

def main(): 
    config()
    generateKeys()
    path = openFile()
    [checker, extension] = is_media_file(path)
    if(checker):
        fernet_media(FernetKey, path)
        s3_upload()
        
    else:
        split(path)
        HybridCrypt()
        s3_upload()

    choice = input("Do you want to decode?")
    if choice == 'y':
        s3_download()
        count = count_file(os.path.join(os.getcwd() + '/EncryptedFiles'))
        if(count <= 1):
            fernet_media_decrypt(FernetKey, extension)
        else:
            AESdecrypt(AESGCMKey, nonce_12)
            ChaChadecrypt(ChaChaPolyKey, nonce_12)
            FernetDecrypt(FernetKey)
            MultiFernetDecrypt(MultiFernetK1, MultiFernetK2)
            merge()
           
main()
    
    