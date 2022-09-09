__author__ = "Andrei Stefan"
__version__ = "1.0.0"
__email__ = "andistef29@gmail.com"
__status__ = "Production"

import random


def print_roman(num):
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
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


class book:
    def __init__(self, chapters):
        self.chapters = chapters
        self.problems = dict()

    def display_chapters(self):
        print(f"There are {self.chapters} chapters in this book.")

    def register_problems(self, chapterNumber, numberProblems):
        if int(chapterNumber) <= (int(self.chapters)):
            self.problems[chapterNumber] = numberProblems

    def display_chapter_problems(self, chapterNumber):
        if chapterNumber > self.chapters:
            print("The number of chapters are not yet defined.")
        elif chapterNumber not in self.problems:
            print("The number of problems for this chapter was not defined yet.")
        else:
            print(f"There are {self.problems[chapterNumber]} problems in chapter {print_roman(chapterNumber)}.")

    def random_generator(self, studentName, homeworkNumberProblems):
        print(f"\nHomework generated for student {studentName} is:")
        while True:
            randomChapter = random.randint(1, self.chapters)
            if self.problems[randomChapter] > homeworkNumberProblems:
                break
        print(
            f"From chapter {randomChapter}, following problems: {sorted(random.sample(range(1, self.problems[randomChapter]), homeworkNumberProblems))}")
