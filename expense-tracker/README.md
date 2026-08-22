# Expense Tracker Application

A full-stack expense tracking application built with **React** (frontend) and **Django** (backend) with **PostgreSQL** database.

## Features

✅ **Add Expenses** - Record expenses with description, amount, category, and date
✅ **View Expenses** - See all expenses in a clean, organized table
✅ **Delete Expenses** - Remove unwanted expense entries
✅ **Expense Summary** - View total expenses and breakdown by category
✅ **Responsive Design** - Works seamlessly on desktop and mobile devices

## Project Structure

```
expense-tracker/
├── backend/                 # Django REST API
│   ├── expense_project/    # Main Django project
│   ├── expenses/           # Expenses app
│   ├── manage.py
│   ├── requirements.txt
│   └── README.md
│
└── frontend/               # React application
    ├── src/
    │   ├── components/
    │   ├── App.js
    │   └── index.js
    ├── public/
    ├── package.json
    └── README.md
```

## Setup & Installation

### Step 1: Install PostgreSQL

1. Download and install PostgreSQL from [postgresql.org](https://www.postgresql.org/download/)
2. Make sure PostgreSQL service is running
3. Create the database:
   ```sql
   CREATE DATABASE expense_tracker_db;
   ```

### Step 2: Setup Backend

1. Navigate to the backend folder:
   ```bash
   cd backend
   ```

2. Create a Python virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate virtual environment:
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser (optional, for admin panel):
   ```bash
   python manage.py createsuperuser
   ```

7. Start the backend server:
   ```bash
   python manage.py runserver
   ```
   Server will run on `http://localhost:8000`

### Step 3: Setup Frontend

1. In a new terminal, navigate to the frontend folder:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```
   App will open on `http://localhost:3000`

## API Endpoints

### Expense Management
- `GET /api/expenses/` - Get all expenses
- `POST /api/expenses/` - Create new expense
- `GET /api/expenses/{id}/` - Get specific expense
- `PUT /api/expenses/{id}/` - Update expense
- `DELETE /api/expenses/{id}/` - Delete expense

### Statistics
- `GET /api/expenses/summary/` - Get expense summary with totals by category
- `GET /api/expenses/today/` - Get today's expenses
- `GET /api/expenses/this_month/` - Get this month's expenses

## Database Schema

### Expense Model
```python
- id: Integer (Primary Key)
- description: String (max 255 chars)
- amount: Decimal (10 digits, 2 decimal places)
- category: Choice field (Food, Transport, Entertainment, Utilities, Healthcare, Shopping, Other)
- date: Date
- created_at: DateTime (auto-populated)
- updated_at: DateTime (auto-updated)
```

## Technologies Used

### Frontend
- **React 18** - UI framework
- **Axios** - HTTP client for API calls
- **CSS3** - Styling

### Backend
- **Django 4.2** - Web framework
- **Django REST Framework** - API development
- **Django CORS Headers** - Cross-Origin Resource Sharing

### Database
- **PostgreSQL** - Relational database

## Troubleshooting

### Backend Issues
- **Database connection error**: Make sure PostgreSQL is running and database exists
- **Module not found**: Ensure virtual environment is activated and dependencies installed
- **Port 8000 already in use**: Change port with `python manage.py runserver 8001`

### Frontend Issues
- **Cannot connect to backend**: Check if backend is running on `http://localhost:8000`
- **Port 3000 already in use**: React will prompt to use a different port
- **npm install errors**: Delete `node_modules` and `package-lock.json`, then reinstall

## Future Enhancements

- User authentication and multiple user support
- Expense budgeting and alerts
- Charts and visualizations
- Data export (CSV, PDF)
- Recurring expenses
- Receipt upload and storage

## License

This project is open source and available under the MIT License.
