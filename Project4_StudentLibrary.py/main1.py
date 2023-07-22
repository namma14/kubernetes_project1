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
        booksissuedtostudent.append(bookname)
        if bookname in self.books:
            print(f"Books {bookname} has been issued to you")
            self.books.remove(str(bookname))
        else:
            print("Books is not available in Library")

    def returnBook(self, bookname):
        self.books.append(bookname)
        print(f"Thanks for returing the book {bookname}")
        booksissuedtostudent.remove(str(bookname))

    def listofbooksissuedtoastudent(self):
        print(f"Total books issued to {studentsname}:\n {booksissuedtostudent}")


class Student:
    def __init__(self, listofstudents):
        self.students = listofstudents

    @staticmethod
    def displayStudents(listofstudents):
        for studentname in listofstudents:
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
Students = ['sachin', 'ajit']
st = Student(Students)

studentsname = input("Welcome to Library.\nPlease enter you name: ")
if studentsname == 'sachin':
        print("Welcome ", studentsname)
        while (True):
                WelcomeMessage = ''' ******* Welcome to Library *******
                                            Choose from below options
                                            1. Check list of Students
                                            2. Check Available Books
                                            3. Request a Book
                                            4. Return a Book
                                            5. List of Books issued to {}
                                            6. Exit''' .format(studentsname)
                print(WelcomeMessage)
                try:
                    a = int(input("Enter your choice: "))
                    if a == 1:
                        Student.displayStudents(Students)
                    elif a == 2:
                        lib.displaybooks()
                    elif a == 3:
                        lib.borrowBook(Student.requestBook())
                    elif a == 4:
                        lib.returnBook(Student.returnBook())
                    elif a == 5:
                        lib.listofbooksissuedtoastudent()
                    elif a == 6:
                        print("Thanks for using Library")
                        exit()
                    else:
                        print("Invalid Option!")
                except ValueError:
                    print("Enter from given options")

if studentsname == 'ajit':
        print("Welcome ", studentsname)
        while (True):
                WelcomeMessage = ''' ******* Welcome to Library *******
                                            Choose from below options
                                            1. Check list of Students
                                            2. Check Available Books
                                            3. Request a Book
                                            4. Return a Book
                                            5. List of Books issued to {}
                                            6. Exit''' .format(studentsname)
                print(WelcomeMessage)
                try:
                    a = int(input("Enter your choice: "))
                    if a == 1:
                        Student.displayStudents(Students)
                    elif a == 2:
                        lib.displaybooks()
                    elif a == 3:
                        lib.borrowBook(Student.requestBook())
                    elif a == 4:
                        lib.returnBook(Student.returnBook())
                    elif a == 5:
                        lib.listofbooksissuedtoastudent()
                    elif a == 6:
                        print("Thanks for using Library")
                        exit()
                    else:
                        print("Invalid Option!")
                except ValueError:
                    print("Enter from given options")
            