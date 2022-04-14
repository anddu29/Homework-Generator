import methods


if __name__ == "__main__":
    # chapters = int(input("Introduce number of chapters:\n"))
    # print(f"There are {chapters} chapters.")


    # for x in range(1, chapters+1):
    #     romanchapter = methods.printRoman(x)
    #     problems = input(f"Introduce number of problems for chapter {romanchapter}:\n")
    #     print(f"There are {problems} problems for Chapter {romanchapter}.")

    MathBook = methods.book(5)
    MathBook.display()
    

