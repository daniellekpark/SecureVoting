import binascii, os
import sys 
from Crypto.Cipher import AES
from datetime import datetime

def encrypt_AES_GCM(vote, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(vote)
    return (ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(encryptedVote, secretKey):
    (ciphertext, nonce, authTag) = encryptedVote
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

count1 = 0
count2 = 0
while True:
  vote = int(input("Vote 1 or 2:  "))  
  if vote == 1:
    count1 +=1
    vote=b'1'
  elif vote == 2:                     
    count2 += 1
    vote=b'2'
  else:
    sys.exit()
  now = datetime.now()
  print("now =", now)
  secretKey = os.urandom(32)  
  print("This is the 256-bit random key:")
  print(secretKey)
  print()
  print("This the Encryption key:", binascii.hexlify(secretKey))
  print()
  print("This is the plaintext vote:")
  print(vote)
  print()

  encryptedVote = encrypt_AES_GCM(vote, secretKey)
  print("This is the encrypted vote:")
  print()
  print({
    'ciphertext': binascii.hexlify(encryptedVote[0]),
    'aesIV': binascii.hexlify(encryptedVote[1]),
    'authTag': binascii.hexlify(encryptedVote[2])
  })
  decryptedVote = decrypt_AES_GCM(encryptedVote, secretKey)
  print()
  print("This is the decrypted vote:", decryptedVote)

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
  f.write(str(binascii.hexlify(encryptedVote[0])))
  f.write('\n')
  f.write(str(binascii.hexlify(secretKey)))
  f.write('\n')
  f.close() 
