class Room:
    def __init__(self, room_type, bed_type, name, nid, phone, stay_duration):
        self.room_type = room_type
        self.bed_type = bed_type
        self.name = name
        self.nid = nid
        self.phone = phone
        self.stay_duration = stay_duration

    def book_room(self):
        print(f"You selected {self.room_type} Quality and {self.bed_type} Room")
        print("Before booking your room, you should provide us with some information")
        self.name = input("Enter your Name: ")
        self.nid = int(input("Enter Your NID: "))
        self.phone = int(input("Enter your number: "))
        self.stay_duration = int(input("How long will you stay: "))
        print("--------------------------------------")
        print("--Your booking is successfully done.--")
        print("--------------------------------------")

class Hotel:
    def __init__(self):
        self.rooms = {
            "Premium": {
                "Single Bed": Room("Premium", "Single Bed", "", 0, 0, 0),
                "Double Bed": Room("Premium", "Double Bed", "", 0, 0, 0)
            },
            "Normal": {
                "Single Bed": Room("Normal", "Single Bed", "", 0, 0, 0),
                "Double Bed": Room("Normal", "Double Bed", "", 0, 0, 0)
            }
        }

    def display_menu(self):
        while True:
            print("----Menu----")
            print("1. Room Booking")
            print("2. Facilities")
            print("3. Contact")
            print("4. Exit")

            select = int(input("Enter your menu: "))

            if select == 1:
                self.book_room()

            elif select == 2:
                self.display_facilities()

            elif select == 3:
                self.display_contact_info()

            elif select == 4:
                break

            else:
                print("Invalid menu option. Please enter a valid option (1, 2, 3, or 4).")

    def book_room(self):
        print("What type of room are you looking for:")
        print("1. Premium")
        print("2. Normal")
        print("3. Back to main menu")
        select1 = int(input("Select your Room: "))

        if select1 == 1 or select1 == 2:
            room_type = "Premium" if select1 == 1 else "Normal"
            bed_type = self.select_bed_type(room_type)
            self.rooms[room_type][bed_type].book_room()
        elif select1 == 3:
            pass
        else:
            print("Invalid selection. Please enter a valid option.")

    def select_bed_type(self, room_type):
        print("1. Single Bed")
        print("2. Double Bed")
        select2 = int(input("Select your type: "))
        bed_type = "Single Bed" if select2 == 1 else "Double Bed"
        return bed_type

    def display_facilities(self):
        print("-----------Facilities menu------------")
        print("> Premium Room (Single - 120$ and Double - 200$)")
        print("> Normal Room (Single - 50$ and Double - 70$)")

    def display_contact_info(self):
        print("---------Contact Information---------")
        print("> Number: 01866259573")
        print("> mail : omi'sHotel31@gmail.com")
        print("> Address : kanishail south surma, sylhet")


if __name__ == "__main__":
    hotel = Hotel()
    hotel.display_menu()
