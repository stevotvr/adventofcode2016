import hashlib

code = b'abbhdwsy'
index = 0
password = [None, None, None, None, None, None, None, None]

while None in password:
	h = hashlib.md5()
	h.update(code)
	h.update(bytes(str(index), 'utf-8'))
	hashed = h.hexdigest()
	index = index + 1

	if hashed[0:5] == '00000':
		if not hashed[5].isdigit():
			continue
		pos = int(hashed[5])
		if pos < 0 or pos >= len(password):
			continue
		if password[pos] == None:
			password[pos] = hashed[6]

print(''.join(password))
input()
