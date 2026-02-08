#  Task Management Application

Task Manager is a full-stack Flask application designed for organized, multi-user task management. It features a modern, "glassmorphism" UI, real-time progress tracking, and a hierarchical task-subtask structure.
---

## ✨ Features

- 🔐 **User Authentication:** Secure Signup/Login system with password hashing.
- 🗂️ **Hierarchical Tasks:** Create main tasks with detailed descriptions and nested sub-steps (subtasks).
- 📊 **Progress Tracking:** Dynamic progress bar that updates as tasks are completed.
- 🔃 **Smart Sorting:** Automatic sorting by creation date (newest first).
- 📅 **Deadline Management:** Optional end dates for time-sensitive goals.
- ⚡ **Real-time Interaction:** AJAX-powered updates (add/delete/toggle) without page reloads.
- 📱 **Responsive Design:** Fully centered and mobile-friendly UI using *Plus Jakarta Sans*.

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask)
- **Database:** SQLite (SQLAlchemy ORM)
- **Frontend:** HTML5, CSS3 (Flexbox/Grid), Vanilla JavaScript
- **Authentication:** Flask-Login
- **Fonts:** Google Fonts (Plus Jakarta Sans)

---

## 🚀 Getting Started

### 1️⃣ Prerequisites
Ensure you have **Python 3.8+** installed.

---

### 2️⃣ Installation
Navigate to your project folder:

```bash
cd task_ass
```

---

### 3️⃣ Setup Virtual Environment (Optional but Recommended)

```bash
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on Mac/Linux:
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install flask flask-sqlalchemy flask-login werkzeug
```

---

### 5️⃣ Initialize the Database (Fresh Start)

Since this project includes **Subtasks + End Dates**, it is recommended to delete the old database if it exists:

**Mac/Linux**
```bash
rm tasks.db
```

**Windows**
```bash
del tasks.db
```

The database will be automatically created when you run the application.

---

## ▶️ Run the Application

```bash
python app.py
```

Now open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 👤 How It Works

- **Signup:** Create a new account to access your private dashboard.
- **Manage Tasks:**
  - Enter a **Title** and **Description**
  - Set an optional **Deadline**
  - Click the **"+" button** inside a task card to add sub-steps
  - Toggle the checkbox to complete subtasks
  - Click **Done** to finish the main task

---

## 📂 Project Structure

```plaintext
task_ass/
├── app.py              # Flask server & API routes
├── tasks.db            # SQLite database (auto-generated)
├── static/
│   ├── style.css       # Custom CSS & Animations
│   └── script.js       # Frontend logic & API calls
└── templates/
    ├── login.html      # Authentication UI
    ├── signup.html     # Registration UI
    └── index.html      # Main Dashboard
```

---

## 📜 License

This project is open-source and free to use for learning and development.
