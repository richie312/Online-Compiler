def caesar_cipher(s, k):
	output = ""
	for c in s:
		if c.isupper():
			output += chr(((ord(c) + k - 65) % 26) + 65)
		elif c.islower():
			output += chr(((ord(c) + k - 97) % 26) + 97)
		else:
			output += c
	return output


if __name__ == '__main__':
	cipherTxt1 = caesar_cipher("I am testing my skill on skillsz", 9)
	cipherTxt2 = caesar_cipher("Python on linux is the best combination among other possible alternatives", 20)
	print(cipherTxt1)
	print(cipherTxt2)