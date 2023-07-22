class Library:
    def __init__(self, listofbooks):
        self.books = listofbooks

    def displaybooks(self):
        # print("\n" .join(self.books))
        print("List of Books available in Library are: ")
        for books in self.books:
            print("\t *", books)

    def borrowBook(self, bookname):
        global booksissuedtostudent
        booksissuedtostudent = []
        if bookname in self.books:
            print(f"Books {bookname} has been issued to you")
            self.books.remove(str(bookname))
            booksissuedtostudent.append(bookname)
            print(booksissuedtostudent)
            return True
        else:
            print("Books is not available in Library")
            return False

    def returnBook(self, bookname):
        self.books.append(bookname)
        print(f"Thanks for returing the book {bookname}")
        booksissuedtostudent.remove(str(bookname))
        print(booksissuedtostudent)


class Student:
    def __init__(self, listofstudents):
        self.students = listofstudents

    def displayStudents(self):
        for studentname in self.students:
            print(" \t", studentname)

    def requestBook():
        book = input("Enter the name of book you want to request")
        return book

    def returnBook():
        book = input("Enter the name of book you want to return")
        return book


lib = Library(['Science', 'Math', 'English', 'history',
              'geograpphy', 'economics', 'biology'])
# lib.displaybooks()
Students = ['sachin', 'ajit', 'rahul', 'karam']
st = Student(Students)

studentsname = input("Welcome to Library.\nPlease enter you name: ")
while (True):
    if studentsname == 'sachin':
        print("Welcome ", studentsname)
        WelcomeMessage = ''' ******* Welcome to Library *******
                                    Choose from below options
                                    1. Check list of Students
                                    2. Check Available Books
                                    3. Request a Book
                                    4. Return a Book
                                    5. Exit'''
        print(WelcomeMessage)
        try:
            a = int(input("Enter your choice: "))
            if a == 1:
                Student.displayStudents()
            elif a == 2:
                lib.displaybooks()
            elif a == 3:
                lib.borrowBook(Student.requestBook())
            elif a == 4:
                lib.returnBook(Student.returnBook())
            elif a == 5:
                print("Thanks for using Library")
                exit()
            else:
                print("Invalid Option!")
        except ValueError:
            print("Enter from given options")
    elif studentsname == 'ajit':
        print("Welcome ", studentsname)
        WelcomeMessage = '''Choose from below options
                                    1. Check list of Students
                                    2. Check Available Books
                                    3. Request a Book
                                    4. Return a Book
                                    5. Exit'''
        print(WelcomeMessage)
        try:
            a = int(input("Enter your choice: "))
            if a == 1:
                Student.displayStudents()
            elif a == 2:
                lib.displaybooks()
            elif a == 3:
                lib.borrowBook(Student.requestBook())
            elif a == 4:
                lib.returnBook(Student.returnBook())
            elif a == 5:
                print("Thanks for using Library")
                exit()
            else:
                print("Invalid Option!")
        except ValueError:
            print("Enter from given options")
