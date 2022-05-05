import methods



if __name__ == "__main__":

    MathBook = methods.book(5)
    MathBook.display_chapters()
    MathBook.register_problems(1,5)

    MathBook.display_chapter_problems(1)
    MathBook.display_chapter_problems(2)
    MathBook.display_chapter_problems(6)

    
    

