import os


class Settings:
    pass


class DevSettings(Settings):
    """Settings for development environment."""
    DB_NAME = 'dev.sqlite'
    APP_DIR = os.path.abspath(__file__)
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///database/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


profiles = {
    'development': DevSettings
}
