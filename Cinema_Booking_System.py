# This System create by AHMAD
class Star_Cinema:
    __hall_list = []


    @classmethod
    def entry_hall(self, hall):
        self.__hall_list.append(hall)


    @classmethod
    def get_hall_list(self):
        return self.__hall_list


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        super().entry_hall(self) 


    def entry_show(self, show_id, movie_name, time):
        show_tuple = (show_id, movie_name, time)
        self.__show_list.append(show_tuple)
        self.__seats[show_id] = [['free' for _ in range(self.__cols)] for _ in range(self.__rows)]


    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            raise ValueError(f"Show ID {show_id} does not exist.")
        
        
        for row, col in seat_list:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                raise ValueError(f"Invalid seat position: ({row}, {col}).")
            if self.__seats[show_id][row][col] == 'booked':
                raise ValueError(f"Seat ({row}, {col}) is already booked.")
            self.__seats[show_id][row][col] = 'booked'


    def view_show_list(self):
        return [(show[0], show[1], show[2]) for show in self.__show_list]
    

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            raise ValueError(f"Show ID {show_id} does not exist.")
        
        print(f"Available seats for show ID {show_id}:\n")
        for row in self.__seats[show_id]:
            print(row)


    def get_hall_no(self):
        return self.__hall_no


def main_dashboard():
    hall1 = Hall(5, 5, 1)

    hall1.entry_show('101', '12th fail', '06/10/2024 12:00 PM')

    hall1.entry_show('102', 'jawan', '08/10/2024 03:00 PM')


    while True:
        print("\n1. View all shows today")
        print("2. View available seats")
        print("3. Book ticket")
        print("4. Exit")
        option = input("Enter option: ")

        if option == '1':
            print("\nShows today:")
            for hall in Star_Cinema.get_hall_list():
                show_list = hall.view_show_list()
                for show in show_list:
                    print(f"Hall {hall.get_hall_no()}, Show ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}")
        elif option == '2':
            try:
                hall_no = int(input("Enter hall number: "))
                show_id = input("Enter show ID: ")
                for hall in Star_Cinema.get_hall_list():
                    if hall.get_hall_no() == hall_no:
                        available_seats = hall.view_available_seats(show_id)
                        available_seats
                        break
                else:
                    print(f"Hall {hall_no} does not exist.")
            except ValueError as e:
                print(e)

        elif option == '3':
            try:
                hall_no = int(input("Enter hall number: "))
                show_id = input("Enter show ID: ")
                seat_count = int(input("Enter number of seats to book: "))
                seats_to_book = []
                for _ in range(seat_count):
                    row = int(input("Enter row number: "))
                    col = int(input("Enter column number: "))
                    seats_to_book.append((row, col))

                for hall in Star_Cinema.get_hall_list():
                    if hall.get_hall_no() == hall_no:
                        hall.book_seats(show_id, seats_to_book)
                        print(f"Seats {seats_to_book} successfully booked for show {show_id}.")
                        break
                else:
                    print(f"Hall {hall_no} does not exist.")
            except ValueError as e:
                print(e)

        elif option == '4':
            print("Exiting system.")
            break

        else:
            print("Invalid option. Please try again.")


main_dashboard()
# This System create by AHMAD
