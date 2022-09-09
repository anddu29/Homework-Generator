__author__ = "Andrei Stefan"
__version__ = "1.0.0"
__email__ = "andistef29@gmail.com"
__status__ = "Production"

import methods

if __name__ == "__main__":
    while True:
        try:
            bookNumberChapters = int(input("Enter the number of chapters for your book: "))
        except ValueError:
            print("Incorrect value type for number of chapters! (Expected integer)")
            continue
        break
    book = methods.book(bookNumberChapters)

    for i in range(bookNumberChapters):
        while True:
            try:
                bookNumberProblems = int(input(f"Enter the number of chapters for chapter number {i + 1}: "))
                book.register_problems(i + 1, bookNumberProblems)
            except ValueError:
                print("Incorrect value type for number of problems per chapter! (Expected integer)")
                continue
            break

    while True:
        try:
            homeworkStudentName = input("Enter the name of the student you want to assign the homework to: ")
        except ValueError:
            print("Incorrect value type for name! (Expected string)")
            continue
        break

    while True:
        try:
            homeworkNumberProblems = int(input("Enter the number of problems for homework: "))
        except ValueError:
            print("Incorrect value type for name! (Expected string)")
            continue
        break

    book.random_generator(homeworkStudentName, homeworkNumberProblems)

    print("\nGeneral information about the book: ")
    for i in range(1, bookNumberChapters):
        book.display_chapter_problems(i)
