# OctoFit Tracker - Fitness App

A full-stack fitness tracking application built with Django REST Framework, MongoDB, and React.

## 📋 Features

- **User Management**: Track superhero fitness enthusiasts (Team Marvel & Team DC!)
- **Activity Logging**: Record workouts and track progress
- **Team Competition**: Team-based fitness challenges
- **Leaderboard**: Competitive rankings based on points and activities
- **Workout Suggestions**: Personalized workout recommendations

## 🛠 Technology Stack

### Backend
- **Django 4.1.7** - Python web framework
- **Django REST Framework 3.14.0** - REST API
- **Djongo 1.3.6** - MongoDB connector for Django
- **MongoDB 6.0** - NoSQL database (running in Docker)
- **CORS Headers** - Cross-origin resource sharing

### Frontend
- **React 18** - JavaScript UI library
- **React Router DOM** - Navigation
- **Bootstrap 5** - CSS framework

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Node.js 14+
- Docker (for MongoDB)

### Installation

1. **Start MongoDB**:
```bash
docker run -d --name mongodb -p 27017:27017 mongo:6.0
```

2. **Backend Setup**:
```bash
# Create and activate virtual environment
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate

# Install dependencies
pip install -r octofit-tracker/backend/requirements.txt

# Run migrations
python octofit-tracker/backend/manage.py migrate

# Populate database with superhero test data
python octofit-tracker/backend/manage.py populate_db

# Start Django server
python octofit-tracker/backend/manage.py runserver 0.0.0.0:8000
```

3. **Frontend Setup** (in a new terminal):
```bash
# Navigate to frontend directory
cd octofit-tracker/frontend

# Install dependencies
npm install

# Start React development server
npm start
```

4. **Access the Application**:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/api/

## 📊 API Endpoints

- `GET /api/` - API root with all available endpoints
- `GET /api/users/` - List all users
- `GET /api/teams/` - List all teams
- `GET /api/activities/` - List all activities
- `GET /api/leaderboard/` - View leaderboard
- `GET /api/workouts/` - Get workout suggestions

## 🦸 Test Data

The application comes with pre-populated superhero test data:

### Team Marvel
- Tony Stark (Iron Man)
- Steve Rogers (Captain America)
- Natasha Romanoff (Black Widow)
- Thor Odinson

### Team DC
- Bruce Wayne (Batman)
- Clark Kent (Superman)
- Diana Prince (Wonder Woman)
- Barry Allen (The Flash)

## 🎯 Database Collections

- **users** - User profiles and fitness levels
- **teams** - Team information
- **activities** - Logged workouts and activities
- **leaderboard** - Competitive rankings
- **workouts** - Workout suggestions and exercises

## 🔧 Development

### Running Tests
```bash
# Backend tests
python octofit-tracker/backend/manage.py test

# Frontend tests
cd octofit-tracker/frontend
npm test
```

### Database Management
```bash
# Access MongoDB shell
docker exec -it mongodb mongosh

# View collections
use octofit_db
show collections
db.users.find().pretty()
```

## 📝 Built With GitHub Copilot

This application was built as part of the "Build Applications with GitHub Copilot Agent Mode" exercise, demonstrating:
- Rapid prototyping with AI assistance
- Full-stack development
- REST API design
- React component development
- MongoDB integration with Django

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

- Built for Mergington High School Physical Education Department
- Inspired by Paul Octo's vision for student fitness tracking
- Powered by GitHub Copilot Agent Mode
