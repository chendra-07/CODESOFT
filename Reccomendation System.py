import os, re, random

class Books:
    def count_words(gen):
        total_words = 0
        genre_list = []
        for i in gen:
            if (i == "+"):
                word_list = gen.split("+")
            else:
                word_list = gen.split()
        for word in word_list:
            if word.lower() not in ["and", ",", "+"]:
                total_words += 1
                genre_list.append(word.lower())
        return total_words, genre_list

    def nyear(file_path, genre_list):
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() in genre_list:
                    GenreF = f"Books/{line.strip()}.txt"
                    Genrep = os.path.join(os.path.dirname(__file__), GenreF)
                    try:
                        with open(Genrep, 'r') as file:
                            lines = file.readlines()
                            ind = random.randint(0, 12)
                            for i in range(ind):
                                index = random.randint(0, 50)
                                random_line = lines[index]
                                print(random_line.strip())
                    except FileNotFoundError:
                        print(f"File not found for genre: {line.strip()}")


class Movies:
    def count_words(gen):
        total_words = 0
        genre_list = []
        for i in gen:
            if (i == "+"):
                word_list = gen.split("+")
            else:
                word_list = gen.split()
        for word in word_list:
            if word.lower() not in ["and", ",", "+"]:
                total_words += 1
                genre_list.append(word.lower())
        return total_words, genre_list

    def nyear(file_path, genre_list):
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() in genre_list:
                    GenreF = f"Movies/{line.strip()}.txt"
                    Genrep = os.path.join(os.path.dirname(__file__), GenreF)
                    try:
                        with open(Genrep, 'r') as file:
                            for l in file:
                                print(l.strip())
                                print("\n")
                    except FileNotFoundError:
                        print(f"File not found for genre: {line.strip()}")

    def oneyear(file_path, genre_list, year):
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() in genre_list:
                    GenreF = f"Movies/{line.strip()}.txt"
                    Genrep = os.path.join(os.path.dirname(__file__), GenreF)
                    try:
                        with open(Genrep, 'r') as file:
                            for l in file:
                                y = [char for char in l if char.isdigit()]
                                result = ''.join(y)
                                if int(result) >= int(year) and int(result) < (int(year)+10):
                                    print(l.strip())
                                else:
                                    y = []
                            print("\n")
                    except FileNotFoundError:
                        print(f"File not found for genre: {line.strip()}")

def Movie():
    GenreFile = "Genre.txt"
    Genrepath = os.path.join(os.path.dirname(__file__), GenreFile)

    gen = input("Enter the genres of the movie you feel like watching?\n")
    gen = gen.replace(", ", " ")
    total_words, genre_list = Movies.count_words(gen)

    year = input("Enter the era of the movie you want to watch(Ex: 2010s)\n")

    if  (year.lower() == "any" or year.lower() == "any year" or year.lower() == "any era"):
        Movies.nyear(Genrepath, genre_list)

    elif len(year) == 4 or len(year) == 5:
        year = ''.join(re.findall(r'\d', year))
        Movies.oneyear(Genrepath, genre_list, year)

def Book():
    GenreFile = "GenreBook.txt"
    Genrepath = os.path.join(os.path.dirname(__file__), GenreFile)

    gen = input("Enter the genres of Books do you wish to read?\n")
    gen = gen.replace(", ", " ")
    total_words, genre_list = Books.count_words(gen)

    Books.nyear(Genrepath, genre_list)

ch = input("""\nWelcome to Book and Movie Reccomendation!
Do you want to read a BOOK or watch a MOVIE\n""")
ch = ch.lower()

if "movies" in ch or "movie" in ch:
    Movie()

elif "books" in ch or "book" in ch:
    Book()

