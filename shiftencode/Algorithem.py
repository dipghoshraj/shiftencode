from .sftascii import *


def shift_encrypt(keyword, salt):
    salt_avg  = avgsalt(salt)
    _word = ascii_(keyword)

    _key_encrypt =[]

    for word in _word:
        encrypt_key =str(word + salt_avg) + "se"    
        _key_encrypt.append(encrypt_key)
    word = ''.join(_key_encrypt)
    encrypt_word = "sftend" + word
    return encrypt_word
    

def shift_decrypt(keyword, salt):
    salt_avg  = avgsalt(salt)
    word = keyword.split("sftend")[1]

    values_list = word.split("se")
    word_list =[]

    for value in values_list:
        if value != "":
            org_asi = int(value) - salt_avg
            word_list.append(chr(org_asi))
            
    org_word = ''.join(word_list)
    return org_word

def verify(keyword, salt, verifier):
    decryptor = shift_decrypt(keyword, salt)
    if verifier == decryptor:
        return True
    return False