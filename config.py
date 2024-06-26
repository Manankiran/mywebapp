import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://blog_user:password@localhost/blog_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

