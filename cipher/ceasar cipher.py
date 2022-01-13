#Python program for Caesar Cipher Technique
def encrypt(text,s):
    result = ""
 
    for i in range(len(text)):
        char = text[i]
 
        
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
 
text = input("Enter a plaintext : ")
s = int(input("Enter shift pattern (must be a digit) :"))

print ("Shift : " + str(s))
print ("Ciphertext: " + encrypt(text,s))
