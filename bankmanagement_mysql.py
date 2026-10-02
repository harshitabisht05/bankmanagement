import mysql.connector

try:
    myconnection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "NewPassword123"
    )

    if myconnection.is_connected():
        print("Connected Successfully!!")

except mysql.connector.Error as e:
    print("Error: ", e)

mycur = myconnection.cursor()

mycur.execute("Create DataBase if not exists Bank_Management")
print("Database created!!")

mycur.execute("Use Bank_Management")

mycur.execute("""
CREATE TABLE IF NOT EXISTS Customers(
    customer_id INT AUTO_INCREMENT PRIMARY KEY ,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(15),
    address VARCHAR(100)
)
""")

mycur.execute("""
CREATE TABLE IF NOT EXISTS Accounts(
    account_no BIGINT PRIMARY KEY,
    customer_id INT ,
    account_type VARCHAR(20),
    balance DECIMAL(10,2),
    FOREIGN KEY(customer_id)
    REFERENCES Customers(customer_id)
)
""")

mycur.execute("""
CREATE TABLE IF NOT EXISTS BankTransactions(
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_no BIGINT,
    transaction_type VARCHAR(20),
    amount DECIMAL(10,2),
    transaction_date DATETIME,
    FOREIGN KEY(account_no)
    REFERENCES Accounts(account_no)
)
""")

print("Tables Created Successfully")

# mycur.execute("SHOW TABLES")
# print("Tables in BankDB:")
# for table in mycur.fetchall():
#     print(table[0])

# #inseted data
# mycur.execute("""
# INSERT INTO Customers (first_name, last_name, phone, address)
# VALUES
# ('John', 'Smith', '1234567890', 'New York'),
# ('Emma', 'Johnson', '2345678901', 'Chicago'),
# ('Michael', 'Brown', '3456789012', 'Los Angeles')
# """)

# mycur.execute("""
# INSERT INTO Accounts (account_no, customer_id, account_type, balance)
# VALUES
# (10001, 1, 'Savings', 5000.00),
# (10002, 2, 'Current', 12000.00),
# (10003, 3, 'Savings', 8000.00)
# """)

# mycur.execute("""
# INSERT INTO BankTransactions
# (account_no, transaction_type, amount, transaction_date)
# VALUES
# (10001, 'Deposit', 5000.00, NOW()),
# (10002, 'Deposit', 12000.00, NOW()),
# (10003, 'Deposit', 8000.00, NOW())
# """)

# myconnection.commit()

print("Sample Data Inserted Successfully")


# verify the data inside tabel
# mycur.execute("Select * from customers")

# print("Customers Tables: ")
# for row in mycur.fetchall():
#     print(row)


# mycur.execute("Select * from Accounts")

# print("Account Tables: ")
# for row in mycur.fetchall():
#     print(row)

# mycur.execute("Select * from BankTransactions")

# print("BankTransactions Tables: ")
# for row in mycur.fetchall():
#     print(row)


def create_account():
    print("<--------------Creating Account--------------->")

    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    phone = input("Phone Number: ")
    address = input("Address: ")

    account_number = int(input("Account number: "))
    account_type = input("Account type(Savings, Current): ")

    balance = float(input("Opening Balance: "))

    sql = """Select account_no from accounts where account_no = %s"""

    mycur.execute(sql,(account_number,))

    result = mycur.fetchone()

    if result is not None:
        print("Account Already exists")
        return

    sql = """insert into customers (first_name, last_name, phone, address) values(%s, %s,%s,%s)"""

    values = (
        first_name, last_name, phone, address
    )
    mycur.execute(sql, values)

    customer_id = mycur.lastrowid


    sql = """insert into accounts (account_no, account_type, balance) values(%s, %s,%s)"""
    
    values = (
            account_number, account_type, balance
        )
    mycur.execute(sql, values)

    if balance > 0:
        sql = """insert into banktransactions (account_no, transaction_type,amount) values (%s,%s,%s)"""

        values = (account_number, "Deposit", balance)

        mycur.execute(sql, values)

    myconnection.commit()

    print("\nAccount created successfully!")
    print("Customer ID:", customer_id)
    print("Account Number:", account_number)
    print("Thank you for the visit!!")

    
