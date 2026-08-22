README: Expense Tracker Backend

## Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL installed and running

### Install Dependencies
1. Create a virtual environment:
   python -m venv venv
   
2. Activate virtual environment:
   - Windows: venv\Scripts\activate
   - Mac/Linux: source venv/bin/activate

3. Install packages:
   pip install -r requirements.txt

### Database Setup
1. Create a PostgreSQL database:
   - Open pgAdmin or psql
   - CREATE DATABASE expense_tracker_db;

2. Run migrations:
   python manage.py migrate

### Run Server
python manage.py runserver

The server will run on http://localhost:8000

### API Endpoints
- GET/POST /api/expenses/ - List all expenses / Create new expense
- GET/PUT/DELETE /api/expenses/{id}/ - Get, update, delete expense
- GET /api/expenses/summary/ - Get expense summary
- GET /api/expenses/today/ - Get today's expenses
- GET /api/expenses/this_month/ - Get this month's expenses
