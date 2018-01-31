letter_values = {'a':1,
		'b':2,
		'c':3,
		'd':4,
  		'e':5,
		'f':6,
		'g':7,
		'h':8,
		'i':9,
		'j':10,
		'k':11,
		'l':12,
		'm':13,
		'n':14,
		'o':15,
		'p':16,
		'q':17,
		'r':18,
		's':19,
		't':20,
		'u':21,
		'v':22,
		'w':23,
		'x':24,
		'y':25,
		'z':26}

def get_ltr_value(letter):
    value = letter_values[letter]
    return value

def get_word_value(word):
    val = 0
    for l in word:
        val = val + get_ltr_value(l)
    return val



word = input("Please give me a word to add up ").lower() 
if word.isalpha():
    print("The word " + word + " adds up to " + str(get_word_value(word))) 
