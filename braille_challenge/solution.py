def solution(plaintext):
    sometext = list("The quick brown fox jumps over the lazy dog".lower())
    braille = "011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
    braille_coding = []
    for i in range(0, len(braille), 6):
        braille_coding.append(braille[i:i+6])
    
    braille_dictionary = dict(zip(sometext, braille_coding))
    plaintext_coding = []
    for i in plaintext:
        if i.isupper():
            plaintext_coding.append("000001")
            plaintext_coding.append(braille_dictionary.get(i.lower()))
        else:
            plaintext_coding.append(braille_dictionary.get(i))
    
    print(''.join(plaintext_coding))

solution("CoDe up")