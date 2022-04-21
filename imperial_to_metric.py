def imperial_to_metric():
    feet = int(input("Number of feet? "))
    inches = int(input("Number of inches? "))
    result = (feet*12 + inches)*2.54

    print(f"{feet}ft{inches} equals {result}cm")
    
print("Welcome to this convertion program!")

while True:
    print("\n" + "Please select a convertion mode.")
    print("    1. Convert imperial height (ft/in) to metric height (cm)" + "\n")
    option = input("Select mode n°: ")
    
    if option == str(1):
        imperial_to_metric()
        break
    elif option != str(1):
        print("ERROR: Not an option")
    

