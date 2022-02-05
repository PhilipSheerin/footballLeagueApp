from turtle import position
from flask import Blueprint, render_template, request, redirect
from website.forms import *
from website.api import *

#Blueprint from flask app 
views = Blueprint('views', __name__)

#Urls to navigate to

@views.route('/')
def default():
    connection = db_connection()
    cursor = connection.cursor()
    cursor = connection.execute("""SELECT PlayerName, WinGame, LoseGame, DrawGame, MatchesPlayed, Points FROM user  ORDER BY Points DESC LIMIT 20""")

    data = [
        dict(playerName=row[0], winGame=row[1], loseGame=row[2], drawGame=row[3], matchesPlayed=row[4], points=row[5])
        for row in cursor.fetchall()
        ]
    return render_template("home.html", data=data)

@views.route('/home')
def home():
    connection = db_connection()
    cursor = connection.cursor()
    cursor = connection.execute("""SELECT PlayerName, WinGame, LoseGame, DrawGame, MatchesPlayed, Points FROM user ORDER BY Points DESC LIMIT 20""")

    data = [
        dict(playerName=row[0], winGame=row[1], loseGame=row[2], drawGame=row[3], matchesPlayed=row[4], points=row[5])
        for row in cursor.fetchall()
        ]
    return render_template("home.html", data=data)

@views.route('/players', methods=["GET"])
def players():
    connection = db_connection()
    cursor = connection.cursor()
    cursor = connection.execute("""SELECT PlayerName, DominantFoot, Position, Attendance FROM user ORDER BY PlayerName ASC""")
    data = [
        dict(playerName=row[0], dominantFoot=row[1], position=row[2], attendance=row[3])
        for row in cursor.fetchall()
        ]
    return render_template("players.html", data=data)

@views.route('/teams', methods=["GET"])
def teamLineup():
    connection = db_connection()
    cursor = connection.cursor()
    cursor = connection.execute("""SELECT PlayerName FROM user ORDER BY PlayerName ASC LIMIT 7""")
    team1 = [
        dict(playerName=row[0])
        for row in cursor.fetchall()
        ]

    cursor = connection.cursor()
    cursor = connection.execute("""SELECT PlayerName FROM user ORDER BY PlayerName DESC LIMIT 7""")
    team2 = [
        dict(playerName=row[0])
        for row in cursor.fetchall()
        ]

    return render_template("teams.html", team1 = team1, team2 = team2)

#Player function views:
@views.route('/addPlayer', methods =["GET", "POST"])
def addPlayer():
    playerName = None
    dominantFoot = None
    position = None
    attendance = None
    addPlayerForm = NewUserForm()
    #Validate submit of form
    if addPlayerForm.validate_on_submit():
        #Capture form data
        playerName = addPlayerForm.playerName.data
        dominantFoot = addPlayerForm.dominantFoot.data
        position = addPlayerForm.position.data
        attendance = addPlayerForm.attendance.data

        connection = db_connection()
        cursor = connection.cursor()

        sql = """INSERT INTO user (PlayerName, DominantFoot, Position, Attendance, WinGame, LoseGame, DrawGame, MatchesPlayed, Points)
                 VALUES (?, ?, ?, ?, 0, 0, 0, 0, 0)"""
        cursor = cursor.execute(sql, (playerName, dominantFoot, position, attendance))
        connection.commit()
        
        #Clear data from form for next time
        addPlayerForm.playerName.data = ''
        addPlayerForm.dominantFoot.data = ''
        addPlayerForm.position.data = ''
        addPlayerForm.attendance.data = ''

        return redirect('/addPlayer')

    return render_template("addPlayer.html",
    #pass form fiels to template
    playername = playerName,
    dominantFoot = dominantFoot,
    position = position,
    attendance = attendance,
    addPlayerForm = addPlayerForm
    )

@views.route('/updatePlayer', methods =["GET", "POST"])
def updatePlayer():
    userID = None
    playerName = None
    dominantFoot = None
    position = None
    attendance = None
    updatePlayerForm = UpdateUserForm()
    #Validate submit of form
    if updatePlayerForm.validate_on_submit():
        #Capture form data
        userID = updatePlayerForm.userID.data
        playerName = updatePlayerForm.playerName.data
        dominantFoot = updatePlayerForm.dominantFoot.data
        position = updatePlayerForm.position.data
        attendance = updatePlayerForm.attendance.data

        connection = db_connection()
        cursor = connection.cursor()

        sql = """UPDATE user SET PlayerName = ?, DominantFoot = ?, Position = ?, Attendance = ? WHERE UserID = ?"""
        cursor = cursor.execute(sql, (playerName, dominantFoot, position, attendance, userID))
        connection.commit()
        
        #Clear data from form for next time
        updatePlayerForm.playerName.data = ''
        updatePlayerForm.dominantFoot.data = ''
        updatePlayerForm.position.data = ''
        updatePlayerForm.attendance.data = ''

        return redirect('/updatePlayer')

    return render_template("updatePlayer.html",
    #pass form fields to template
    userID = userID,
    playername = playerName,
    dominantFoot = dominantFoot,
    position = position,
    attendance = attendance,
    updatePlayerForm = updatePlayerForm
    )

