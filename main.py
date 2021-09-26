#add code to github

#Python code would (for each vote) 1) generate a new pseudorandom key 2) encrypt the vote with the key 3) store the key and encrypted vote
#link to prof.satt https://replit.com/join/xsamhhquar-daniellepark

#import string
#install pycrypto and pycryptodome

#homomorphism 
#does python have library for homomorphism 

#from Crypto.Cipher import AES
from Crypto.Cipher import AES
import binascii, os
import sys 

#from cryptography.fernet import Fernet
#import secrets
from datetime import datetime
def encrypt_AES_GCM(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(encryptedMsg, secretKey):
    (ciphertext, nonce, authTag) = encryptedMsg
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext
count1 = 0
count2 = 0
while True:
  
  vote = int(input("Vote 1 or 2:  "))  
  if vote == 1:
    count1 +=1
    msg=b'1'
  elif vote == 2:                     
    count2 += 1
    msg=b'2'
  else:
    sys.exit()
  #key = secrets.randbits(512)
 # f = Fernet(key)
 # f.encrypt(vote)
  # datetime object containing current date and time
  now = datetime.now()
  print("now =", now)
  secretKey = os.urandom(32)  # 256-bit random encryption key




  print("This is the 256-bit random key:")
  print(secretKey)
  print()
  print("This the Encryption key:", binascii.hexlify(secretKey))
  print()
  #msg = b'Message for AES-256-GCM + Scrypt encryption'
  print("This is the plaintext message:")
  print(msg)
  print()
  encryptedMsg = encrypt_AES_GCM(msg, secretKey)
  print("This is the encrypted message:")
  print()
  print({
    'ciphertext': binascii.hexlify(encryptedMsg[0]),
    'aesIV': binascii.hexlify(encryptedMsg[1]),
    'authTag': binascii.hexlify(encryptedMsg[2])
  })

  decryptedMsg = decrypt_AES_GCM(encryptedMsg, secretKey)
  print()
  print("This is the decrypted message:", decryptedMsg)
  # dd/mm/YY H:M:S
  dt_string = now.strftime("[%d/%m/%Y %H:%M:%S]")
  print("date and time =", dt_string)	
  print("you voted for ", count1)
  print("you voted for ", count2)
  f = open("election.txt", "a")
  f.write('\n')
  f.write(dt_string)
  f.write('\n')
  f.write(str(count1))
  f.write("/")
  f.write(str(count2))
  f.write('\n')
  f.write(str(binascii.hexlify(encryptedMsg[0])))
  f.write('\n')
  f.write(str(binascii.hexlify(secretKey)))
  f.write('\n')
  f.close() 

#1) The seed value is very significant in computer security to pseudo-randomly generate a secure secret encryption key. So using a custom seed value, you can initialize the robust and reliable pseudo-random number generator the way you want.

#2)
