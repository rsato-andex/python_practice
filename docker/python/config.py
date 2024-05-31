class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://docker:docker@db/python_sample'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