@views.route('/deletePlayer', methods =["GET", "POST"])
def deletePlayer():
    userID = None
    deleteUserForm = DeleteUserForm()
    #Validate submit of form
    if deleteUserForm.validate_on_submit():
        #Capture form data
        userID = deleteUserForm.userID.data
        #DB connection
        connection = db_connection()
        cursor = connection.cursor()

        #SQL query
        sql = """DELETE FROM user WHERE UserID = ?"""
        cursor = cursor.execute(sql, (userID,))
        connection.commit()
        
        #Clear data from form for next time
        deleteUserForm.userID.data = ''

        return redirect('/deletePlayer')

    return render_template("deletePlayer.html",
    #pass form fiels to template
    userID = userID,
    deleteUserForm = deleteUserForm
    )

@views.route('/updateGameData', methods=["GET", "POST"])
def updateGameData():
    connection = db_connection()
    cursor = connection.cursor()
    cursor = connection.execute("""SELECT UserID, PlayerName FROM user ORDER BY userID ASC""")
    data = [
        dict(userID=row[0], playerName=row[1])
        for row in cursor.fetchall()
        ]

    #Handle button presses
    userID = None

    winGameButton = WinGame()
    drawGameButton = DrawGame()
    loseGameButton = LoseGame()
    mwinGameButton = RemoveWinGame()
    mdrawGameButton = RemoveDrawGame()
    mloseGameButton = RemoveLoseGame()

    #Validate submit of form
    
    if winGameButton.validate_on_submit():

        print("success")

        #Capture form data
        userID = winGameButton.userID.data
        connection = db_connection()
        cursor = connection.cursor()

        sql = """UPDATE user SET WinGame = WinGame + 1, MatchesPlayed = MatchesPlayed + 1, Points = Points + 3 WHERE UserID = ?"""
        cursor = cursor.execute(sql, (userID,))
        connection.commit()
        
        #Clear data from form for next time
        winGameButton.userID.data = ''

        return redirect('/udpateGameData')
    
    #Validate submit of form
    if drawGameButton.validate_on_submit():

        #Capture form data
        userID = drawGameButton.userID.data
        connection = db_connection()
        cursor = connection.cursor()

        sql = """UPDATE user SET DrawGame = DrawGame + 1, MatchesPlayed = MatchesPlayed + 1, Points = Points + 1 WHERE UserID = ?"""
        cursor = cursor.execute(sql, (userID,))
        connection.commit()
        
        #Clear data from form for next time
        drawGameButton.userID.data = ''

        return redirect('/udpateGameData')

    #Validate submit of form
    if loseGameButton.validate_on_submit():

        #Capture form data
        userID = loseGameButton.userID.data
        connection = db_connection()
        cursor = connection.cursor()

        sql = """UPDATE user SET LoseGame = LoseGame + 1, MatchesPlayed = MatchesPlayed + 1 WHERE UserID = ?"""
        cursor = cursor.execute(sql, (userID,))
        connection.commit()
        
        #Clear data from form for next time
        loseGameButton.userID.data = ''

        return redirect('/udpateGameData')


    #Validate submit of form
    if mwinGameButton.validate_on_submit():

        #Capture form data
        userID = mwinGameButton.userID.data
        connection = db_connection()
        cursor = connection.cursor()

        sql = """UPDATE user SET WinGame = WinGame - 1, MatchesPlayed = MatchesPlayed - 1, Points = Points - 3 WHERE UserID = ?"""
        cursor = cursor.execute(sql, (userID,))
        connection.commit()
        
        #Clear data from form for next time
        mwinGameButton.userID.data = ''

        return redirect('/udpateGameData')
    
    #Validate submit of form
    if mdrawGameButton.validate_on_submit():

        #Capture form data
        userID = mdrawGameButton.userID.data
        connection = db_connection()
        cursor = connection.cursor()

        sql = """UPDATE user SET DrawGame = DrawGame - 1, MatchesPlayed = MatchesPlayed - 1, Points = Points - 1 WHERE UserID = ?"""
        cursor = cursor.execute(sql, (userID,))
        connection.commit()
        
        #Clear data from form for next time
        mdrawGameButton.userID.data = ''

        return redirect('/udpateGameData')

    #Validate submit of form
    if mloseGameButton.validate_on_submit():

        #Capture form data
        userID = mloseGameButton.userID.data
        connection = db_connection()
        cursor = connection.cursor()

        sql = """UPDATE user SET LoseGame = LoseGame - 1, MatchesPlayed = MatchesPlayed - 1 WHERE UserID = ?"""
        cursor = cursor.execute(sql, (userID,))
        connection.commit()
        
        #Clear data from form for next time
        mloseGameButton.userID.data = ''

        return redirect('/udpateGameData')

    
    return render_template("updateGameData.html", 
        data=data,
        userID = userID,
        winGameButton = winGameButton,
        drawGameButton = drawGameButton,
        loseGameButton = loseGameButton,
        mwinGameButton = mwinGameButton,
        mdrawGameButton = mdrawGameButton,
        mloseGameButton = mloseGameButton
        )


