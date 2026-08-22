README: Expense Tracker Frontend

## Setup Instructions

### Prerequisites
- Node.js 14+ and npm
- Backend server running on http://localhost:8000

### Install Dependencies
npm install

### Run Development Server
npm start

The app will open on http://localhost:3000

### Build for Production
npm build

### Features
- ✅ Add new expenses with description, amount, category, and date
- ✅ View all expenses in a clean table format
- ✅ Delete expenses with confirmation
- ✅ See expense summary and breakdown by category
- ✅ Responsive design that works on mobile and desktop

### Project Structure
- src/
  - components/
    - AddExpense.js - Form to add new expenses
    - ExpenseList.js - Display list of expenses
    - Summary.js - Show expense summary
  - App.js - Main component
  - index.js - Entry point
