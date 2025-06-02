# Nourhan Adel Mohamed El-Hady  
# Caroline Ayman Isaac          
# Fatma Nazeih Hanfy             

def decimal_to_binary(decimal_num):
    # To convert the number from decimal to binary
    binary = ""                                        # Empty string to store the Binary result
    while decimal_num > 0:                             # To make sure that the entered number is true
        remainder = decimal_num % 2
        binary = str(remainder) + binary               # Build the binary string in reverse
        decimal_num = decimal_num // 2
    return binary

def decimal_to_octal(decimal_num):
    # To convert the number from decimal to octal
    octal = ""                                         # Empty string to store the octal result
    while decimal_num > 0:                             # To make sure that the entered number is true
        remainder = decimal_num % 8
        octal = str(remainder) + octal                 # Build the octal string in reverse
        decimal_num = decimal_num // 8
    return octal

def octal_to_decimal(octal_num):
    # To convert the number from octal to decimal
    decimal_num = 0
    power = 0
    while octal_num > 0:                               # To make sure that the entered number is true
        digit = octal_num % 10
        decimal_num += digit * (8 ** power)
        power += 1
        octal_num //= 10
    return decimal_num

def decimal_to_hexadecimal(decimal_num):
    # To convert the number from decimal to hexadecimal
    hexadecimal_digits = "0123456789ABCDEF"           # List of valid hexadecimal characters
    hexadecimal = ""                                  # Empty string to store the hexadecimal result
    while decimal_num > 0:
        remainder = decimal_num % 16
        hexadecimal = hexadecimal_digits[remainder] + hexadecimal  # Append the corresponding hex digit (in reverse order)
        decimal_num //= 16
    return hexadecimal

def binary_to_decimal(binary_num):
    # To convert the number from binary to decimal
    decimal_num = 0
    power = 0
    for bit in binary_num[::-1]:  # Iterate through each binary digit in reverse order, starting from the least significant bit
        if bit == '1':
            decimal_num += 2 ** power
        power += 1
    return decimal_num

def hex_to_decimal(hex_num):
    # To convert the number from hexadecimal to decimal
    hex_digits = "0123456789ABCDEF"                  # List of valid hexadecimal characters
    hex_num = hex_num.upper()                        # Ensure consistent uppercase representation
    decimal_num = 0
    power = len(hex_num) - 1
    for digit in hex_num:
        decimal_num += hex_digits.index(digit) * (16 ** power)  # Convert each digit to its decimal value and add to the result
        power -= 1
    return decimal_num

def hexadecimal_to_octal(hex_num):
    # To convert the number from hexadecimal to octal
    decimal_num = hex_to_decimal(hex_num)                      # First convert to decimal
    if decimal_num is not None:                                # Proceed only if the decimal conversion was successful
        octal_number = decimal_to_octal(decimal_num)           # Convert decimal to octal
        return octal_number

def binary_to_hexadecimal(binary_num):
    # To convert the number from binary to hexadecimal
        decimal = 0
        power = 0
        for digit in reversed(binary_num):                    # Iterate through the binary digits in reverse order
            decimal += int(digit) * (2 ** power)
            power += 1
        hex_digits = "0123456789ABCDEF"                       # List of valid hexadecimal characters
        hexadecimal = ""                                      # Empty string to store the hexadecimal result
        while decimal > 0:
            remainder = decimal % 16
            hexadecimal = hex_digits[remainder] + hexadecimal
            decimal //= 16
        return hexadecimal


def binary_to_octal(binary):
    # To convert the number from binary to octal
    while len(binary) % 3 != 0:
        binary = '0' + binary                       # Add a leading zero if needed

    octal = ""
    i = 0
    while i < len(binary):
        bits = binary[i:i + 3]                      # Extract 3 bits at a time
        decimal = 0                                 # Temporary variable to hold decimal value of 3 bits
        power = 2                                   # Start with the first bit having a weight of 2^2

        for bit in bits:                            # Convert 3 bits to decimal
            decimal += int(bit) * (2 ** power)      # Add the weighted value of each bit
            power -= 1                              # Decrement power for the next bit

        octal += str(decimal)                       # Append the decimal equivalent (as an octal digit)
        i += 3                                      # Move to the next group of 3 bits

    return octal


def hex_to_binary(hexadecimal):
    # To convert the number from hexadecimal to binary
    hex_digits = "0123456789ABCDEF"                # List of valid hexadecimal characters
    binary = ""                                    # Empty string to store the hexadecimal result

    for digit in hexadecimal:                      # Iterate through each hexadecimal digit
        decimal = hex_digits.index(digit)          # Find the decimal equivalent of the current digit
        binary += bin(decimal)[2:].zfill(4)        # Convert decimal to binary and append to result, padding with zeros
    return binary

def octal_to_binary(octal):
    # To convert the number from octal to binary
    binary = ""  # Initialize the empty binary result string

    for digit in octal:
        decimal = 0
        power = 0
        # Convert octal digit to decimal:
        octal_digit = int(digit)  # Convert octal digit to integer
        while octal_digit != 0:
            remainder = octal_digit % 10
            decimal += remainder * (8 ** power)
            octal_digit //= 10
            power += 1
        # Convert decimal to binary (3 bits for each octal digit):
        binary_digit = ""  # Initialize string for binary representation of the decimal
        while decimal != 0:
            binary_digit = str(decimal % 2) + binary_digit  # Append binary digits in reverse order
            decimal //= 2
        binary += binary_digit.zfill(3)  # Add padded binary to the final result

    return binary

