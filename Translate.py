#This function translates one character
def binary_to_String(binstr):
    bin_list = binstr.split()
    char_list = []
    for bit in bin_list:
        char_list.append(chr(int(bit)))
    return ''.join(char_list)
    


def String_to_binary(charstr):
    char_list = list(charstr)
    bin_list = []
    for char in char_list:
        bin_list.append(str(ord(char)))
    return ' '.join(bin_list)