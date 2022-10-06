from flask import Flask, render_template
from peewee import *

db = "Todos.db"
database = SqliteDatabase(db)

class BaseModel(Model):
	class Meta:
		database=database

class User(BaseModel):
	id = AutoField(primary_key=True)
	name = CharField()
	username = CharField(unique=True)
	password = CharField()

class Todo(BaseModel):
	id = AutoField(primary_key=True)
	todo = TextField()
	description = TextField()

class create_tables():
	with database:
		database.create_tables([User, Todo])

app = Flask(__name__)

@app.route('/')
def index():
	data_todo = Todo.select()
	return render_template("index.html", data=data_todo)

if __name__ == '__main__':
	create_tables()
	app.run()