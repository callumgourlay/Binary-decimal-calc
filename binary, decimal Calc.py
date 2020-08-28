"""
calculator Project
"""
import random

int1 = 0
int2 = 0
sumtype = ""
module = ""
binInt = "0"
decInt = "0"
binordec = ""
choice2 = ""
decOut = 0
bin1 = 0
bin2 = 0
bin3 = 0
bin4 = 0
bin5 = 0
bin6 = 0
bin7 = 0
bin8 = 0
bin11 = 0
bin12 = 0
bin13 = 0
bin14 = 0
bin15 = 0
bin16 = 0
bin17 = 0
bin18 = 0
diceSize = 0
rollAmount = 0

while True:
    print('select a module,')
    print('c = calculator')
    print('d = dice roll ')
    print('b = decimal to binary calculator')
    print('esc = close program')
    module = str(input())
    if module == "c":

        print("enter a value for unit 1")
        int1 = int(input())
        print("Select Sum type from  (+, - , / , *)")
        sumtype = str(input())
        while sumtype != "+" and sumtype != "-" and sumtype != "*" and sumtype != "/":
            print("invalid sum type")
            print("Select Sum type from  (+, - , / , *")
            sumtype = str(input())

        print("enter a value for unit 2")
        int2 = int(input())
        if sumtype == "+":
            print("the answer for your sum is ", int1 + int2)
        if sumtype == "-":
            print("the answer for your sum is ", int1 - int2)
        if sumtype == "/":
            print("the answer for your sum is ", int1 / int2)
        if sumtype == "*":
            print("the answer for your sum is ", int1 * int2)

        print("                         ")
        print("                         ")
        print("                         ")
        print("                         ")
        print("                         ")

    if module == "d":
        print("Enter the size of dice you want to roll")
        diceSize = int(input())
        print("How many times do you want to roll")
        rollAmount = int(input())
        while rollAmount >= 1:
            print(random.randint(1, diceSize))
            rollAmount = rollAmount -1


        print("                         ")
        print("                         ")

    if module == "b":

        print("do you want to do normal binary or 2's compliment")
        print("2 = 2's comp")
        print("b = normal")
        choice2 = str(input())

        if choice2 == "b":
            print("do you want to calculate binary or decimal, (b = binary, d = decimal)")

            binordec = str(input())

            if binordec == "b":
                print("enter a decimal number")
                decInt = int(input())

                if decInt >= 128:
                    bin1 = 1
                    decInt = decInt - 128

                if decInt >= 64:
                    bin2 = 1
                    decInt = decInt - 64

                if decInt >= 32:
                    bin3 = 1
                    decInt = decInt - 32

                if decInt >= 16:
                    bin4 = 1
                    decInt = decInt - 16

                if decInt >= 8:
                    bin5 = 1
                    decInt = decInt - 8

                if decInt >= 4:
                    bin6 = 1
                    decInt = decInt - 4

                if decInt >= 2:
                    bin7 = 1
                    decInt = decInt - 2

                if decInt >= 1:
                    bin8 = 1
                    decInt = decInt - 1

                print("Binary Number = ")

                print(bin1, bin2, bin3, bin4, bin5, bin6, bin7, bin8)

                print("                         ")
                print("                         ")
                print("                         ")
                print("                         ")
                print("                         ")

            if binordec == "d":
                print("enter a binary number up to 8 characters")
                binInt = str(input())

                bin11 = binInt[0]
                bin12 = binInt[1]
                bin13 = binInt[2]
                bin14 = binInt[3]
                bin15 = binInt[4]
                bin16 = binInt[5]
                bin17 = binInt[6]
                bin18 = binInt[7]

                if bin11 == "1":
                    decOut = decOut + 128
                if bin12 == "1":
                    decOut = decOut + 64
                if bin13 == "1":
                    decOut = decOut + 32
                if bin14 == "1":
                    decOut = decOut + 16
                if bin15 == "1":
                    decOut = decOut + 8
                if bin16 == "1":
                    decOut = decOut + 4
                if bin17 == "1":
                    decOut = decOut + 2
                if bin18 == "1":
                    decOut = decOut + 1

                print("your decimal number is ")
                print(decOut)

                print("                         ")
                print("                         ")
                print("                         ")
                print("                         ")
                print("                         ")
        if choice2 == "2":
            print("do you want to calculate 2 compliment or decimal, (2 = 2 comp, d = decimal)")

            binordec = str(input())

            if binordec == "2":
                print("enter a negative number (e.g -26 (must be > than -128))")
                decInt = int(input())
                decInt = 128 + decInt

                bin1 = 1

                if decInt >= 64:
                    bin2 = 1
                    decInt = decInt - 64

                if decInt >= 32:
                    bin3 = 1
                    decInt = decInt - 32

                if decInt >= 16:
                    bin4 = 1
                    decInt = decInt - 16

                if decInt >= 8:
                    bin5 = 1
                    decInt = decInt - 8

                if decInt >= 4:
                    bin6 = 1
                    decInt = decInt - 4

                if decInt >= 2:
                    bin7 = 1
                    decInt = decInt - 2

                if decInt >= 1:
                    bin8 = 1
                    decInt = decInt - 1

                print("2 Compliment Binary Number = ")

                print(bin1, bin2, bin3, bin4, bin5, bin6, bin7, bin8)
                print("                         ")
                print("                         ")
                print("                         ")
                print("                         ")
                print("                         ")

            if binordec == "d":
                print("enter a binary number up to 8 characters")
                binInt = str(input())

                bin11 = binInt[0]
                bin12 = binInt[1]
                bin13 = binInt[2]
                bin14 = binInt[3]
                bin15 = binInt[4]
                bin16 = binInt[5]
                bin17 = binInt[6]
                bin18 = binInt[7]

                if bin11 == "1":
                    decOut = 0
                if bin12 == "1":
                    decOut = decOut - 64
                if bin13 == "1":
                    decOut = decOut - 32
                if bin14 == "1":
                    decOut = decOut - 16
                if bin15 == "1":
                    decOut = decOut - 8
                if bin16 == "1":
                    decOut = decOut - 4
                if bin17 == "1":
                    decOut = decOut - 2
                if bin18 == "1":
                    decOut = decOut - 1

                print("your decimal number is ")
                print(decOut)

                print("                         ")
                print("                         ")
                print("                         ")
                print("                         ")
                print("                         ")

    if module == "esc":
        exit()

    if module != "c" and module != "d" and module != "esc" and module != "b":
        print("ERROR, unexpected module selected")

"Fergus" " <-------------do not delete"

