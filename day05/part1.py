import hashlib
import os

os.system('cls')

code = b'abbhdwsy'
index = 0
password = []

print('Decrypting...')
print(''.join(['_'] * 8))
while len(password) < 8:
    h = hashlib.md5()
    h.update(code)
    h.update(bytes(str(index), 'utf-8'))
    hashed = h.hexdigest()
    if hashed[0:5] == '00000':
        password.append(hashed[5])
        print('\033[2;1H' + ''.join(password))
 
    index += 1

print('Ta-da! Your password is:', ''.join(password))
input()
