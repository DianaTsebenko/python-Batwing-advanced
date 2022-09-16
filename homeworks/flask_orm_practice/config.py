class Config:
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = "postgresql://library:library@db:5432/library?sslmode=disable"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
