import hashlib

#using 3 Functions
#1.deCryptor - Takes the wordlist.txt file hashes the each word and compares the our hash with wordlist.txt hash
#2.Main -  enables us to select the hash and options
#3.Banner - we can't use run time while using Google Colab, so this is put on hold

#def banner():
#    print("Banner")

#this hashes the word(passwrd list) with particular hash that we have selected
# SHA-256 and MD5
# Resources - https://www.geeksforgeeks.org/hashlib-module-in-python/
# methods -
# https://pypi.org/project/hashlib/
wordlist = open("wordlist.txt", "r")

def hash_decryptor(wordlist, given_hash, option):
    
    #hash_decryptor(wordlist, given_hash, option-( sha256, MD5))
    option = option.lower()

    for word in wordlist:
        word = word.strip()
        #choose any one of the following
        if option == "sha256":
            #choose sha256 hash
            h_object = hashlib.sha256(word.encode())
        elif option == "md5":
            h_object = hashlib.md5(word.encode())
        else:
            print("Unknown option", option)
            return 
        
        #hashes are done by hexdigest
        hashed_word = h_object.hexdigest()

        #For debugging    
        print(f"word: {word}:{hashed_word}")
        
        if given_hash == hashed_word:
            print("Password is: ", word)
            return
        
    print("Password not in list")
    return

# https://10015.io/tools/sha256-encrypt-decrypt 
# Online https://tools.keycdn.com/sha256-online-generator - amreen = 437fcdaa47644fe7bb816e21cb9031f3931747058f46816a036a64099c152ea8
# apple - 3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b
hash_decryptor(wordlist,"c7b2cb55a920e95f5c49e3331a49be027f9e402e81bbf38393b72d80e76158b9", "sha256")



