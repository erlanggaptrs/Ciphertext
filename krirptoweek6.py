alphabets = "abcdefghijklmnopqrstuvwxyzABCDEF"
def encrypt_caesar(num, text):
    results = ''
    
    for k in text.lower():
        try:
            i = (alphabets.index(k) + num) % 26
            results += alphabets[i]
        except ValueError:
            results += k
    return results.lower()
num = int(input("Please input the shift: ")) 
text = input("Please input the text: ")
ciphertext = encrypt_caesar(num,text)

print("Encoded Text: " + ciphertext)