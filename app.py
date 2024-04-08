print("***Welcome to my encrypt machine***")
encrypted_text = ""
decoded_text = ""

while True:
    inp = int(input("Enter your choice number: \n\t1-Encript \n\t2-Decode \n\t3-Exit\n Enter: "))
    if(inp == 1):
        encrypt_inp = input("Enter your text: ")
        for i in range(0,len(encrypt_inp)):
            aski_num = ord(encrypt_inp[i])
            encrypted_text += chr(aski_num *6 +2)   
        print(f"Your encrypted text is: {encrypted_text}\n",end="")
        inp1 = input("Do you want to continue: y/n  ").lower()
        if(inp1 == 'y'):
            continue
        elif(inp1 == 'n'):
            break    
    elif(inp == 2):
        decode_text = input("Enter your text: ")
        for i in range(0,len(decode_text)):
            aski_num = ord(decode_text[i])
            decoded_num = (aski_num-2)//6
            decoded_text += chr(decoded_num)   
        print(f"Your decodeded text is: {decoded_text}\n",end="")
        inp2 = input("Do you want to continue: y/n  ").lower()
        if(inp2 == 'y'):
            continue
        elif(inp2 == 'n'):
            break  
    elif(inp == 3):
        break 
    else:
        print("your entry isn't correct, please enter a valid number :)")       