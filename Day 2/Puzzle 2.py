from utility import Utility


utility = Utility()
passwords = []

for value in utility.inputs:
	length, password = value.split(':')
	limit, letter = length.split(' ')
	minium, maxium = limit.split('-')

	password_letters = list(password)
	password_letters.remove(' ')

	if letter == password_letters[(int(minium) - 1)] and letter != password_letters[(int(maxium) - 1)]:
		passwords.append(value)
	elif letter == password_letters[(int(maxium) - 1)] and letter != password_letters[(int(minium) - 1)]:
		passwords.append(value)

print(len(passwords))
print(len(utility.inputs))