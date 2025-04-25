# Penguin-Backend

A Django REST Framework backend for a game application that manages users and scores. The API provides endpoints for user management, score tracking, and a global scoreboard.
## Table of Contents
- Overview
- Features
- Installation
- API Endpoints
- Database Schema
- Usage Examples
## Overview
This project provides a backend API for a game application, allowing users to register, login, and track their game scores. The API supports keeping track of each user's last game score and their all-time high score, as well as providing a global leaderboard.
## Features
- User management (registration, profile updates)
- Score tracking for each user (high score and last game score)
- Global scoreboard sorted by high scores
- API documentation with Swagger UI
- Secure password storage with hashing
## Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd Game_backend
```
2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install django djangorestframework drf-yasg
```
4. Run migrations:
```bash
python manage.py migrate
```
5. Start the development server:
```bash
python manage.py runserver
```
The API will be available at http://127.0.0.1:8000/api/
## API Endpoints
### Documentation
- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`
### User Endpoints
- `GET /api/users/` - List all users
- `POST /api/users/` - Create a new user
- `GET /api/users/{id}/` - Retrieve user details
- `PUT /api/users/{id}/` - Update user details
- `DELETE /api/users/{id}/` - Delete a user
### Score Endpoints
- `GET /api/score/` - Get the global scoreboard (sorted by high score)
- `POST /api/score/` - Submit a new score for a user
- `GET /api/score/{username}/` - Get score for a specific user
## Database Schema
### User Model
- `id`: Auto-incremented ID
- `name`: User's full name
- `username`: Unique username
- `password`: Hashed password
- `created_at`: Timestamp of user creation
- `updated_at`: Timestamp of last update
### Score Model
- `user`: OneToOne relationship with User (primary key)
- `high_score`: User's highest score
- `last_game_score`: User's most recent score
- `created_at`: Timestamp of score creation
- `updated_at`: Timestamp of last update
## Usage Examples
### Creating a new user
```json
POST /api/users/
{
  "name": "John Doe",
  "username": "johndoe",
  "password": "securepassword"
}
```
### Submitting a score
```json
POST /api/score/
{
  "user": 1,
  "last_game_score": 500
}
```
### Retrieving the leaderboard
```
GET /api/score/
```
Response:
```json
[
  {
    "username": "topplayer",
    "high_score": 1000
  },
  {
    "username": "johndoe",
    "high_score": 500
  }
]
```