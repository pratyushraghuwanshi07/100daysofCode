#Caesar Cipher Code
#also read the comments below

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

#TODO-3: What happens if the user enters a number/symbol/space?
#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#e.g. start_text = "meet me at 3"
#end_text = "•••• •• •• 3"

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = 0
while count == 0:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    def caesar(text, shift, direction):
        final_output = ""
        if shift > 26:
            shift = shift%26
        if direction == "encode":
            for i in range(len(text)):
                if text[i] in alphabet:
                    if (alphabet.index(text[i]) + shift) < len(alphabet):
                        final_output += alphabet[alphabet.index(text[i]) + shift]
                    else:
                        final_output += alphabet[alphabet.index(text[i]) + shift - 26]
                else:
                    final_output += text[i]
            print(f"The encrypted string is {final_output}")
    
        elif direction == "decode":
            for i in range(len(text)):
                if text[i] in alphabet:
                    final_output += alphabet[alphabet.index(text[i]) - shift]
                else:
                    final_output += text[i]
            print(f"The decrypted string is {final_output}")
    
        else:
            print("Select encode or decode!!")
            
        
    caesar(text=text, shift=shift, direction=direction)
    
    start_again = input("Do you want to restart the cipher program?Type yes or no: ").lower()
    if start_again == "yes":
        continue;
    else:
        count == 1
        break;






