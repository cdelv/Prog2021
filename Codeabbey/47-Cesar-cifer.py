import string

def encrypt(msg_count, key):
    alphabet = string.ascii_uppercase
    alphabet_shifted = alphabet[key:] + alphabet[:key]
    caesar_shift = str.maketrans(alphabet, alphabet_shifted)
    answer = []

    for msg in range(msg_count):
        unencrypted_msg = input()
        encrypted_msg = unencrypted_msg.translate(caesar_shift)
        answer.append(encrypted_msg)
    print(' '.join(answer))

def decrypt(msg_count, key):
    key = 26 - key
    alphabet = string.ascii_uppercase
    alphabet_shifted = alphabet[key:] + alphabet[:key]
    caesar_shift = str.maketrans(alphabet, alphabet_shifted)
    answer = []

    for msg in range(msg_count):
        unencrypted_msg = input()
        encrypted_msg = unencrypted_msg.translate(caesar_shift)
        answer.append(encrypted_msg)
    print(' '.join(answer))

def caesar_cipher():
    encrypted_msg_count, shift_key = [int(x) for x in input().split()]
    decrypt(encrypted_msg_count, shift_key)
    #encrypt(encrypted_msg_count, shift_key)
caesar_cipher()