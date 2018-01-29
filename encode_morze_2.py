def encode_morze(text):
	morse_code = {
    "A" : "^_^^^", 
    "B" : "^^^_^_^_^", 
    "C" : "^^^_^_^^^_^", 
    "D" : "^^^_^_^", 
    "E" : "^", 
    "F" : "^_^_^^^_^", 
    "G" : "^^^_^^^_^", 
    "H" : "^_^_^_^", 
    "I" : "^_^", 
    "J" : "^_^^^_^^^_^^^", 
    "K" : "^^^_^_^^^", 
    "L" : "^_^^^_^_^", 
    "M" : "^^^_^^^", 
    "N" : "^^^_^", 
    "O" : "^^^_^^^_^^^", 
    "P" : "^_^^^_^^^_^", 
    "Q" : "^^^_^^^_^_^^^", 
    "R" : "^_^^^_^", 
    "S" : "^_^_^", 
    "T" : "^^^", 
    "U" : "^_^_^^^", 
    "V" : "^_^_^_^^^", 
    "W" : "^_^^^_^^^", 
    "X" : "^^^_^_^_^^^", 
    "Y" : "^^^_^_^^^_^^^", 
    "Z" : "^^^_^^^_^_^"
	}

	code = []
	if type(text) is not str:
		return ""

	text = text.split(" ")
	for word in text:
		new_word = []
		for letter in word:
			letter = letter.upper()
			if letter in morse_code:
				new_word.append(morse_code[letter])
			else:
				continue
		code.append("___".join(new_word))
	if len(code) > 1:
		code = "_______".join(code)
	else:
		code = "".join(code)

	return code

print(encode_morze("SOS SOSO"))