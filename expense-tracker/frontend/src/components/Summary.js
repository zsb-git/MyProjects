import React from 'react';
import './Summary.css';

function Summary({ summary }) {
  if (!summary) {
    return <div className="summary-container">Loading summary...</div>;
  }

  const categoryEmojis = {
    food: '🍔',
    transport: '🚗',
    entertainment: '🎬',
    utilities: '💡',
    healthcare: '🏥',
    shopping: '🛍️',
    other: '📌',
  };

  return (
    <div className="summary-container">
      <h2>Summary</h2>
      
      <div className="summary-stats">
        <div className="stat-card total">
          <div className="stat-label">Total Expenses</div>
          <div className="stat-value">
            ${summary.total_expenses.toFixed(2)}
          </div>
          <div className="stat-count">{summary.total_count} transactions</div>
        </div>
      </div>

      <div className="categories-section">
        <h3>By Category</h3>
        <div className="categories-list">
          {Object.keys(summary.by_category).length > 0 ? (
            Object.entries(summary.by_category).map(([category, amount]) => (
              <div key={category} className="category-item">
                <span className="category-icon">
                  {categoryEmojis[category] || '📌'}
                </span>
                <span className="category-name">
                  {category.charAt(0).toUpperCase() + category.slice(1)}
                </span>
                <span className="category-amount">
                  ${parseFloat(amount).toFixed(2)}
                </span>
              </div>
            ))
          ) : (
            <p className="no-data">No expenses yet</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default Summary;
