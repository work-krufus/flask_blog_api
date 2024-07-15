### Blogging Platform API

This project is a simple blogging platform with a RESTful API built using Python Flask. It includes user authentication, blog post management, and error handling.

## Features

- User Registration
- User Login
- JWT-based Authentication
- Create, Retrieve, Update, and Delete (CRUD) operations for blog posts
- Error handling and validation

## Prerequisites

- Python 3.7+
- Virtualenv

## Setup

### 1. Clone the repository
```
git clone https://github.com/yourusername/blogging_platform.git
cd blogging_platform

```
### 2. Create and activate a virtual environment
```
python3 -m venv venv
source venv/bin/activate

```
### 3. Install dependencies
```
pip install -r requirements.txt

```
### 4. Set up environment variables

Create a `.env` file in the root directory of the project and add the following environment variables:
```
SECRET_KEY=my_precious
JWT_SECRET_KEY=my_precious_jwt
DATABASE_URL=sqlite:///blog.db

```
### 5. Initialize the database
```
flask db init 
flask db migrate 
flask db upgrade
```
## Running the Application

### 1. Start the Flask server
```
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```
The application will be available at `http://127.0.0.1:5000`

## API Endpoints

### User Registration

- **URL:** `/api/register`
- **Method:** `POST`
- **Request Body:**
```
{
    "username": "string",
    "password": "string"
}
```
- **Response:**
```
{
    "message": "User registered successfully"
}

```
### User Login

- **URL:** `/api/login`
- **Method:** `POST`
- **Request Body:**
```
{
    "username": "string",
    "password": "string"
}
```
- **Response:**

```
{
    "access_token": "string"
}
```
### Create a Blog Post

- **URL:** `/api/posts`
- **Method:** `POST`
- **Headers:**
```
Authorization: Bearer <access_token>

```
- **Request Body:**
```
{
    "message": "Post created successfully",
    "post_id": "integer"
}
```
- **Response**
```
{
    "message": "Post created successfully",
    "post_id": "integer"
}
```
### Retrieve All Blog Posts

- **URL:** `/api/posts`
- **Method:** `GET`
- **Response:**
```
[
    {
        "id": "integer",
        "title": "string",
        "content": "string",
        "date_posted": "datetime",
        "user_id": "integer"
    }
]
```
### Retrieve a Single Blog Post

- **URL:** `/api/posts/<int:post_id>`
- **Method:** `GET`
- **Response:**
```
{ "id": "integer", "title": "string", "content": "string", "date_posted": "datetime", "user_id": "integer" }
```
### Update a Blog Post

- **URL:** `/api/posts/<int:post_id>`
- **Method:** `PUT`
- **Headers:**
```
Authorization: Bearer <access_token>
```
- **Request Body:**
```
{
    "title": "string",
    "content": "string"
}
```
- **Response:**
```
{
    "message": "Post updated successfully"
}
```
### Delete a Blog Post

- **URL:** `/api/posts/<int:post_id>`
- **Method:** `DELETE`
- **Headers:**
```
Authorization: Bearer <access_token>
```
- **Response:**
```
{
    "message": "Post deleted successfully"
}
```
## Error Handling

The API uses custom error handling for validation, not found, and unauthorized errors. Responses are returned with appropriate HTTP status codes and error messages in JSON format.

### Example Error Response
```
{
    "error": "Validation error message"
}

```
## Running Tests

Unit tests are included to ensure the functionality of the API.

### Run the tests:
```
python -m unittest discover tests
```
## Directory Structure
```
blogging_platform/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── exceptions.py
│
├── tests/
│   ├── test_blog.py
│
├── config.py
├── run.py
├── requirements.txt
```