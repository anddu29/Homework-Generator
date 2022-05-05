from pkg_resources import working_set

def printRoman(num):
        val = [
                1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4,
                1
                ]
        syb = [
                "M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV",
                "I"
                ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
class book:
    def __init__(self, chapters):
        self.chapters = chapters
        self.problems = dict()

    def display_chapters (self):
        
        print (f"There are {self.chapters} chapters in this book.")

    def register_problems (self,chapter_number,number_problems):
        if int(chapter_number) <= (int(self.chapters)):
            self.problems[chapter_number] = number_problems

    def display_chapter_problems (self,chapter_number):
        if chapter_number > self.chapters:
            print ("The number of chapters are not yet defined.")
        elif chapter_number not in self.problems:
            print("The number of problems for this chapter was not defined yet.")
        else:
            print (f"There are {self.problems[chapter_number]} problems in chapter {printRoman(chapter_number)}.")    
    