from django.db import models
from django.contrib.auth.models import User
# imports

class Message(models.Model):
    # create a new class called Message which inherits from models.Model
    # every class in models.py is a table in the database, 
    # and every attribute of the class is a column in the table
    
    # in SQL, this is a VARCHAR(255) column
    # it is a column which consists of a room name with max length of 255
    room = models.CharField(max_length=255) 

    # in SQL, this is a use_id column with type of INTEGER
    # Foreign Key is a type of relationship between two tables,
    # in this case, the Message table has a foreign key to the User table
    # for example, one user can have many messages, but one message can only belong to one user
    # so we add ForeignKey to be able to add the messages to User table
    # CASCADE is a type of relationship between two tables, 
    # which means that if the user is deleted, 
    # all messages related to that user will be deleted as well
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # In SQL, this is a TEXT column, with no limit on the length of the text
    # it is a column which consists of the content of the message
    content = models.TextField()
    # In SQL, this is a DATETIME column,
    # auto_now_add=True means that the timestamp will be set to the current time, 
    # when the message is created
    # it is a column which consists of the timestamp when the message was sent
    timestamps = models.DateTimeField(auto_now_add=True)

    # just fancy representation of the message in the database
    def __str__(self):
        return f'{self.user.username}: {self.content[:20]}'


# in database all of this will be represented like that:  
    #     CREATE TABLE room_message (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     room VARCHAR(255) NOT NULL,
    #     user_id INTEGER NOT NULL REFERENCES auth_user(id),
    #     content TEXT NOT NULL,
    #     timestamps DATETIME NOT NULL
    # );
# Django will automatically create the table in the database when we run the migrations
# And Django automatically creates id column
