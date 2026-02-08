# Task-Manager

**Task Flow** is a full-stack Flask application designed for organized, multi-user task management.  
It features a modern **glassmorphism UI**, **real-time progress tracking**, and a **hierarchical task → subtask structure**.

---

## ✨ Features

- 🔐 **User Authentication:** Secure Signup/Login system with password hashing.
- 🗂️ **Hierarchical Tasks:** Create main tasks with detailed descriptions and nested sub-steps (subtasks).
- 📊 **Progress Tracking:** Dynamic progress bar that updates as you complete tasks.
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
Make sure you have **Python 3.8+** installed.

---

### 2️⃣ Installation

Clone the project or navigate into your project folder:

```bash
cd task_ass 


---

##3️⃣ Setup Virtual Environment (Optional but Recommended)
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on Mac/Linux:
source venv/bin/activate

---

##4️⃣ Install Dependencies
pip install flask flask-sqlalchemy flask-login werkzeug
---
##▶️ Run the Application
python app.py

---

##👤 How It Works

-Signup: Create a new account to access your private dashboard.

-Manage Tasks:

-Enter a Title and Description

-Set an optional Deadline

-Click the "+" button inside a task card to add sub-steps

-Toggle the checkbox to complete subtasks

-Click Done to finish the main task

---

##📂 Project Structure
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

