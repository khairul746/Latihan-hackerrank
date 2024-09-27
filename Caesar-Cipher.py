import string

def CaesarCipher(s, k):
    abjad = string.ascii_lowercase
    cipherText = []
    for letter in s:
        if not letter.isalpha():
            cipherText.append(letter)
            continue
        if letter.isupper():
            letter = letter.lower()
            is_upper = True
        else:
            is_upper = False
        shifted_index = (abjad.index(letter) + k) % 26 
        shifted_letter = abjad[shifted_index]  
        if is_upper:  
            shifted_letter = shifted_letter.upper()
        cipherText.append(shifted_letter)
    return ''.join(cipherText)
s = 'Always-Look-on-the-Bright-Side-of-Life'
k = 5
print(CaesarCipher(s,k))
e = 'Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj'
print(e)        
