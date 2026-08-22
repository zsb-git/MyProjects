import React from 'react';
import './ExpenseList.css';

function ExpenseList({ expenses, onDeleteExpense }) {
  const categoryEmojis = {
    food: '🍔',
    transport: '🚗',
    entertainment: '🎬',
    utilities: '💡',
    healthcare: '🏥',
    shopping: '🛍️',
    other: '📌',
  };

  const formatDate = (dateString) => {
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
  };

  if (expenses.length === 0) {
    return (
      <div className="expense-list-container">
        <h2>Expenses</h2>
        <div className="empty-state">
          <p>No expenses yet. Add one to get started! 💸</p>
        </div>
      </div>
    );
  }

  return (
    <div className="expense-list-container">
      <h2>Expenses</h2>
      <div className="expenses-table">
        <div className="table-header">
          <div className="col-date">Date</div>
          <div className="col-description">Description</div>
          <div className="col-category">Category</div>
          <div className="col-amount">Amount</div>
          <div className="col-action">Action</div>
        </div>
        <div className="table-body">
          {expenses.map((expense) => (
            <div key={expense.id} className="table-row">
              <div className="col-date">{formatDate(expense.date)}</div>
              <div className="col-description">{expense.description}</div>
              <div className="col-category">
                <span className="category-badge">
                  {categoryEmojis[expense.category]} {expense.category}
                </span>
              </div>
              <div className="col-amount">${parseFloat(expense.amount).toFixed(2)}</div>
              <div className="col-action">
                <button
                  className="delete-btn"
                  onClick={() => onDeleteExpense(expense.id)}
                  title="Delete expense"
                >
                  🗑️ Delete
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default ExpenseList;
