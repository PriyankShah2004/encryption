def encrypt(words, shift):
    ans = ""
    for i in range (len(words)):
        ch = words[i]
        if 'a' <= ch <= 'z':
            ans += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z' :
            ans += chr((ord(ch) - ord('A') + shift)%26 + ord('A'))
        else:
            ans += ch
    return ans
        
message = encrypt("Priyank Shah", 3)
print(message)            