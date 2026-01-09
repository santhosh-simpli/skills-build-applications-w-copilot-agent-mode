from djongo import models


class User(models.Model):
    _id = models.ObjectIdField(db_column='_id')
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    fitness_level = models.CharField(max_length=50)
    team_id = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
        
    def __str__(self):
        return self.name


class Team(models.Model):
    _id = models.ObjectIdField(db_column='_id')
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'teams'
        
    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField(db_column='_id')
    user_id = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    calories_burned = models.IntegerField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'
        
    def __str__(self):
        return f"{self.activity_type} - {self.duration_minutes} minutes"


class Leaderboard(models.Model):
    _id = models.ObjectIdField(db_column='_id')
    user_id = models.CharField(max_length=100)
    team_id = models.CharField(max_length=100)
    total_points = models.IntegerField()
    total_activities = models.IntegerField()
    rank = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'
        
    def __str__(self):
        return f"Rank {self.rank} - {self.total_points} points"


class Workout(models.Model):
    _id = models.ObjectIdField(db_column='_id')
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    duration_minutes = models.IntegerField()
    exercises = models.JSONField()

    class Meta:
        db_table = 'workouts'
        
    def __str__(self):
        return self.name
