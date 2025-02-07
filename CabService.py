import datetime
import os

def main():
    time = datetime.datetime.now()
    print("""
          _______ 
         //  ||\ \ 
________//___||_\ \_______
)  _                 _    | 
|_/ \_______________/ \___| 
___\_/_______________\_/____ 
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
            admin()
        elif choice == 2:
            unregistered_customer()
        elif choice == 3:
            registered_customer()
        elif choice == 4:
            break
        else:
            print("Please enter a choice between 1-4 only!")

def admin():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "abc123":
        admin_function()
    else:
        print("\nIncorrect username or password!\n")

def admin_function():
    while True:
        print("""
        ******** Admin Access ******** 
              1. Add Vehicle
              2. Display All Vehicles
              3. Exit to main menu
              """)
        try:
            choice = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        if choice == 1:
            add_vehicle()
        elif choice == 2:
            display_vehicles()
        elif choice == 3:
            break
        else:
            print("Please enter a number between 1-3 only!")

def add_vehicle():
    with open("vehicles.txt", "a") as file:
        vehicle_type = input("Type: ")
        brand = input("Brand: ")
        color = input("Color: ")
        year = input("Year: ")
        file.write(f"{vehicle_type}:{brand}:{color}:{year}\n")
        print("Vehicle added successfully!\n")

def display_vehicles():
    if not os.path.exists("vehicles.txt"):
        with open("vehicles.txt", "w") as file:
            file.write("Car:Toyota:Red:2022\n")
            file.write("Bike:Yamaha:Blue:2021\n")
            file.write("Van:Nissan:White:2020\n")
    
    with open("vehicles.txt", "r") as file:
        vehicles = file.readlines()
    
    if not vehicles:
        print("No vehicles available.\n")
        return
    
    print("Available Vehicles:")
    for index, vehicle in enumerate(vehicles, 1):
        vehicle_type, brand, color, year = vehicle.strip().split(":")
        print(f"{index}. Type: {vehicle_type}, Brand: {brand}, Color: {color}, Year: {year}")

def unregistered_customer():
    while True:
        print("""
        ******** Unregistered Customer ******** 
              1. View all Vehicles
              2. Register
              3. Exit to main menu
              """)
        try:
            choice = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        if choice == 1:
            display_vehicles()
        elif choice == 2:
            register_user()
        elif choice == 3:
            break
        else:
            print("Please enter a number between 1-3 only!")

def register_user():
    with open("users.txt", "a") as file:
        username = input("Enter username: ")
        password = input("Enter password: ")
        file.write(f"{username}:{password}\n")
        print("Registration successful!\n")

def registered_customer():
    if login_user():
        while True:
            print("""
            ******** Registered Customer ******** 
                  1. View Vehicles
                  2. Book a Vehicle
                  3. Exit to main menu
                  """)
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a valid number!")
                continue
            
            if choice == 1:
                display_vehicles()
            elif choice == 2:
                book_vehicle()
            elif choice == 3:
                break
            else:
                print("Please enter a number between 1-3 only!")

def login_user():
    if not os.path.exists("users.txt"):
        print("No users registered. Please register first.\n")
        return False
    
    username = input("Username: ")
    password = input("Password: ")
    
    with open("users.txt", "r") as file:
        users = file.readlines()
    
    for user in users:
        stored_user, stored_pass = user.strip().split(":")
        if username == stored_user and password == stored_pass:
            print("Login successful!\n")
            return True
    
    print("Invalid username or password!\n")
    return False

def book_vehicle():
    display_vehicles()
    
    if not os.path.exists("vehicles.txt"):
        return
    
    with open("vehicles.txt", "r") as file:
        vehicles = file.readlines()
    
    if not vehicles:
        return
    
    try:
        choice = int(input("Select a vehicle number to book: "))
        if 1 <= choice <= len(vehicles):
            print(f"Vehicle {choice} has been booked successfully!\n")
        else:
            print("Invalid selection!\n")
    except ValueError:
        print("Please enter a valid number!\n")

if __name__ == "__main__":
    main()
