import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import logo from './octofitapp-small.png';
import './App.css';

function App() {
  const [apiData, setApiData] = useState(null);
  const apiUrl = process.env.REACT_APP_CODESPACE_NAME 
    ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev`
    : 'http://localhost:8000';

  useEffect(() => {
    fetch(`${apiUrl}/api/`)
      .then(response => response.json())
      .then(data => setApiData(data))
      .catch(error => console.error('Error fetching API:', error));
  }, [apiUrl]);

  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container">
            <Link className="navbar-brand" to="/">
              <img src={logo} alt="OctoFit Tracker" height="40" className="me-2" />
              OctoFit Tracker
            </Link>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <Link className="nav-link" to="/">Home</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Workouts</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<Home logo={logo} apiUrl={apiUrl} apiData={apiData} />} />
          <Route path="/users" element={<Users apiUrl={apiUrl} />} />
          <Route path="/teams" element={<Teams apiUrl={apiUrl} />} />
          <Route path="/activities" element={<Activities apiUrl={apiUrl} />} />
          <Route path="/leaderboard" element={<Leaderboard apiUrl={apiUrl} />} />
          <Route path="/workouts" element={<Workouts apiUrl={apiUrl} />} />
        </Routes>

        <footer className="bg-dark text-white text-center py-3 mt-5">
          <p>&copy; 2026 OctoFit Tracker - Build Applications with GitHub Copilot</p>
        </footer>
      </div>
    </Router>
  );
}

function Home({ logo, apiUrl, apiData }) {
  return (
    <div className="container mt-5">
      <div className="text-center">
        <img src={logo} alt="OctoFit Tracker" className="img-fluid mb-4" style={{maxWidth: '300px'}} />
        <h1>Welcome to OctoFit Tracker</h1>
        <p className="lead">A fitness tracking app for Mergington High School</p>
        <div className="row mt-5">
          <div className="col-md-6">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">Features</h5>
                <ul className="list-group list-group-flush">
                  <li className="list-group-item">User profiles and authentication</li>
                  <li className="list-group-item">Activity logging and tracking</li>
                  <li className="list-group-item">Team creation and management</li>
                  <li className="list-group-item">Competitive leaderboard</li>
                  <li className="list-group-item">Personalized workout suggestions</li>
                </ul>
              </div>
            </div>
          </div>
          <div className="col-md-6">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">API Status</h5>
                {apiData ? (
                  <div className="alert alert-success">
                    <strong>✓ API Connected!</strong>
                    <p className="mb-0 mt-2">Available endpoints:</p>
                    <ul className="mb-0">
                      {Object.keys(apiData).map(key => (
                        <li key={key}>{key}</li>
                      ))}
                    </ul>
                  </div>
                ) : (
                  <div className="alert alert-warning">
                    <strong>⚠ Connecting to API...</strong>
                    <p className="mb-0">API URL: {apiUrl}</p>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function Users({ apiUrl }) {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch(`${apiUrl}/api/users/`)
      .then(response => response.json())
      .then(data => setUsers(data))
      .catch(error => console.error('Error fetching users:', error));
  }, [apiUrl]);

  return (
    <div className="container mt-5">
      <h2>Users</h2>
      <div className="row">
        {users.map(user => (
          <div key={user.id} className="col-md-4 mb-3">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{user.name}</h5>
                <p className="card-text">
                  <strong>Email:</strong> {user.email}<br />
                  <strong>Fitness Level:</strong> {user.fitness_level}<br />
                  <strong>Team ID:</strong> {user.team_id}
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function Teams({ apiUrl }) {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch(`${apiUrl}/api/teams/`)
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.error('Error fetching teams:', error));
  }, [apiUrl]);

  return (
    <div className="container mt-5">
      <h2>Teams</h2>
      <div className="row">
        {teams.map(team => (
          <div key={team.id} className="col-md-6 mb-3">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{team.name}</h5>
                <p className="card-text">{team.description}</p>
                <small className="text-muted">Created: {new Date(team.created_at).toLocaleDateString()}</small>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function Activities({ apiUrl }) {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch(`${apiUrl}/api/activities/`)
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, [apiUrl]);

  return (
    <div className="container mt-5">
      <h2>Activities</h2>
      <div className="table-responsive">
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Type</th>
              <th>Duration (min)</th>
              <th>Distance (km)</th>
              <th>Calories</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody>
            {activities.map(activity => (
              <tr key={activity.id}>
                <td>{activity.activity_type}</td>
                <td>{activity.duration_minutes}</td>
                <td>{activity.distance_km || 'N/A'}</td>
                <td>{activity.calories_burned}</td>
                <td>{new Date(activity.date).toLocaleDateString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function Leaderboard({ apiUrl }) {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch(`${apiUrl}/api/leaderboard/`)
      .then(response => response.json())
      .then(data => setLeaderboard(data.sort((a, b) => a.rank - b.rank)))
      .catch(error => console.error('Error fetching leaderboard:', error));
  }, [apiUrl]);

  return (
    <div className="container mt-5">
      <h2>Leaderboard</h2>
      <div className="table-responsive">
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Rank</th>
              <th>User ID</th>
              <th>Team ID</th>
              <th>Total Points</th>
              <th>Total Activities</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.map(entry => (
              <tr key={entry.id}>
                <td>
                  <span className={`badge ${entry.rank === 1 ? 'bg-warning' : entry.rank === 2 ? 'bg-secondary' : entry.rank === 3 ? 'bg-info' : 'bg-light text-dark'}`}>
                    {entry.rank}
                  </span>
                </td>
                <td>{entry.user_id}</td>
                <td>{entry.team_id}</td>
                <td><strong>{entry.total_points}</strong></td>
                <td>{entry.total_activities}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function Workouts({ apiUrl }) {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch(`${apiUrl}/api/workouts/`)
      .then(response => response.json())
      .then(data => setWorkouts(data))
      .catch(error => console.error('Error fetching workouts:', error));
  }, [apiUrl]);

  return (
    <div className="container mt-5">
      <h2>Workout Suggestions</h2>
      <div className="row">
        {workouts.map(workout => (
          <div key={workout.id} className="col-md-6 mb-3">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{workout.name}</h5>
                <p className="card-text">{workout.description}</p>
                <div className="mb-2">
                  <span className="badge bg-primary me-2">{workout.category}</span>
                  <span className="badge bg-danger me-2">{workout.difficulty}</span>
                  <span className="badge bg-success">{workout.duration_minutes} min</span>
                </div>
                <h6>Exercises:</h6>
                <ul className="list-unstyled">
                  {workout.exercises && workout.exercises.map((exercise, idx) => (
                    <li key={idx}>
                      • {exercise.name} 
                      {exercise.reps && ` - ${exercise.reps} reps`}
                      {exercise.sets && ` x ${exercise.sets} sets`}
                      {exercise.duration && ` - ${exercise.duration}`}
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