def octal_to_hexadecimal(octal_number):
    #Converts an octal number to its hexadecimal representation.
    decimal_num = octal_to_decimal(octal_number)  # First convert octal to decimal
    if decimal_num is not None:  # Proceed only if the decimal conversion was successful
        hexa_number = decimal_to_hexadecimal(decimal_num)  # Convert decimal to hexadecimal
        return hexa_number

def menu_1():
    #Displays the main menu with options to insert a new number or exit.

    print("** Numbering System Converter **")
    print("A) Insert new number")
    print("B) Exit")

def menu_2():
    #Displays a menu to select the base of the input number.

    print("** Please select the base you want to convert a number from **")
    print("A) Decimal")
    print("B) Binary")
    print("C) Octal")
    print("D) Hexadecimal")

def menu_3():
    #Displays a menu to select the desired base for the output number.

    print("** Please select the base you want to convert a number to **")
    print("A) Decimal")
    print("B) Binary")
    print("C) Octal")
    print("D) Hexadecimal")
while True:
    # Display the main menu and prompt for user choice
    menu_1()
    option = input("select a choice ( A/B ) :")

    if option == "A": # Insert a new number
        num_1 = input("please insert a number: ")

        while True:
            # Display the base selection menu
            menu_2()
            option_2 = input("select a choice( A/B/C/D ) :")

            if option_2 == "A":  # from decimal
               dec = [str(i) for i in range(10)] # Valid decimal digits
               for digit in str(num_1):
                   if digit not in dec:
                      print("ERROR: please insert a valid number")
                      break   # Exit the loop if invalid input
               else:  # If all digits are valid
                   while True:
                       # Display the target base selection menu
                       menu_3()
                       option_3 = input("select a choice ( A/B/C/D ) :")
                       if option_3 == "A":  # to decimal
                          print("The result =",int(num_1))
                          break
                       elif option_3 == "B":  #to binary
                          print("The result = ", decimal_to_binary(int(num_1)))
                          break
                       elif option_3 == "C":  #to octal
                          print("The result = ",decimal_to_octal(int(num_1)))
                          break
                       elif option_3 == "D":  #to hexadecimal
                          print("The result = ",decimal_to_hexadecimal(int(num_1)))
                          break
                       else:
                          print("please insert a valid choice ")
                          continue
                   break  # Exit the loop after conversion
            elif option_2 == "B":  # from binary
                bin_digits = {'0', '1'}  # Set of valid binary digits
                for bit in num_1:  # Validate each digit of the input number
                    if bit not in bin_digits:  # If a non-binary digit is found
                        print("ERROR: please insert a valid number")
                        break
                else:  # If all digits are valid
                    while True:
                        # Display the target base selection menu
                        menu_3()
                        option_3 = input("select a choice ( A/B/C/D) :")
                        if option_3 == "A":  # to decimal
                            print("The result = ",binary_to_decimal(num_1))
                            break
                        elif option_3 == "B":  # to binary
                            print("The result = ",num_1)
                            break
                        elif option_3 == "C":  #to octal
                            print("The result = ",binary_to_octal(num_1))
                            break
                        elif option_3 == "D":  # to hexadecimal
                            print("The result = ",binary_to_hexadecimal(num_1))
                            break
                        else:
                            print("please insert a valid choice ")
                            continue
                    break  # Exit the loop after conversion
            elif option_2 == "C":   # from octal
                oct_digits = [str(i) for i in range(8)]   # Valid octal digits (0 to 7)
                for digit in num_1:   # Validate each digit of the input number
                    if digit not in oct_digits:  # If a non-octal digit is found
                      print("ERROR: please insert a valid number")
                      break   # Exit the loop if invalid input
                else:  # If all digits are valid
                    while True:
                        # Display the target base selection menu
                        menu_3()
                        option_3 = input("select a choice (A/B/C/D) :")
                        if option_3 == "A":  # to decimal
                            print("The result = ",octal_to_decimal(int(num_1)))
                            break
                        elif option_3 == "B":  # to binary
                            print("The result = ",octal_to_binary(str(num_1)))
                            break
                        elif option_3 == "C":  # to octal
                            print("The result = ",num_1)
                            break
                        elif option_3 == "D":  # to hexadecimal
                            print( "The result = ",octal_to_hexadecimal(int(num_1)))
                            break
                        else:
                             print("please insert a valid choice ")
                             continue
                    break  # Exit the loop after conversion
            elif option_2 == "D":  # from hexadecimal
                hex_digits = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']  # Valid hexadecimal digits
                for digit in num_1:  # Validate each digit of the input number
                    if digit not in hex_digits:  # If a non-hexadecimal digit is found
                        print("ERROR: please insert a valid number")
                        break  # Exit the loop if invalid input
                else:  # If all digits are valid
                    while True:
                        # Display the target base selection menu
                        menu_3()
                        option_3 = input("select a choice (A/B/C/D) :")
                        if option_3 == "A":  # to decimal
                            print("The result = ",hex_to_decimal(str(num_1)))
                            break
                        elif option_3 == "B":  # to binary
                            print("The result = ",hex_to_binary(str(num_1)))
                            break
                        elif option_3 == "C":  # to octal
                            print("The result = ",hexadecimal_to_octal(str(num_1)))
                            break
                        elif option_3 == "D":  # to hexadecimal
                            print("The result = ",num_1)
                            break
                        else:
                             print("please insert a valid choice ")
                             continue
                    break  # Exit the loop after conversion
            else:
                print("ERROR: Please select a valid choice.")
                continue

        continue

    elif option == "B":
        print("Exit")
        break

    else:
        print(" please select a valid choice")
