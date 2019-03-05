# Global Constant
MILES = 0.6214

# Get Kilometers
def getKilometers():
    kilometers = input("Enter the kilometer distance.")
    while kilometers.isdigit == False and kilometers <= 0:
        print("Error: Enter a valid number")
        kilometers = input("Enter the kilometer distance.")
        kilometers = int(kilometers)
        calcMiles(kilometers)
    return kilometers

# Calc Miles
def calcMiles(miles):
    
    miles = kilometers / MILES
    round (miles, 2)
    displayResult(miles)
    return miles

# Display the Result
def displayResult(miles):
    print("The distance in miles is", miles)

# Menu
def menu():
    print ("\n1- Continue")
    print ("2- Quit")

    a = input("\n Press 1 or 2")
    while a.isdigit() == False and (a < 1 or a > 2):
        print("Error: Enter 1 or 2")
        a = input("Press 1 or 2")

    if a == 1:
        main()
    elif a == 2:
        quit()

# Main
def main():
    kilometers = 1
    getKilometers()
    miles = 1
    calcMiles(miles)
    displayResult()

# Calling Main
main()


