# Quick Start Guide

## 🚀 Get the Application Running in 10 Minutes

### Prerequisites Checklist
- [ ] PostgreSQL installed and running
- [ ] Python 3.8+ installed
- [ ] Node.js 14+ and npm installed

### Terminal 1: Start Backend

```bash
# Navigate to backend
cd expense-tracker/backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create database (in PostgreSQL)
# Run: CREATE DATABASE expense_tracker_db;

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
# Server runs on http://localhost:8000
```

### Terminal 2: Start Frontend

```bash
# Navigate to frontend
cd expense-tracker/frontend

# Install dependencies
npm install

# Start development server
npm start
# App opens on http://localhost:3000
```

### ✅ Done!

Now you can:
1. Open http://localhost:3000 in your browser
2. Add, view, and delete expenses
3. See expense summaries by category

## 📝 What You Can Do

### Add Expense
- Fill in description, amount, category, and date
- Click "+ Add Expense" button

### View Expenses
- See all expenses in the table on the right
- Expenses are sorted by most recent first

### Delete Expense
- Click the "🗑️ Delete" button on any expense
- Confirm deletion when prompted

### See Summary
- View total expenses at the top
- See breakdown by category below

## 🔧 Troubleshooting

**Backend won't start:**
- Check if PostgreSQL is running
- Run: `CREATE DATABASE expense_tracker_db;` in PostgreSQL

**Frontend shows "Cannot connect to server":**
- Make sure backend is running on http://localhost:8000
- Check CORS settings in backend/expense_project/settings.py

**npm install fails:**
- Delete `node_modules` folder and `package-lock.json`
- Run `npm install` again

**Port already in use:**
- Backend: `python manage.py runserver 8001`
- Frontend: Will ask if you want to use a different port

## 📚 More Information

- Backend README: `backend/README.md`
- Frontend README: `frontend/README.md`
- Main README: `README.md`
