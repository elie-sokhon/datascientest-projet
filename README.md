# Technical project

This project is about creating the backend API of a lobby where the user can login using only a username, be able to see who's online and be able to send messages to other online users, in real time.

This backend provides:

* REST API for user login, logout, and listing connected users
* Real-time messaging with WebSockets
* SQLite database with SQLAlchemy models
* Fully linted and tested codebase with pre-commit hooks and GitHub Actions CI

Tech Stack

* Python 3.11.6
* Flask + Flask-SocketIO
* Flask-SQLAlchemy + Flask-Migrate
* Flask-RESTful
* Pytest for unit tests
* pre-commit hooks (black, isort, flake8)
* GitHub Actions for continuous integration

## How to Run Locally

1. Clone Repository

Using bash, run these commands: 
git clone https://github.com/elie-sokhon/datascientest-projet.git

2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate  

3. Install Dependencies

pip install -r requirements.txt

4. Setup Environment Variables

Create a file called `.env` inside `backend/` folder and add this line:

SECRET_KEY=supersecretkey

5. Initialize Database

cd backend
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

6. Run the Application

cd backend
flask run

The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).


## API Documentation

POST `/login`

* **Body:** `{ "pseudonym": "JohnDoe" }`
* **Response:** 200 OK `{ "id": 1, "pseudonym": "JohnDoe", "is_connected": true, "created_at": "..." }`

GET `/users`

* **Response:** List of currently connected users.

POST `/logout`

* **Body:** `{ "pseudonym": "JohnDoe" }`
* **Response:** 200 OK

## Real-Time Messaging with SocketIO

When a client emits a `send_message` event:
The backend broadcasts the message to all connected clients.
Example payload:

```json
{
  "sender": "JohnDoe",
  "content": "Hello world!",
  "timestamp": "2024-05-14T14:23:00Z"
}
```

Clients listen to the `new_message` event to receive updates.

## Testing

Run tests from project root:

cd backend
pytest

## Code Quality & Pre-commit

Before committing:

```bash
black .
isort .
flake8 .
```

or run pre-commit:

```bash
pre-commit run --all-files
```

The project uses black, isort, and flake8 for code quality.

## Continuous Integration

GitHub Actions workflow:

* Runs pytest
* Runs flake8

Every push & PR to `main` will trigger the pipeline automatically.

Developed by: Elie Sokhon

