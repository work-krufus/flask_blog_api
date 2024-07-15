from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .models import User, BlogPost
from exceptions import ValidationError, NotFoundError, UnauthorizedError
from . import db


class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        if "username" not in data or "password" not in data:
            raise ValidationError("Username and password are required.")
        if User.query.filter_by(username=data["username"]).first():
            raise ValidationError("Username already exists.")
        new_user = User(username=data["username"])
        new_user.set_password(data["password"])
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User registered successfully"}, 201


class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        if "username" not in data or "password" not in data:
            raise ValidationError("Username and password are required.")
        user = User.query.filter_by(username=data["username"]).first()
        if not user or not user.check_password(data["password"]):
            raise UnauthorizedError("Invalid credentials.")
        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token}, 200


class BlogPostResource(Resource):

    def get(self, post_id):
        post = BlogPost.query.get(post_id)
        if not post:
            raise NotFoundError("Post not found.")
        return {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "date_posted": post.date_posted,
            "user_id": post.user_id,
        }

    @jwt_required()
    def put(self, post_id):
        user_id = get_jwt_identity()
        post = BlogPost.query.get(post_id)
        if not post:
            raise NotFoundError("Post not found.")
        if post.user_id != user_id:
            raise UnauthorizedError("Permission denied.")
        data = request.get_json()
        if "title" not in data or "content" not in data:
            raise ValidationError("Title and content are required.")
        post.title = data["title"]
        post.content = data["content"]
        db.session.commit()
        return {"message": "Post updated successfully"}

    @jwt_required()
    def delete(self, post_id):
        user_id = get_jwt_identity()
        post = BlogPost.query.get(post_id)
        if not post:
            raise NotFoundError("Post not found.")
        if post.user_id != user_id:
            raise UnauthorizedError("Permission denied.")
        db.session.delete(post)
        db.session.commit()
        return {"message": "Post deleted successfully"}


class BlogPostList(Resource):
    def get(self):
        posts = BlogPost.query.all()
        return [
            {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "date_posted": post.date_posted,
                "user_id": post.user_id,
            }
            for post in posts
        ]

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()
        if "title" not in data or "content" not in data:
            raise ValidationError("Title and content are required.")
        new_post = BlogPost(
            title=data["title"], content=data["content"], user_id=user_id
        )
        db.session.add(new_post)
        db.session.commit()
        return {"message": "Post created successfully"}, 201
