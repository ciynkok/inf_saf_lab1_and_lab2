# from pydoc import plaintext


def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    # PUT YOUR CODE HERE
    ciphertext = ''
    f = lambda n: n - 65 if 64 < n <= 90 else n - 97 if 96 < n <= 122 else 0
    i = 0
    for l in range(len(plaintext)):
        num = ord(plaintext[l])
        if i >= len(keyword):
            i = 0
        sh = f(ord(keyword[i]))
        if f(num) + sh > 25:
            ciphertext += chr(num - (26 - sh))
        else:
            ciphertext += chr(num + sh)
        i += 1

    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE
    plaintext = ''
    f = lambda n: n - 65 if 64 < n <= 90 else n - 97 if 96 < n <= 122 else 0
    i = 0
    for l in range(len(ciphertext)):
        num = ord(ciphertext[l])
        if i >= len(keyword):
            i = 0
        sh = f(ord(keyword[i]))
        if f(num) - sh < 0:
            plaintext += chr(num + (26 - sh))
        else:
            plaintext += chr(num - sh)
        i += 1
    return plaintext
