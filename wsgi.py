import sys
import os

# Add the project directory to the sys.path
sys.path.insert(0, '/etc/mywebapp/blog_app')

# Set the environment variable for the Flask app
os.environ['FLASK_APP'] = 'app'

# Import the app variable from your app module
from app import app as application

