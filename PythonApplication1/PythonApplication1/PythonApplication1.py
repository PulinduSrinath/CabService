import datetime

def main():
    time = datetime.datetime.now()
    print("""
           _______
          //  ||\ \\
 ________//___||_\ \\______
 )  _                 _    |
 |_/ \_______________/ \___|
 __\_/_______________\_/____
    """)
    
    print("\n\tWELCOME TO Pulindu VEHICLE RENTAL SHOP!\n")
    print(f"\tCurrent date and time: {time}\n")
    
    while True:
        print("""
        ******** Pulindu Vehicle Rental Shop ********
              1. Admin
              2. Unregistered Customer
              3. Registered Customer
              4. Exit the program
              """)
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        if choice == 1:
            Admin()
        elif choice == 2:
            Unregistered_Customer()
        elif choice == 3:
            Registered_Customer()
        elif choice == 4:
            break
        else:
            print("Please enter a choice between 1-4 only!")

def Admin(password="abc123"):
    username = input("Enter username: ")
    pValue = input("Enter Password: ")
    if pValue == password:
        Admin_function()
    else:
        print("\nPassword is incorrect!")

def Admin_function():
    while True:
        print("""
        ******** Access System ********
              1. Add Vehicle with details, to be rented out
              2. Display All records of
                 a. Vehicles available for Rent
                 b. Customer Payment for a specific time duration
              3. Search Specific record of
                 a. Specific Vehicle Booking
                 b. Specific Customer Payment
              4. Return a Rented Vehicle
              5. Exit to main menu
              """)
        
        try:
            choice = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        if choice == 1:
            add_Vehicles()
        elif choice == 2:
            option = input("Option a or b? ")
            if option.lower() == 'a':
                display_Vehicles()
            else:
                print("Customers Payment for a specific time duration")
        elif choice == 3:
            option = input("Option a or b?")
            if option.lower() == 'a':
                print("Specific Search of Vehicle Booking")
            else:
                print("Specific Search of Customer Payment")
        elif choice == 4:
            print("Return Vehicles")
        elif choice == 5:
            break
        else:
            print("Please enter a number between 1-5 only!")

def get_new_users():
    with open("User_Data.txt", "a") as text:
        name = input("Enter name to register: ")
        password = input("Enter password: ")
        record = name + ":" + password
        text.write(record + "\n")
        print("User registered successfully!")

def existing_users():
    username = input("Username: ")
    password = input("Password: ")
    with open("User_Data.txt", "r") as text:
        lines = text.readlines()
        for line in lines:
            user, passw = line.strip().split(":")
            if username == user and password == passw:
                return True
    print("Invalid username or password!")
    return False

def display_Vehicles():
    with open("DisplayVehicles_Data.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitted = line.strip().split(":")
            print(f"{index}. Type: {splitted[0]}, Brand: {splitted[1]}, Color: {splitted[2]}, Year: {splitted[3]}")
            index += 1

def add_Vehicles():
    with open("DisplayVehicles_Data.txt", "a") as text:
        vehicle_type = input("Type: ")
        brand = input("Brand: ")
        color = input("Color: ")
        year = input("Year: ")
        text.write(f"{vehicle_type}:{brand}:{color}:{year}\n")
        print("Vehicle added successfully!")

def Unregistered_Customer():
    while True:
        print("""
        ******** Unregistered Customers ********
              1. View all Vehicles available for rent
              2. Register to SCRS
              3. Exit to main menu
              """)
        try:
            choice = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            display_Vehicles()
        elif choice == 2:
            get_new_users()
        elif choice == 3:
            break
        else:
            print("Please enter a choice between 1-3 only!")

def Registered_Customer():
    if existing_users():
        while True:
            print("""
            ******** Registered Customer ********
                  1. Personal Rental History
                  2. Available Vehicles
                  3. Booking Vehicles
                  4. Payment and Confirmation of Booking
                  5. Exit to main menu
                  """)
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a valid number!")
                continue
            
            if choice == 1:
                print("Personal Rental History")
            elif choice == 2:
                display_Vehicles()
            elif choice == 3:
                book_Vehicles()
            elif choice == 4:
                print("Payment and Confirmation")
            elif choice == 5:
                break
            else:
                print("Please enter a choice between 1-5 only!")

def book_Vehicles():
    with open("DisplayVehicles_Data.txt", "r") as text:
        lines = text.readlines()
        print("Available Vehicles:")
        for i, line in enumerate(lines, start=1):
            print(f"{i}. {line.strip()}")
        
        try:
            choice = int(input("Select Vehicle number for booking: "))
            if 1 <= choice <= len(lines):
                print(f"You have booked: {lines[choice-1].strip()}")
            else:
                print("Invalid selection!")
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()

