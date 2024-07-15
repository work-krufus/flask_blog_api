from flask import Blueprint
from flask_restful import Api
from .resources import UserRegistration, UserLogin, BlogPostResource, BlogPostList

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

api.add_resource(UserRegistration, "/register")
api.add_resource(UserLogin, "/login")
api.add_resource(BlogPostList, "/posts")
api.add_resource(BlogPostResource, "/posts/<int:post_id>")
