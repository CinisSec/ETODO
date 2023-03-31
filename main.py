import sqlite3

conn = sqlite3.connect('entertainment.db')

def createTables():
    conn.execute('''CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY,title TEXT NOT NULL)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS series (id INTEGER PRIMARY KEY,title TEXT NOT NULL,season INTEGER NOT NULL, episode INTEGER NOT NULL)''')

def addMovie():
    movieTitle = input("Please input movie title to add to DB: ")
    conn.execute('INSERT INTO movies(title) VALUES (?)', (movieTitle))
    conn.commit()
    print("Movie added to DB!")

def addSeries():
    seriesTitle = input("Please input movie title to add to DB: ")
    sve = input("Did you watch a season before?")
    if sve == "yes":
        snum = int(input("Which season?: [1-99] "))
        epinum = int(input("Which episode?: [1-99]"))
    else:
        snum = 1
        epinum = 1
    conn.execute('INSERT INTO series(title, season, episode) VALUES (?,?,?)', (seriesTitle,snum,epinum))
    conn.commit()
    print("Series added to DB!")

def getMovies():
    movies = conn.execute('SELECT * FROM movies')
    print("ID - Title")
    for row in movies:
        print(f'{row[0]} - {row[1]}')

choice = 0
createTables()
while choice != "q":
    print("Welcome to ETODO!")
    print("Add a movies [1]")
    print("Add a series [2]")
    print("Show movies to watch [3]")
    print("Quit [q]")
    choice = input("What would you like to do?")
    if choice == "1":
        addMovie()
    elif choice == "2":
        addSeries()
    elif choice == "3":
        getMovies()