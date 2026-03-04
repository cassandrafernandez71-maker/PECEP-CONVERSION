# ASK FIRST IF THEY WANT TO START
Start_Choice = input("Would you like to start to convert your Hexadecimal to decimal? [Y/N]: ").upper()

if Start_Choice == 'Y':
    User_Action = 'Y'
else:
    User_Action = 'N'
    print("Program discontinued.")

# CONVERTION LOOP
while User_Action == 'Y':
    Decimal_Input = input("\nEnter a decimal number (e.g., 255.625): ")
    
    try:
        if "." in Decimal_Input:
            Whole_Part, Frac_Part = Decimal_Input.split(".")
            Whole_Num = int(Whole_Part)
            Fraction = float("0." + Frac_Part)
        else:
            Whole_Num = int(Decimal_Input)
            Fraction = 0.0

        # CONVERTION OF WHOLE NUMBER TO HEXADECIMAL
        Hex_Whole = hex(Whole_Num).replace("0x", "").upper()

        # CONVERTION OF FRACTION PART TO HEXADECIMAL
        Hex_Frac = ""
        Hex_Digits = "0123456789ABCDEF"
        while Fraction > 0 and len(Hex_Frac) < 10:
            Fraction *= 16
            Index = int(Fraction)
            Hex_Frac += Hex_Digits[Index]
            Fraction -= Index

        Result = Hex_Whole + ("." + Hex_Frac if Hex_Frac else "")
        print(f"Hexadecimal representation: {Result}")
    except ValueError:
        print("Invalid input! Please enter a valid decimal number.")

    # ASK TO REPEAT AGAIN
    Enter_Again = 'Y'
    while Enter_Again == 'Y':
        Input_User_Action = input("Do you want to enter again? [Y/N]: ").upper()
        if Input_User_Action == 'Y':
            User_Action = 'Y'
            Enter_Again = 'N'
        elif Input_User_Action == 'N':
            User_Action = 'N'
            Enter_Again = 'N'
            print("okay, Thank you!")
        else:
            print("Please choose Y or N only.")
            Enter_Again = 'Y'