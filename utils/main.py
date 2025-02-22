# main.py

import sys
from models.room import RoomModel
# from models.guest import GuestModel  # for example
# from models.booking import BookingModel

def main_menu():
    while True:
        print("\n--- Hotel Management System ---")
        print("1. Add New Room")
        print("2. View Room")
        print("3. Update Room")
        print("4. Delete Room")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_room_flow()
        elif choice == '2':
            view_room_flow()
        elif choice == '3':
            update_room_flow()
        elif choice == '4':
            delete_room_flow()
        elif choice == '5':
            print("Exiting the system...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

def add_room_flow():
    print("\n--- Add New Room ---")
    room_number = input("Room Number: ")
    room_type = input("Room Type (Single/Double/Deluxe): ")
    price_per_night = float(input("Price per night: "))
    RoomModel.create_room(room_number, room_type, price_per_night)

def view_room_flow():
    print("\n--- View Room ---")
    room_id = input("Enter Room ID: ")
    room = RoomModel.get_room(int(room_id))
    if room:
        print("Room details:")
        print("Room ID:", room[0])
        print("Room Number:", room[1])
        print("Room Type:", room[2])
        print("Price per Night:", room[3])
        print("Status:", room[4])
    else:
        print("No room found with that ID.")

def update_room_flow():
    print("\n--- Update Room ---")
    room_id = input("Enter Room ID to update: ")
    new_room_number = input("New Room Number (leave blank to skip): ")
    new_room_type = input("New Room Type (leave blank to skip): ")
    new_price = input("New Price (leave blank to skip): ")
    new_status = input("New Status (leave blank to skip): ")

    RoomModel.update_room(
        room_id=int(room_id),
        room_number=new_room_number if new_room_number else None,
        room_type=new_room_type if new_room_type else None,
        price_per_night=float(new_price) if new_price else None,
        status=new_status if new_status else None
    )

def delete_room_flow():
    print("\n--- Delete Room ---")
    room_id = input("Enter Room ID to delete: ")
    RoomModel.delete_room(int(room_id))

if __name__ == "__main__":
    main_menu()
