
# from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime

# app = Flask(__name__)

# # --- CONFIGURATION ---
# app.config['SECRET_KEY'] = 'dev-key-789'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'

# # --- DATABASE MODELS ---

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)
#     tasks = db.relationship('Task', backref='owner', lazy=True, cascade="all, delete-orphan")

# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(200))
#     status = db.Column(db.String(20), default='Pending') # Default set to Pending
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)

# # Create database on startup
# with app.app_context():
#     db.create_all()

# @login_manager.user_loader
# def load_user(user_id):
#     # Modern SQLAlchemy 2.0 syntax (fixes your LegacyWarning)
#     return db.session.get(User, int(user_id))

# # --- AUTH ROUTES ---

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
        
#         if User.query.filter_by(username=username).first():
#             flash("Username already exists!")
#             return redirect(url_for('signup'))
        
#         new_user = User(username=username, password=generate_password_hash(password))
#         db.session.add(new_user)
#         db.session.commit()
        
#         flash("Registration successful! Please login.")
#         return redirect(url_for('login'))
#     return render_template('signup.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         user = User.query.filter_by(username=request.form.get('username')).first()
#         if user and check_password_hash(user.password, request.form.get('password')):
#             login_user(user)
#             return redirect(url_for('index'))
#         flash("Invalid username or password.")
#     return render_template('login.html')

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))

# # --- TASK API ---

# @app.route('/')
# @login_required
# def index():
#     # Pass counts to template for the initial page load
#     total = len(current_user.tasks)
#     completed = len([t for t in current_user.tasks if t.status == 'Completed'])
#     return render_template('index.html', user=current_user, total=total, completed=completed)

# @app.route('/tasks', methods=['GET'])
# @login_required
# def get_tasks():
#     # Only get tasks for the logged-in user
#     user_tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.created_at.desc()).all()
#     return jsonify([{
#         "id": t.id, 
#         "title": t.title, 
#         "description": t.description, 
#         "status": t.status
#     } for t in user_tasks])

# @app.route('/tasks', methods=['POST'])
# @login_required
# def add_task():
#     data = request.json
#     if not data or not data.get('title'):
#         return jsonify({"error": "Missing title"}), 400
        
#     # FORCE 'Pending' status on creation
#     new_task = Task(
#         title=data['title'], 
#         description=data.get('description', ''),
#         status='Pending',
#         user_id=current_user.id
#     )
#     db.session.add(new_task)
#     db.session.commit()
#     return jsonify({"msg": "added"}), 201

# @app.route('/tasks/<int:id>', methods=['PUT'])
# @login_required
# def update_task(id):
#     # Security: check user_id
#     task = Task.query.filter_by(id=id, user_id=current_user.id).first_or_404()
#     task.status = 'Completed'
#     db.session.commit()
#     return jsonify({"msg": "updated"})

# @app.route('/tasks/<int:id>', methods=['DELETE'])
# @login_required
# def delete_task(id):
#     # Security: check user_id
#     task = Task.query.filter_by(id=id, user_id=current_user.id).first_or_404()
#     db.session.delete(task)
#     db.session.commit()
#     return jsonify({"msg": "deleted"})

# if __name__ == '__main__':
#     app.run(debug=True) 
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)

# --- CONFIGURATION ---
app.config['SECRET_KEY'] = 'dev-key-789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# --- DATABASE MODELS ---

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    tasks = db.relationship('Task', backref='owner', lazy=True, cascade="all, delete-orphan")

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    status = db.Column(db.String(20), default='Pending')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.String(20), nullable=True) # New: Optional Deadline
    
    # Relationship to Subtasks
    subtasks = db.relationship('Subtask', backref='parent', lazy=True, cascade="all, delete-orphan")

class Subtask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    is_done = db.Column(db.Boolean, default=False)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)



# Create database on startup
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# --- AUTH ROUTES ---

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if User.query.filter_by(username=username).first():
            flash("Username already exists!")
            return redirect(url_for('signup'))
        new_user = User(username=username, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form.get('username')).first()
        if user and check_password_hash(user.password, request.form.get('password')):
            login_user(user)
            return redirect(url_for('index'))
        flash("Invalid credentials.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# --- MAIN TASK API ---

@app.route('/')
@login_required
def index():
    total = len(current_user.tasks)
    completed = len([t for t in current_user.tasks if t.status == 'Completed'])
    return render_template('index.html', user=current_user, total=total, completed=completed)

@app.route('/tasks', methods=['GET'])
@login_required
def get_tasks():
    # Sort by created_at descending so newest tasks are on top
    user_tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.created_at.desc()).all()
    return jsonify([{
        "id": t.id, 
        "title": t.title, 
        "description": t.description, 
        "status": t.status,
        "created_at": t.created_at.strftime("%b %d"),
        "end_date": t.end_date,
        "subtasks": [{"id": s.id, "title": s.title, "is_done": s.is_done} for s in t.subtasks]
    } for t in user_tasks])

@app.route('/tasks', methods=['POST'])
@login_required
def add_task():
    data = request.json
    new_task = Task(
        title=data['title'], 
        description=data.get('description', ''),
        end_date=data.get('end_date'),
        user_id=current_user.id
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"msg": "added"}), 201

@app.route('/tasks/<int:id>', methods=['PUT', 'DELETE'])
@login_required
def manage_single_task(id):
    task = Task.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    if request.method == 'PUT':
        task.status = 'Completed'
    else:
        db.session.delete(task)
    db.session.commit()
    return jsonify({"msg": "success"})

# --- SUBTASK API ---

@app.route('/tasks/<int:task_id>/subtasks', methods=['POST'])
@login_required
def add_subtask(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    data = request.json
    new_sub = Subtask(title=data['title'], task_id=task_id)
    db.session.add(new_sub)
    db.session.commit()
    return jsonify({"msg": "sub-added"}), 201

@app.route('/subtasks/<int:sub_id>', methods=['PUT'])
@login_required
def toggle_subtask(sub_id):
    sub = Subtask.query.join(Task).filter(Subtask.id == sub_id, Task.user_id == current_user.id).first_or_404()
    sub.is_done = not sub.is_done
    db.session.commit()
    return jsonify({"msg": "toggled"})

if __name__ == '__main__':
    app.run(debug=True)