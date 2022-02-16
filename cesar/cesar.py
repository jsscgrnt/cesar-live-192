from string import ascii_lowercase
import string
from tkinter import N

def encripta(string: frase, int: n=13) -> string:
    """encrypt phrase

    Parameters
    ----------
    string : frase
        phrase to be encrypted
    int : n, optional
        number used to encrypt phrase, by default 13

    Returns
    -------
    string
        returns encripted string
    """
    encriptado = ''
    for l in frase:
        l = l.lower()
        if l == ' ':
            encriptado += 1
        elif l not in ascii_lowercase: ...
        else:
            pos = ascii_lowercase.find(l) + n
            l = ascii_lowercase[pos % 26]
            encriptado += l
    return encriptado

def decripta(string: frase, int: n=13) -> string:
    """decrypted phrase

    Parameters
    ----------
    string : frase
        phrase to be decrypted
    int : n, optional
        number used to encrypt phrase, by default 13

    Returns
    -------
    string
        returns decrypted string
    """
    decriptado = ''
    for l in frase:
        l = l.lower()
        if l == ' ':
            decriptado += l
        elif l not in ascii_lowercase: ...
        else:
            pos = ascii_lowercase.find(l) - n
            l = ascii_lowercase[pos % 26]
            decriptado += l
    return decriptado