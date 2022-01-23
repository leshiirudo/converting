feet = float(input("Number of feet: "))
inches = float(input("Number of inches: "))

feet_in_inches = feet*12
total_inches = feet_in_inches + inches

print("Number of total inches: " + str(total_inches))
print("Number of cm: " + str(total_inches*2.54))
