'''

Intro to Comp Sci and Eg.

HW06

hw06.py

Xiaoyan Zhang

xz1133

Calculator

'''

def calculate():
    string = str( raw_input("Enter math: "))
    negative_sign = string[0]

    if (negative_sign == '-'):
        aString = string.lstrip("-")
        operand = aString.strip("1234567890")

        if ( operand == "+" ):
            number = string.split("+")
            result = int(number[0]) + int(number[1])
            return result

        elif ( operand == "-" ):
            number = string.split("-")
            result = (-int(number[1])) - int(number[2])
            return result

        elif ( operand == "--" ):
            number = string.split("--")
            result = int(number[0]) + int(number[1])
            return result

        elif ( operand == "*" ):
            number = string.split("*")
            result = int(number[0]) * int(number[1])
            return result

        elif ( operand == "**" ):
            number = string.split("**")
            result = int(number[0]) ** int(number[1])
            return result

        elif ( operand == "/" ):
            number = string.split("/")
            result = float(number[0]) / float(number[1])
            return result

        else:
            return "Operand not supported or not invalid. \nUpgrade to premium: giving full credits!\n"
    
        return result

    elif int(negative_sign):
        operand = string.strip("1234567890")
        if ( operand == "+" ):
            number = string.split("+")
            result = int(number[0]) + int(number[1])
            return result

        elif ( operand == "-" ):
            number = string.split("-")
            if ( number[1] != ''):
                result = int(number[0]) - int(number[1])
                return result
            else:
                result = int(number[0]) + int(number[2])
                return result

        elif ( operand == "*" ):
            number = string.split("*")
            result = int(number[0]) * int(number[1])
            return result

        elif ( operand == "**" ):
            number = string.split("**")
            result = int(number[0]) ** int(number[1])
            return result

        elif ( operand == "/" ):
            number = string.split("/")
            result = float(number[0]) / float(number[1])
            return result

        else:
            return "Operand not supported for free version. \nUpgrade to premium for only $0.99 today!\n"
    

def main():
    while(True):
        result = calculate()
        print result

main()
