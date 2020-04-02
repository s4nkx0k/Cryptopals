import binascii 
from binascii import hexlify


def repeated_KeyXOR(s,key):

    return bytes(s[i] ^ key[i % len(key)] for i in range(len(s))) # using a circular key
    



def main():

    input = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal".encode() #convert ascii to bytes
    
    key = "ICE".encode()
    
    msg = repeated_KeyXOR(input,key)

    print("Message: "+str(hexlify(msg)))
    

if __name__ == "__main__":
    main() 