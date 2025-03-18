def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    ciphertext = ''
    for l in plaintext:
        num = ord(l)
        if 64 < num <= 87 or 96 < num <= 119:
            ciphertext += chr(ord(l) + 3)
        elif 87 < num <= 90 or 119 < num <= 122:
            ciphertext += chr(ord(l) - 23)
        else:
            ciphertext += l
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    plaintext = ''
    for l in ciphertext:
        num = ord(l)
        if 67 < num <= 90 or 99 < num <= 122:
            plaintext += chr(ord(l) - 3)
        elif 64 < num <= 67 or 96 < num <= 99:
            plaintext+= chr(ord(l) + 23)
        else:
            plaintext += l
    return plaintext
