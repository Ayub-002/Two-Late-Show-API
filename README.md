# 🌙 Late Show API

A Flask REST API for managing guests, episodes, and appearances on a Late Night TV show — built using Flask, PostgreSQL, and JWT Authentication.

---

## ✅ Features

- RESTful routes using Flask
- PostgreSQL database (no SQLite!)
- Token-based authentication with JWT
- MVC architecture
- Relationships:
  - Guests can appear in many episodes
  - Episodes can have many guests
- Protected routes with JWT
- Postman collection for testing all endpoints

---

## 📁 Project Structure

late-show-api-challenge/
├── server/
│ ├── app.py
│ ├── config.py
│ ├── seed.py
│ ├── models/
│ │ ├── user.py
│ │ ├── guest.py
│ │ ├── episode.py
│ │ └── appearance.py
│ ├── controllers/
│ │ ├── auth_controller.py
│ │ ├── guest_controller.py
│ │ ├── episode_controller.py
│ │ └── appearance_controller.py
├── migrations/
├── .env
├── Pipfile
├── challenge-4-lateshow.postman_collection.json
└── README.md

yaml
Copy
Edit

---

## 🛠 Setup Instructions

1. Clone the repo

git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
2. Install dependencies
bash
Copy
Edit
pipenv install
pipenv shell
3. Create PostgreSQL database
sql
Copy
Edit
CREATE DATABASE late_show_db;
4. Add environment variables in .env
ini
Copy
Edit
DATABASE_URI=postgresql://<username>:<password>@localhost:5432/late_show_db
SECRET_KEY=your_jwt_secret
🔧 Run the App
Run Migrations
bash
Copy
Edit
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Seed the Database
bash
Copy
Edit
python server/seed.py
Run the Server
bash
Copy
Edit
flask run
🔐 Authentication Flow
Register → /register

Login → /login

You’ll receive a JWT token

Send it in protected requests using:

makefile
Copy
Edit
Authorization: Bearer <your_token>
📡 Routes
Method	Route	Auth?	Description
POST	/register	❌	Register a new user
POST	/login	❌	Login and receive JWT token
GET	/guests	❌	Get all guests
GET	/episodes	❌	Get all episodes
GET	/episodes/<id>	❌	Get episode + appearances
POST	/appearances	✅	Add a new appearance
DELETE	/episodes/<id>	✅	Delete episode and appearances

🧪 Testing with Postman
Import challenge-4-lateshow.postman_collection.json

Test endpoints in order:

Register

Login → copy the token

Add token to headers:
Authorization: Bearer <token>

Test protected routes (POST /appearances, DELETE /episodes/<id>)

💡 Sample Requests
Register
http
Copy
Edit
POST /register
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}
Login
http
Copy
Edit
POST /login
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}
Add Appearance
http
Copy
Edit
POST /appearances
Authorization: Bearer <token>
Content-Type: application/json

{
  "guest_id": 1,
  "episode_id": 1,
  "rating": 5
}
✅ Submission Checklist
 MVC folder structure

 PostgreSQL used

 JWT authentication added

 Protected routes working

 Seed script runs without error

 All routes tested via Postman

 Complete and clean README.md

🔗 GitHub Repository
https://github.com/your-username/late-show-api-challenge

