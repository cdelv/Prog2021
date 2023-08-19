Code = {
' ': '11',             'e': '101',
't': '1001',           'o': '10001',
'n': '10000',          'a': '011',
's': '0101',           'i': '01001',
'r': '01000',          'h': '0011',
'd': '00101',          'l': '001001',
'!': '001000',         'u': '00011',
'c': '000101',         'f': '000100',
'm': '000011',         'p': '0000101',
'g': '0000100',        'w': '0000011',
'b': '0000010',        'y': '0000001',
'v': '00000001',       'j': '000000001',
'k': '0000000001',     'x': '00000000001',
'q': '000000000001',   'z': '000000000000'}

Code = {v: k for k, v in Code.items()}

message = input() 
binary_stream = []

# Convert each base-32 character to 5-bit binary representation
for char in message:
    binary_stream.append(bin(int(char, 32))[2:].zfill(5))

binary_stream = ''.join(binary_stream)

# Traverse the binary tree using the chunks of 8 bits
decoded_message = []
start = 0

for i in range(start, len(binary_stream)):
    if binary_stream[start:i] in Code.keys():
        decoded_message.append(Code[binary_stream[start:i]])
        start = i

print(''.join(decoded_message))