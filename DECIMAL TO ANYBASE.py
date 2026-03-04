# ASK FIRST IF THEY WANT TO START
Start_Choice = input("Would you like to start to convert your Hexadecimal to decimal? [Y/N]: ").upper()

if Start_Choice == 'Y':
    User_Action = 'Y'
else:
    User_Action = 'N'
    print("Program discontinued.")

# CONVERTION LOOP STARTS HERE
while User_Action == 'Y':
    try:
        Decimal_Input = input("\nEnter a decimal number (e.g., 1000.5): ")
        Base = int(input("Enter the base to convert to (2-500): "))
        
        if Base < 2 or Base > 500:
            print("Please enter a base between 2 and 500.")
            continue

        # SEPERATE WHOLE AND FRACTION
        if "." in Decimal_Input:
            Whole_Part, Frac_Part = Decimal_Input.split(".")
            Whole_Num = int(Whole_Part)
            Fraction = float("0." + Frac_Part)
        else:
            Whole_Num = int(Decimal_Input)
            Fraction = 0.0

        # USE (n) NOTATION FOR BASES ABOVE 36 TO AVOIND RUNNING OUT OF LETTERS
        def get_digit(n):
            Digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            return Digits[n] if n < 36 else f"({n})"

        # CONVERTION OF WHOLE NUMBER PART
        Res_Whole = ""
        Temp_Num = Whole_Num
        if Temp_Num == 0: Res_Whole = "0"
        while Temp_Num > 0:
            Res_Whole = get_digit(Temp_Num % Base) + Res_Whole
            Temp_Num //= Base

        # CONVERTION OF FRACTION PART
        Res_Frac = ""
        while Fraction > 0 and len(Res_Frac) < 10:
            Fraction *= Base
            Index = int(Fraction)
            Res_Frac += get_digit(Index)
            Fraction -= Index

        Result = Res_Whole + ("." + Res_Frac if Res_Frac else "")
        print(f"Base {Base} representation: {Result}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    # THIS WILL ASK YOU IF YOU WANT TO CONTINUE AGAIN
    Enter_Again = 'Y'
    while Enter_Again == 'Y':
        Input_User_Action = input("Do you want to enter again? [Y/N]: ").upper()
        if Input_User_Action == 'Y':
            Enter_Again = 'N'
        elif Input_User_Action == 'N':
            User_Action = 'N'
            Enter_Again = 'N'
            print("Okay, Thank You!")
        else:
            print("Please choose Y or N only.")
            Enter_Again = 'Y'