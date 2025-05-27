def simple_substitution_cipher(text, key, language='english'):
    if language == 'english':
        original_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif language == 'russian':
        original_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    else:
        raise ValueError("Unsupported language. Supported languages are 'english' and 'russian'.")

    if len(key) != len(original_alphabet):
        raise ValueError("The length of the key must be equal to the length of the alphabet.")

    encrypted_text = ""
    for char in text:
        if char in original_alphabet:
            index = original_alphabet.index(char)
            encrypted_text += key[index]
        else:
            encrypted_text += char
    return encrypted_text


def simple_substitution_decipher(text, key, language='english'):
    if language == 'english':
        original_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif language == 'russian':
        original_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    else:
        raise ValueError("Unsupported language. Supported languages are 'english' and 'russian'.")

    if len(key) != len(original_alphabet):
        raise ValueError("The length of the key must be equal to the length of the alphabet.")

    decryption_key = ''.join(sorted(original_alphabet, key=lambda x: key.index(x)))

    decrypted_text = ""
    for char in text:
        if char in key:
            index = key.index(char)
            decrypted_text += original_alphabet[index]
        else:
            decrypted_text += char
    return decrypted_text


def main():
    language = input("Выберите язык (английский или русский): ").lower()
    if language not in ['english', 'russian']:
        print("Неподдерживаемый язык.")
        return

    key = input("Введите ключ: ")
    if len(set(key)) != len(key):
        print("Ключ не должен содержать повторяющихся букв.")
        return

    choice = input("Выберите операцию:\n1. Зашифровать текст\n2. Расшифровать текст\nВведите номер операции: ")
    if choice == '1':
        text = input("Введите текст для шифрования: ")
        encrypted_text = simple_substitution_cipher(text, key, language)
        print("Зашифрованный текст:", encrypted_text)
    elif choice == '2':
        text = input("Введите текст для расшифровки: ")
        decrypted_text = simple_substitution_decipher(text, key, language)
        print("Расшифрованный текст:", decrypted_text)
    else:
        print("Некорректный выбор операции.")


if __name__ == "__main__":
    main()
