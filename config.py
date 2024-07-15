import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://localhost:5432/blog_api_test"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "my_precious_jwt")
