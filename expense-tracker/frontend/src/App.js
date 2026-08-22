import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import AddExpense from './components/AddExpense';
import ExpenseList from './components/ExpenseList';
import Summary from './components/Summary';

const API_URL = 'http://localhost:8000/api/expenses';

function App() {
  const [expenses, setExpenses] = useState([]);
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(false);

  // Fetch all expenses
  const fetchExpenses = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${API_URL}/`);
      setExpenses(response.data);
    } catch (error) {
      console.error('Error fetching expenses:', error);
      alert('Error fetching expenses');
    } finally {
      setLoading(false);
    }
  };

  // Fetch summary
  const fetchSummary = async () => {
    try {
      const response = await axios.get(`${API_URL}/summary/`);
      setSummary(response.data);
    } catch (error) {
      console.error('Error fetching summary:', error);
    }
  };

  // Initial load
  useEffect(() => {
    fetchExpenses();
    fetchSummary();
  }, []);

  // Add new expense
  const handleAddExpense = async (expenseData) => {
    try {
      await axios.post(`${API_URL}/`, expenseData);
      fetchExpenses();
      fetchSummary();
    } catch (error) {
      console.error('Error adding expense:', error);
      alert('Error adding expense');
    }
  };

  // Delete expense
  const handleDeleteExpense = async (id) => {
    if (window.confirm('Are you sure you want to delete this expense?')) {
      try {
        await axios.delete(`${API_URL}/${id}/`);
        fetchExpenses();
        fetchSummary();
      } catch (error) {
        console.error('Error deleting expense:', error);
        alert('Error deleting expense');
      }
    }
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>💰 Expense Tracker</h1>
      </header>

      <main className="app-main">
        <div className="app-layout">
          <div className="left-section">
            <AddExpense onAddExpense={handleAddExpense} />
          </div>

          <div className="right-section">
            <Summary summary={summary} />
            {loading ? (
              <div className="loading">Loading expenses...</div>
            ) : (
              <ExpenseList expenses={expenses} onDeleteExpense={handleDeleteExpense} />
            )}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
