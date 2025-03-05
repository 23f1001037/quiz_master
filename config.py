from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path=".env", override=True)

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False') == 'True'

# Debugging
print("SECRET_KEY:", Config.SECRET_KEY)
print("DATABASE_URI:", Config.SQLALCHEMY_DATABASE_URI)
