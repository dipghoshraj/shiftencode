from .Algorithem import  *

def encrypt(keyword, salt):
    return shift_encrypt(keyword, salt)

def decrypt(keyword, salt):
    return shift_decrypt(keyword, salt)

def validator(keyword, salt, verifier):
    return verify(keyword, salt, verifier)