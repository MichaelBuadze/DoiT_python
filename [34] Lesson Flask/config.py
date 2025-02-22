import os

class Config:
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://openroot:openRoot2501@localhost:3307/lesson33_todo_app_flask'
  SQLALCHEMY_ECHO = True
  SECRET_KEY = os.urandom(32)