import sys

def password():
	passwd = input()
	if "12" == passwd:
		print('0')
		return 0
	else:
		print('1')
		return 1

password()