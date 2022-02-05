from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, HiddenField
from wtforms.validators import DataRequired


#Create form class
class NewUserForm(FlaskForm):
    playerName = StringField ("Player's Name", validators=[DataRequired()])
    dominantFoot = StringField ("Player's Dominant Foot", validators=[DataRequired()])
    position = StringField ("Player's Position", validators=[DataRequired()])
    attendance = StringField ("Player's Attendance", validators=[DataRequired()])
    submit = SubmitField("Add player")

class UpdateUserForm(FlaskForm):
    userID = StringField("Player's User ID", validators=[DataRequired()])
    playerName = StringField ("Player's Name", validators=[DataRequired()])
    dominantFoot = StringField ("Player's Dominant Foot", validators=[DataRequired()])
    position = StringField ("Player's Position", validators=[DataRequired()])
    attendance = StringField ("Player's Attendance", validators=[DataRequired()])
    submit = SubmitField("Update player")

class DeleteUserForm(FlaskForm):
    userID = StringField("Player's UserID", validators=[DataRequired()])
    submit = SubmitField("Delete Player")


class WinGame(FlaskForm):
    userID = HiddenField("UserID", validators=[DataRequired()])
    submit = SubmitField("+Win")

class DrawGame(FlaskForm):
    userID = HiddenField("UserID", validators=[DataRequired()])
    submit = SubmitField("+Draw")

class LoseGame(FlaskForm):
    userID = HiddenField("UserID", validators=[DataRequired()])
    submit = SubmitField("+Lose")

class RemoveWinGame(FlaskForm):
    userID = HiddenField("UserID", validators=[DataRequired()])
    submit = SubmitField("-Win")

class RemoveDrawGame(FlaskForm):
    userID = HiddenField("UserID", validators=[DataRequired()])
    submit = SubmitField("-Draw")

class RemoveLoseGame(FlaskForm):
    userID = HiddenField("UserID", validators=[DataRequired()])
    submit = SubmitField("-Lose")
