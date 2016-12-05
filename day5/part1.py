import hashlib

code = b'abbhdwsy'
index = 0
password = []

while len(password) < 8:
	h = hashlib.md5()
	h.update(code)
	h.update(bytes(str(index), 'utf-8'))
	hashed = h.hexdigest()
	if hashed[0:5] == '00000':
		password.append(hashed[5])

	index = index + 1

print(''.join(password))
input()
