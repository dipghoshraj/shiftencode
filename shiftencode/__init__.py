from .Algorithem import  *

def encrypt(message, salt):
    return shift_encrypt(message, salt)

def decrypt(message, salt):
    return shift_decrypt(message, salt)

def validator(message, salt, verifier):
    return verify(message, salt, verifier)