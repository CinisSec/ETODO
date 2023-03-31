import sqlite3
import argparse

conn = sqlite3.connect('Entertainment.db')

def createTables():
    conn.execute('''CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY,title TEXT NOT NULL)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS series (id INTEGER PRIMARY KEY,title TEXT NOT NULL,season INTEGER NOT NULL, episode INTEGER NOT NULL)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY,title TEXT NOT NULL, platform TEXT NOT NULL)''')

def addMovie():
    movieTitle = input("Please input movie title:  ")
    conn.execute('INSERT INTO movies(title) VALUES (?)', (movieTitle,))
    conn.commit()
    print("Movie added to DB!")

def addSeries():
    seriesTitle = input("Please input movie: ")
    sve = input("Did you watch a episodes before? [y/n]")
    if sve == "y":
        snum = int(input("Which season?: [1-99] "))
        epinum = int(input("Which episode?: [1-99]"))
    else:
        snum = 1
        epinum = 1
    conn.execute('INSERT INTO series(title, season, episode) VALUES (?,?,?)', (seriesTitle,snum,epinum))
    conn.commit()
    print("Series added to DB!\n\n")

def addGame():
    gameTitle = input("Please input game title: ")
    platform = input("On which platform?: ")
    conn.execute('INSERT INTO games(title, platform) VALUES (?,?)', (gameTitle,platform))
    conn.commit()
    print("Game added to DB!")

def getMovies():
    movies = conn.execute('SELECT * FROM movies')
    print("ID - Title")
    for row in movies:
        print(f'{row[0]} - {row[1]}')

def getSeries():
    series = conn.execute('SELECT * FROM series')
    print("ID - Title - Season - Episode")
    for row in series:
        print(f'{row[0]} - {row[1]} - {row[2]} - {row[3]}')

choice = 0
createTables()
while choice != "q":
    print("Welcome to ETODO!")
    print("Add a movies [1]")
    print("Add a series [2]")
    print("Show movies to watch [3]")
    print("Show movies to watch [4]")
    print("Quit [q]")
    
    choice = input("What would you like to do?")
    if choice == "1":
        addMovie()
    elif choice == "2":
        addSeries()
    elif choice == "3":
        getMovies()
    elif choice == "4":
        getSeries()
