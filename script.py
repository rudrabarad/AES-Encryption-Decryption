from Crypto import Random                               # installing dependencies
from Crypto.Cipher import AES
import os.path
import time
#pycryptodome
class Encryptor:
    def __init__(self, key):                            # constructor in which key is passed as argument
        self.key = key                                  # key used will be string

    def pad(self, s):                                   # padding since data may not be multiple of AES Block Size i.e. 16
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):      # function to encrypt the data
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)          # iv = initialization vector
        cipher = AES.new(key, AES.MODE_CBC, iv)         # iv is random string of block size
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):                  # function to encrypt the file
        with open(file_name, 'rb') as fo:               # to open file in binary read mode
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:      # to create file with same name but with .enc extension
            fo.write(enc)                               # writing encrypted data
        os.remove(file_name)                            # to delete the original file

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]                # separating iv from cipher text
        cipher = AES.new(key, AES.MODE_CBC, iv)         # cbc = cipher block chaining
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])     # decrypting the cipher text
        return plaintext.rstrip(b"\0")                  # removing the additional padding

    def decrypt_file(self, file_name):                  # function to decrypt the file
        with open(file_name, 'rb') as fo:               # read the data
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:          # after decrypting it will store data in original file
            fo.write(dec)
        os.remove(file_name)                            # to delete encrypted file

    def getAllFiles(self, folder_name):
        dirs = []
        for dirName, subdirList, fileList in os.walk(folder_name):
            for fname in fileList:
                if (fname != 'script.py' and fname != 'data.txt.enc'):
                    dirs.append(dirName + "\\" + fname)
        return dirs

    def encrypt_all_files(self, folder_name):
        dirs = self.getAllFiles(folder_name)
        for file_name in dirs:
            self.encrypt_file(file_name)

    def decrypt_all_files(self, folder_name):
        dirs = self.getAllFiles(folder_name)
        for file_name in dirs:
            self.decrypt_file(file_name)



def aes_encryption_decryption():

    while True:
        print("\n1. Press '1' to Encrypt a file.\n"
              "2. Press '2' to Decrypt a file.\n"
              "3. Press '3' to Encrypt all the files in a directory.\n"
              "4. Press '4' to Decrypt all the files in a directory.\n"
              "5. Press '5' to Exit.\n"
              )
        choice = input("Please Enter your Choice : ")
        if choice == "1":
            file=input("\nEnter the name of a file to Encrypt: ")
            time.sleep(2)
            enc.encrypt_file(str(file))
            print(file + " is ENCRYPTED.......100%")
            time.sleep(2)
        elif choice == "2":
            file = input("\nEnter the name of a file to Decrypt: ")
            enc.decrypt_file(str(file))
            time.sleep(2)
            print(file + " is DECRYPTED.......100%")
            time.sleep(2)
        elif choice == "3":
            dir = input("\nEnter name of the directory to Encrypt: ")
            time.sleep(2)
            enc.encrypt_all_files(str(dir))
            print("All the files in "+ dir + " are ENCRYPTED.......100%")
            time.sleep(2)
        elif choice == "4":
            dir = input("\nEnter name of the directory to Decrypt: ")
            time.sleep(2)
            enc.decrypt_all_files(str(dir))
            print("All the files in "+ dir + " are DECRYPTED.......100%")
            time.sleep(2)

        elif choice == "5":
            exit()
        else:
            print("\nPlease select a valid option!")





key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)

print("\n| AES ENCRYPTION AND DECRYPTION\n|\n| Prepared by\n| 18DCS007 - RUDRA BARAD")
aes_encryption_decryption()