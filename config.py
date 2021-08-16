import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:read432q@localhost/pitches'
    SECRET_KEY= os.environ.get("SECRET_KEY")
    
    UPLOADED_PHOTOS_DEST='app/static/photos'

    #email configuration
    