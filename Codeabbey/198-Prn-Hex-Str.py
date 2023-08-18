def convert_to_hex_string(text):
    result = ""
    for char in text:
        ascii_code = ord(char)
        if ascii_code >> 4 == 0:
            break  # Stop on encountering new-line or carriage-return
        hex_representation = "{:02X}".format(ascii_code)
        result += hex_representation
    return result

# Read input from the user
input_text = input()

# Convert and print the hex representation
output_hex = convert_to_hex_string(input_text)
print(output_hex)
