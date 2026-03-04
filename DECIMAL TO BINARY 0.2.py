Start_Choice = input("Would you like to start to convert your decimal to binary? [Y/N]: ").upper()

if Start_Choice == 'Y':
    User_Action = 'Y'
else:
    User_Action = 'N'
    print("Program discountinued")
    
while User_Action == 'Y':
    Decimal_Input = input("\nEnter a decimal number (Ex., 1114.06 ): ")
    
    if "." in Decimal_Input:
        Whole_Part, Fractional_Part = map(str, Decimal_Input.split("."))
        Whole_Num = int(Whole_Part)
        Fraction = float("0." + Fractional_Part)
    else:
        Whole_Num = int(Decimal_Input)
        Fraction = 0.0

    # WHOLE NUMBER CONVERTION
    Binary_Whole = bin(Whole_Num).replace("0b", "")

    # FRACTION PART CONVERTION
    Binary_Fraction = ""
    while Fraction > 0 and len(Binary_Fraction) < 8:      #   LIMITS TO ONLY 8 DECIMALS ONLY
        Fraction *= 2
        Bit = int(Fraction)
        Binary_Fraction += str(Bit)
        Fraction -= Bit

    Result = Binary_Whole + ("." + Binary_Fraction if Binary_Fraction else "")
    print(f"Binary representation: {Result}")

    Enter_Again = 'Y'
    while Enter_Again == 'Y':
        Input_User_Action = input("Do you want to enter again? [Y/N]: ").upper()
        if Input_User_Action == 'Y':
            Enter_Again = 'N'
        elif Input_User_Action == 'N':
            User_Action = 'N'
            Enter_Again = 'N'
            print("Okay, Thank you!")
        else:
            print("Please choose Y or N only.")