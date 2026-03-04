# ASK FIRST IF THEY WANT TO START
Start_Choice = input("Would you like to start to convert your octal to decimal? [Y/N]: ").upper()

if Start_Choice == 'Y':
    User_Action = 'Y'
else:
    User_Action = 'N'
    print("Program discontinued.")

# CONVERTION LOOP
while User_Action == 'Y':
    Octal_Input = input("\nEnter an octal number (Ex., 2026.25): ")
    
    try:
        if "." in Octal_Input:
            Whole_Part, Frac_Part = Octal_Input.split(".")
            # CONVERTION IF THE WHOLE NUMBER PART
            Decimal_Whole = int(Whole_Part, 8)
            # CENVERTION OF FRACTION PART
            Decimal_Frac = 0.0
            for i, digit in enumerate(Frac_Part):
                Decimal_Frac += int(digit) * (8 ** -(i + 1))
            Result = Decimal_Whole + Decimal_Frac
        else:
            Result = int(Octal_Input, 8)

        print(f"Decimal representation: {Result}")
    except ValueError:
        print("Invalid input! Please enter valid octal digits (0-7).")

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