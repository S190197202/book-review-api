# Book Review API

A Django REST Framework project for managing a digital book review library with JWT Authentication system.

## How to Run the Project Locally

1. **Clone the repository:**

   ```bash
   git clone https://github.com/S190197202/book-review-api.git
   cd book-review-api
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # For Mac/Linux
   # or
   .venv\Scripts\activate      # For Windows
   ```

3. **Install the project dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

## 🧪 How to Test Each Endpoint
You can use Postman or curl to test the API endpoints.

### Authentication

- **Register a new user:**
  ```http
  POST /api/register/
  ```

- **Obtain JWT token:**
  ```http
  POST /api/token/
  ```

- **Refresh JWT token:**
  ```http
  POST /api/token/refresh/
  ```

- **Change password:**
  ```http
  POST /api/change-password/
  ```

### Book Management

- **List all books:**
  ```http
  GET /api/books/
  ```

- **Retrieve book details:**
  ```http
  GET /api/books/<id>/
  ```

- **Add a new book (Admin only):**
  ```http
  POST /api/books/
  ```

- **Edit a book (Admin only):**
  ```http
  PUT /api/books/<id>/
  ```

- **Delete a book (Admin only):**
  ```http
  DELETE /api/books/<id>/
  ```

### Review Management

- **Add a review to a book:**
  ```http
  POST /api/books/<book_id>/reviews/
  ```

- **List all reviews for a book:**
  ```http
  GET /api/books/<book_id>/reviews/
  ```

- **Edit a review (Review owner only):**
  ```http
  PUT /api/reviews/<id>/
  ```

- **Delete a review (Review owner only):**
  ```http
  DELETE /api/reviews/<id>/
  ```

## Authentication Mechanism
This project uses JWT (JSON Web Tokens) for authentication, powered by SimpleJWT:

Upon successful login, users receive an access token and a refresh token.

- The access token is used for accessing secured API endpoints.
- When the access token expires, the refresh token can be used to obtain a new access token without needing to log in again.

## Admin Credentials for Testing
- **Admin Panel URL:** `/admin/`
- **Username:** admin
- **Password:** Admin1122233