def display_account():

    account_number = int(input("Enter your Account number: "))

    sql = """Select 
    c.customer_id, 
    c.first_name, 
    c.last_name, 
    c.phone, 
    c.address, 
    a.account_no, 
    a.account_type, 
    a.balance

    from customers c inner join accounts a 
    on c.customer_id = a.customer_id
    where account_no = %s
    """

    mycur.execute(sql, (account_number,))

    result = mycur.fetchone()

    if result is None:
        print("No account found!")
        return

    print("<----------------Account details----------------->")
    print("Customer ID: " , result[0])
    print("Name: ", result[1], result[2])
    print("Phone: ", result[3])
    print("Address: ", result[4])
    print("Account Number: ", result[5])
    print("Account Type: ", result[6])
    print("Balance: ", result[7])
    print("---------------------------------------------------")
    print("Thank you for the visit!!")


def deposit_money():

    account_number = int(input("Enter your Account number: "))

    sql = """select balance from accounts where account_no = %s"""

    mycur.execute(sql, (account_number,))
    
    result = mycur.fetchone()
    
    if result is None:
        print("No account found!")
        return

    current_balance = result[0]

    print("Your current Balance: ", current_balance)

    moneytodeposit = int(input("Enter Amount you want to deposit: "))

    if moneytodeposit <= 0:
        print("Money should be greater than 0.")
        return

    sql = """Update accounts
    set balance = balance+  %s
    where account_no = %s
    """
    mycur.execute(sql, (moneytodeposit, account_number))

    sql = """insert into banktransactions (account_no, transaction_type, amount) values (%s, %s, %s) """

    mycur.execute(sql, (account_number, "Deposit", moneytodeposit))

    myconnection.commit()

    print("Money Deposited!!\n")
    print("New Balance: ", current_balance + moneytodeposit)
    print("Thank you for the visit!!")


def withdraw_money():

    account_number = int(input("Enter your account number: "))

    sql = """Select balance from accounts where account_no = %s"""
    mycur.execute(sql,(account_number,))

    result = mycur.fetchone()
    if result is None: 
        print("No Account Found!!")
        return

    current_balance = result[0]
    print("Your Current balance is: ", current_balance)

    withdraw_money = int(input("Enter the Amount you want to Withdraw: "))

    if withdraw_money > current_balance:
        print("Insufficient Balance!!")
        return
    if withdraw_money <= 0:
        print("Enter amount greater than 0.")
        return

    sql = """Update accounts
            set balance = balance - %s
            where account_no = %s
    """

    mycur.execute(sql, (withdraw_money, account_number))

    sql = """Insert into banktransactions(account_no, transaction_type,amount) values (%s,%s,%s)"""

    mycur.execute(sql,(account_number, "Withdrawal", withdraw_money))

    myconnection.commit()

    print("Account withdraw!!\n")
    print("New Balance: ", current_balance - withdraw_money)
    print("Thank you for the visit!!")



def start_bank():
    print("\nWelcome to Your Digital Bank!\n")

    print("1. Open a new Bank Account")
    print("2. View your Bank details")
    print("3. Make a Deposit")
    print("4. Make a Withdrawal\n")

    option = int(input("Enter a Number between(1-4) to choose an option: "))

    if option > 4:
        print("Enter Number between 1-4")
        return
    if option < 0:
        print("Enter Number between 1-4")
        return

    if option == 1:
        create_account()
        return
    elif option == 2:
       display_account()
       return

    elif option == 3:
        deposit_money()
        return
    
    elif option == 4:
        withdraw_money()
        return

start_bank()
