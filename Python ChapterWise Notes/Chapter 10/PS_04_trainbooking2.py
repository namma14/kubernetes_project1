# writing a prog for booking cancellation
class booking:
    global final_seats
    final_seats=[]
    def seatbooking(self,book_seatno):
        print ("final seats are",final_seats) 
        print(type(final_seats))
        if len(book.seats)>0:
            if book_seatno in book.seats:
                print(f"Booking in train {book.train_name} is confirmed, SeatNo is {book_seatno}")
                total_available_seats = len(book.seats)-1
                print(f"Total no of seats available are {total_available_seats}")
                a = book.seats.remove(book_seatno)
                global z
                z= book.seats
                print(f"Available seats are {book.seats}")  
                print("**********************************")

                final_seats.append(book_seatno)
                print("Booked Seats are: ",final_seats)
            else:
                print("Enter a valid Seat No")
        else:
            print(f"All seats are booked for train {book.train_name}")
        return final_seats
        
    def cancellation(self,seatno):
        print("seats available for cancellation", final_seats)
        # cancellationseat=int(input("Select seat for cancellation from booked seats",final_seats))
        print("Seats available for Booking",z)
        if seatno in final_seats:
            print(f"Cancellation of Ticket.No for train {book.train_name} is confirmed.")
            print(f"Seat No {seatno} is available for booking")
            book.seats.append(seatno)
            currently_available_seats = len(book.seats)
            print(f"Total Seats available in train {book.train_name} are {book.seats}")
        else:
            print("Enter valid Seat No for cancellation")
        

book = booking()
book.seats = [1,2,3,4,5,6,7]
book.train_name = "Rajdhani 14034"
book.seatbooking(1)
book.seatbooking(2)
book.seatbooking(3)
book.seatbooking(4)
book.seatbooking(5)
book.seatbooking(6)
book.seatbooking(7)
book.cancellation(4)

