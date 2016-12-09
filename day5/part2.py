import hashlib
import os

os.system('cls')

code = b'abbhdwsy'
index = 0
password = [None, None, None, None, None, None, None, None]

print('Decrypting...')
print('|'.join([' '] * 8))
while None in password:
    h = hashlib.md5()
    h.update(code)
    h.update(bytes(str(index), 'utf-8'))
    hashed = h.hexdigest()
    index += 1

    if hashed[0:5] == '00000':
        if not hashed[5].isdigit():
            continue
        pos = int(hashed[5])
        if pos < 0 or pos >= len(password):
            continue
        if password[pos] == None:
            password[pos] = hashed[6]
        print('\033[2;' + str((pos * 2) + 1) + 'H' + password[pos])

print('Ta-da! Your password is:', ''.join(password))
input()
