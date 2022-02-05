from flask import Flask, request, jsonify, Blueprint
import json
import sqlite3

#app = Flask(__name__)

apiView = Blueprint('api', __name__)

#-----------------------------------------------------------------------------------#
#Database connection
def db_connection():
    connection = None
    try:
        connection = sqlite3.connect('database.db', check_same_thread=False)
    except sqlite3.error as e:
        print(e)
    return connection

@apiView.route("/playerGameData", methods=["GET"])
def playerGameData():

    connection = db_connection()
    if request.method =="GET":
        cursor = connection.execute("SELECT * FROM PlayerGameData ORDER BY Points DESC")
        data = [
            dict(UserId=row[1], WinGame=row[2], LoseGame=row[3], DrawGame=row[4], MatchesPlayed=row[5], Points=row[6])
            for row in cursor.fetchall()
            ]
    if playerGameData is not None:
        return jsonify(data)

#---------------------------------------------------------#
#Game data updates based on user id

@apiView.route("/updateGameData/win/<int:id>", methods=["POST"])
def updateGameDataWim():
    connection = db_connection()
    cursor = connection.cursor()

    userID = request.form["userID"]

    if request.method == "POST":
        sql = """UPDATE playerGameData SET winGame = winGame + 1, points = points + 3, matchesPlayed = matchesPlayed + 1 WHERE UserID = ?"""

        cursor.execute(sql, (userID, id))
        connection.commit()
        return jsonify(userID)

@apiView.route("/updateGameData/loss/<int:id>", methods=["POST"])
def updateGameDataLoss():
    connection = db_connection()
    cursor = connection.cursor()

    if request.method == "POST":
        sql = """UPDATE playerGameData SET winGame = loseGame + 1, matchesPlayed = matchesPlayed + 1 WHERE UserID = ?"""

        userID = request.form["userID"]
        cursor.execute(sql, (userID, id))
        connection.commit()
        return jsonify(userID)

@apiView.route("/updateGameData/draw/<int:id>", methods=["POST"])
def updateGameDataDraw():
    connection = db_connection()
    cursor = connection.cursor()

    if request.method == "POST":
        sql = """UPDATE playerGameData SET drawGame = drawGame + 1, points = points + 1, matchesPlayed = matchesPlayed + 1 WHERE UserID = ?"""

        userID = request.form["userID"]
        cursor.execute(sql, (userID, id))
        connection.commit()
        return jsonify(userID)
#------------------------------------------------------#


#------------------------------------------------------#
#Player API calls

@apiView.route("/playerData", methods=["GET"])
def playerData():
    connection = db_connection()
    cursor = connection.cursor()

    if request.method =="GET":
        cursor = connection.execute("SELECT * FROM user ORDER BY UserID DESC")
        data = [
            dict(UserId=row[0], PlayerName=row[1], DominantFoot=row[2], Postion=row[3], Attendance=row[4])
            for row in cursor.fetchall()
            ]
    if playerData is not None:
        return jsonify(data)
#-------------------------------------------------------------------#



# @app.route("/plot/<int:id>", methods=["GET", "PUT", "DELETE"])
# def single_plot(id):
#     connection = db_connection()
#     cursor = connection.cursor()
#     plot = None
#     if request.method == "GET":
#         cursor.execute("SELECT * FROM plots WHERE PlotId=?", (id,))
#         rows = cursor.fetchall()
#         for r in rows:
#             plot = r
#         if plot is not None:
#             return jsonify(plot), 200
#         else:
#             return "Something wrong", 404

#     if request.method == "PUT":
#         sql = """UPDATE plots
#                 SET PlotTitle=?,
#                     PlotText=?,
#                 WHERE PlotId=? """

#         plotTitle = request.form["PlotTitle"]
#         plotText = request.form["PlotText"]
#         updated_plot = {
#             "PlotId": id,
#             "PlotTitle": plotTitle,
#             "PlotText": plotText
#         }
#         connection.execute(sql, (plotTitle, plotText, id))
#         connection.commit()
#         return jsonify(updated_plot)

#     if request.method == "DELETE":
#         sql = """ DELETE FROM plots WHERE PlotId=? """
#         connection.execute(sql, (id,))
#         connection.commit()
#         return "The plot with id: {} has been deleted.".format(id), 200


# if __name__ == "__main__":
#     #Only run when testing
#     app.run(debug=True)
