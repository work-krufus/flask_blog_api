import unittest
from app import create_app, db


class BlogTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app.config["SQLALCHEMY_DATABASE_URI"] = (
            "postgresql://username:password@localhost:5432/blog_api_test"
        )
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_registration(self):
        response = self.client.post(
            "/api/register", json={"username": "testuser", "password": "testpassword"}
        )
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        self.client.post(
            "/api/register", json={"username": "testuser", "password": "testpassword"}
        )
        response = self.client.post(
            "/api/login", json={"username": "testuser", "password": "testpassword"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json)

    def test_create_blog_post(self):
        self.client.post(
            "/api/register", json={"username": "testuser", "password": "testpassword"}
        )
        login_response = self.client.post(
            "/api/login", json={"username": "testuser", "password": "testpassword"}
        )
        token = login_response.json["access_token"]
        response = self.client.post(
            "/api/posts",
            json={
                "title": "Test Post",
                "content": "This is a test post. That are greater than 50 characters in length so it doesnot give an error",
            },
            headers={"Authorization": f"Bearer {token}"},
        )
        self.assertEqual(response.status_code, 201)

    def test_get_blog_posts(self):
        response = self.client.get("/api/posts")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
