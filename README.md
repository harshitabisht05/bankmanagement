# Bank Management System

A beginner-friendly **Bank Management System** built with **Python** and **MySQL**. The project demonstrates how a Python application can connect to MySQL, create a relational database, manage customer and account records, and perform basic banking operations.

## Features

- Create a new bank account
- Store customer details
- View account details
- Deposit money
- Withdraw money
- Check account balance
- Record deposits and withdrawals in a transaction table
- Automatically create the required database and tables

## Tech Stack

- **Python 3**
- **MySQL 8.0+**
- **mysql-connector-python**

## Project Structure

```text
bankmanagement/
├── bankmanagement_mysql.py   # Main Python program
└── README.md                 # Project documentation
```

## Database Design

The application creates a database named `Bank_Management`.

It uses three tables:

### 1. Customers

Stores personal information about bank customers.

| Column | Description |
|---|---|
| `customer_id` | Primary key, auto-incremented |
| `first_name` | Customer first name |
| `last_name` | Customer last name |
| `phone` | Customer phone number |
| `address` | Customer address |

### 2. Accounts

Stores bank account information.

| Column | Description |
|---|---|
| `account_no` | Primary key for the account |
| `customer_id` | Links the account to a customer |
| `account_type` | Savings or Current |
| `balance` | Current account balance |

### 3. BankTransactions

Stores deposit and withdrawal records.

| Column | Description |
|---|---|
| `transaction_id` | Primary key, auto-incremented |
| `account_no` | Links the transaction to an account |
| `transaction_type` | Deposit or Withdrawal |
| `amount` | Transaction amount |
| `transaction_date` | Date and time of transaction |

### Relationship

```text
Customers
    |
    | customer_id
    v
Accounts
    |
    | account_no
    v
BankTransactions
```

## Requirements

Make sure you have:

1. Python 3 installed
2. MySQL Server installed and running
3. A MySQL user such as `root`
4. Permission to create a database and tables

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/harshitabisht05/bankmanagement.git
cd bankmanagement
```

### 2. Install the MySQL connector

```bash
pip install mysql-connector-python
```

### 3. Configure MySQL credentials

Open:

```text
bankmanagement_mysql.py
```

Find the connection section:

```python
myconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yourpassword"
)
```

Replace `Yourpassword` with your actual MySQL password.

For example:

```python
myconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123"
)
```

> **Important:** Do not commit your real database password to a public GitHub repository. For a production project, use environment variables instead.

## Run the Project

From the project directory:

```bash
python bankmanagement_mysql.py
```

The program connects to MySQL and creates the `Bank_Management` database and required tables automatically if they do not already exist.

You will then see a menu similar to:

```text
Welcome to Your Digital Bank!

1. Open a new Bank Account
2. View your Bank details
3. Make a Deposit
4. Make a Withdrawal

Enter a Number between(1-4) to choose an option:
```

## Example Workflow

### Create an account

Select:

```text
1
```

Enter the customer's information and opening balance.

The application:

1. Inserts the customer into `Customers`
2. Gets the generated `customer_id`
3. Creates the account in `Accounts`
4. Records the opening deposit in `BankTransactions`
5. Commits the changes to MySQL

### Display account details

Select:

```text
2
```

Enter the account number. The program uses an SQL `INNER JOIN` to combine customer and account information.

### Deposit money

Select:

```text
3
```

The application checks that the account exists, increases the balance, records the deposit transaction, and commits the changes.

### Withdraw money

Select:

```text
4
```

The application checks the account balance before allowing the withdrawal. It prevents withdrawals when the requested amount is greater than the available balance.

## Important Python/MySQL Concepts Demonstrated

This project is useful for learning:

- Python functions
- User input and menu-driven programs
- MySQL database connections
- SQL `CREATE DATABASE`
- SQL `CREATE TABLE`
- `INSERT`, `SELECT`, and `UPDATE`
- Primary keys
- Foreign keys
- Table relationships
- SQL `INNER JOIN`
- Parameterized SQL queries using `%s`
- `fetchone()`
- Transactions and `commit()`
- Basic validation and error handling

## Current Limitations

This is a learning project rather than a production banking system.

Some things that could be improved:

- Use environment variables for database credentials
- Add stronger input validation
- Add a continuous menu loop instead of exiting after one operation
- Add account deletion/closure
- Add transaction history display
- Add authentication/login
- Add database transaction rollback handling
- Use `Decimal` consistently for monetary values
- Add automated tests
- Improve error handling and user experience

## Learning Goal

The main purpose of this project is to understand how **Python applications interact with relational databases** and how related data can be modeled using tables, primary keys, foreign keys, and SQL queries.

## Author

**Harshita Bisht**

GitHub: [harshitabisht05](https://github.com/harshitabisht05)

## Repository

[Bank Management System](https://github.com/harshitabisht05/bankmanagement)
