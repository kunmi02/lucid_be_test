# Blog API - FastAPI + MySQL

## Setup

1. Clone the repo:
```bash
git clone <repo-url>
cd blog_api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up MySQL:
```bash

```

4. Run migrations:
```bash
alembic upgrade head
```

5. Run the app:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

### Users

- `POST /api/v1/register` - Register a new user
- `POST /api/v1/login` - Login and get an access token

### Posts

- `GET /api/v1/posts` - Get all posts
- `POST /api/v1/posts` - Create a new post
- `PUT /api/v1/posts/{post_id}` - Update an existing post
- `DELETE /api/v1/posts/{post_id}` - Delete a post

## Notes

- The API uses JWT authentication.
- Passwords are hashed using bcrypt.
- MySQL database is used for storage.
- The app is built with FastAPI and runs on port 8000.

## License

MIT License

## Contact

- Author: [Azeez Ibrahim](mailto:azeezibrahim02@gmail.com)
