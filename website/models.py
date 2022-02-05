import sqlite3

#Create DB file
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

#Create User Table
userTable = """CREATE TABLE IF NOT EXISTS user(
                    UserId INTEGER PRIMARY KEY, 
                    PlayerName TEXT, 
                    DominantFoot TEXT,
                    Position TEXT,
                    Attendance TEXT,
                    WinGame INTEGER,
                    LoseGame INTEGER,
                    DrawGame INTEGER,
                    MatchesPlayed INTEGER,
                    Points INTEGER);"""

cursor.execute(userTable)

#Create User inputted data table
playGameDataTable = """CREATE TABLE IF NOT EXISTS playerGameData(
                        playerGameDataID INTEGER PRIMARY KEY, 
                        UserID INTEGER, 
                        WinGame INTEGER,
                        LoseGame INTEGER,
                        DrawGame INTEGER,
                        MatchesPlayed INTEGER,
                        Points INTEGER,
                        FOREIGN KEY(UserId) REFERENCES userTable(UserId));"""

cursor.execute(playGameDataTable)

#Create plots table
previousGameDataTable = """CREATE TABLE IF NOT EXISTS previousGameData(
                    PreviousGameDataID INTEGER PRIMARY KEY, 
                    UserID INTEGER,  
                    DatePlayed DATE,
                    WinGame INTEGER,
                    LoseGame INTEGER,
                    DrawGame INTEGER, 
                    FOREIGN KEY(UserId) REFERENCES userTable(UserId));"""

cursor.execute(previousGameDataTable)
