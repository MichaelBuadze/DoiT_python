import os

class Config:
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://openroot:openRoot2501@localhost:3307/lesson34_hw'
  SQLALCHEMY_ECHO = True
  SECRET_KEY = os.urandom(32)
