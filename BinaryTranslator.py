"""
This program translates real text into binary using ASCII codes
Nadeem Elsayed September 23, 2024
Translating fr om binary to real text will be added later
"""
import Translate
def main():
    str_or_bin = input("Do you want to enter binary or String characters? (b/c): ").lower()
    if str_or_bin == 'b':
        #take in as string
        bin_str = scan_bin()
        translation = Translate.binary_to_String(bin_str)
        print("The character equivalent is", translation)
        
    elif str_or_bin == 'c':
        char_str = input("Enter the String you want to translate: ")
        translation = Translate.String_to_binary(char_str)
        print("The binary equivalent is", translation)
    else:
        print("Invalid Input")
        return

#checks that the given string contains only numbers
def scan_bin():
    valid = False
    while valid == False:
        try:
            string = input("Enter a binary value")
            integer = int(string.replace(" ", ""))
            valid = True
            return integer
        except ValueError:
            continue
main()