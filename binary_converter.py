#!/usr/local/bin/python3

import colored
import math

print(colored.stylize("\n---- | Convert decimal to binary | ----\n", colored.fg("red")))

decimal_num = int(input("Enter a decimal number: "))

def binary(number):
    exponent = math.floor(math.log2(number))
    binary_num = ""
    decimal = number

    for _ in range(exponent+1):
        if decimal//(2**exponent) >= 1:
            binary_num += "1"
            decimal -= (2**exponent)
            exponent -= 1
        else:
            binary_num += "0"
            exponent -= 1

    return f"The binary number is: {binary_num}\n"


if decimal_num == 0:
    print(f"The binary number is: 0\n")
elif decimal_num == 1:
    print(f"The binary number is: 1\n")
else:
    print(binary(decimal_num))
