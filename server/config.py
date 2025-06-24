import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = os.getenv("DATABASE_URI")
SECRET_KEY = os.getenv("SECRET_KEY", "super-secret")

class Config:
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = SECRET_KEY
