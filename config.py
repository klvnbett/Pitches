import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:read432q@localhost/pitch'
    SECRET_KEY= os.environ.get("SECRET_KEY")
    
    UPLOADED_PHOTOS_DEST='app/static/photos'

    #email configuration

    class DevConfig(config):
        Debug =True


    class ProdConfig(Config):
        pass

    Config_options ={
        'development':DevConfig,
        'production' :ProdConfig
    }
    