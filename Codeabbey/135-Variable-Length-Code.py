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

message = input()
encoding = []

for letter in message:
    encoding.append(Code[letter])

chunk_size = 8
chunks = [''.join(encoding)[i:i+chunk_size] for i in range(0, len(''.join(encoding)), chunk_size)]
if len(chunks[-1]) < chunk_size:
    chunks[-1] = chunks[-1].ljust(chunk_size, '0')

hex_chunks = [hex(int(chunk, 2))[2:].zfill(2).upper() for chunk in chunks]
print(' '.join(hex_chunks))