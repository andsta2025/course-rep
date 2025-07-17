from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required

# Flask app and config
app = Flask(__name__)
app.config.from_pyfile('config.py')

# Database setup
db = SQLAlchemy(app)

# Define models
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    roles = db.relationship('Role', secondary=roles_users, backref='users')

# Flask-Security setup
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security()
security.init_app(app, user_datastore)

# Routes
@app.route('/')
@login_required
def home():
    return render_template('home.html')

# App run
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Create a user if not exists
        if not User.query.filter_by(email='admin@example.com').first():
            user_datastore.create_user(
                email='admin@example.com',
                password='password123'  # plaintext just for demo
            )
            db.session.commit()

    app.run(debug=True)