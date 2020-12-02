from utility import Utility


utility = Utility()

lengths = []
passwords = []

test_input = ['2-9 c: ccccccccc', '1-3 b: cdefg', '1-3 a: abcde']

for value in utility.inputs:
	length, password = value.split(':')
	limit, letter = length.split(' ')
	minium, maxium = limit.split('-')

	password_letters = list(password)
	password_letters.remove(' ')

	correct_passwords = []
	for symbol in password_letters:
		appernce = password_letters.count(symbol)

		if symbol == str(letter) and value not in passwords:
			if appernce >= int(minium) and appernce <= int(maxium):
				passwords.append(value)

print(len(passwords))
print(len(utility.inputs))