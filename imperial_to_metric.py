# calculating functions
def imperial_to_metric():
    feet = int(input("Number of feet? "))
    inches = int(input("Number of inches? "))
    result = (feet*12 + inches)*2.54 # calculate from inches to cm

    print(f"{feet}ft{inches} equals {result}cm")
    
# welcome message
print("Welcome to this convertion program!")

# program loop
while True:
    print("\n" + "Please select an option.")
    print("    1. Convert imperial height (ft/in) to metric height (cm)")
    print("    2. Exit program" + "\n")
    option = input("Select option n°: ")
    
    if option == str(1):
        imperial_to_metric()
        
        again = input("Use again? ")
        
        if again.lower() == "y" or "yes":
            continue
        else:
            break
    elif option == str(2):
        print("Program exited.")
        break
    elif option != str(1):
        print("ERROR: Not an option")