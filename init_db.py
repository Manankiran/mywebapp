from app import app
from models import db, User, BlogPost
from flask_bcrypt import generate_password_hash

with app.app_context():
    db.create_all()

    # Create an admin user
    hashed_password = generate_password_hash('admin_password').decode('utf-8')
    admin = User(username='admin', password=hashed_password)
    db.session.add(admin)
    db.session.commit()

