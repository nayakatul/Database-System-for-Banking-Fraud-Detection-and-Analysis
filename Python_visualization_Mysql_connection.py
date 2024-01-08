
import mysql.connector
from mysql.connector import Error
import pandas as pd
import matplotlib.pyplot as plt

# Establish a database connection
try:
    connection = mysql.connector.connect(
        host='localhost',
        database='Fraud_Detection_System',
        user='root',
        password='Aeiou1999.',
        auth_plugin='mysql_native_password'
    )

    # SQL query to fetch the total transaction amount per day
    total_amount_per_day_query = """
    SELECT Date, SUM(Amount) as TotalAmount
    FROM Transaction
    GROUP BY Date
    ORDER BY Date;
    """
    total_amount_per_day_df = pd.read_sql(total_amount_per_day_query, connection)

    # SQL query to fetch the count of transactions per type
    transaction_count_per_type_query = """
    SELECT TransactionType, COUNT(*) as TransactionCount
    FROM Transaction
    GROUP BY TransactionType
    ORDER BY TransactionCount DESC;
    """
    transaction_count_per_type_df = pd.read_sql(transaction_count_per_type_query, connection)

    # Query for total transaction amount by customer
    amount_by_customer_query = """
    SELECT c.Name, SUM(t.Amount) as TotalAmount
    FROM Customer c
    JOIN Account a ON c.CustomerID = a.CustomerID
    JOIN Transaction t ON a.AccountNumber = t.SourceAccount
    GROUP BY c.CustomerID
    ORDER BY TotalAmount DESC;
    """
    amount_by_customer_df = pd.read_sql(amount_by_customer_query, connection)

    # Query for number of transactions by customer
    transactions_by_customer_query = """
    SELECT c.Name, COUNT(*) as TransactionCount
    FROM Customer c
    JOIN Account a ON c.CustomerID = a.CustomerID
    JOIN Transaction t ON a.AccountNumber = t.SourceAccount
    GROUP BY c.CustomerID
    ORDER BY TransactionCount DESC;
    """
    transactions_by_customer_df = pd.read_sql(transactions_by_customer_query, connection)

    # Query for average account balance by account type
    avg_balance_by_type_query = """
    SELECT 'Savings' as Type, AVG(sa.MinimumBalanceRequirement) as AvgBalance
    FROM SavingsAccount sa
    UNION ALL
    SELECT 'Checking' as Type, AVG(ca.OverdraftLimit) as AvgBalance
    FROM CheckingAccount ca
    UNION ALL
    SELECT 'Loan' as Type, AVG(la.LoanAmount) as AvgBalance
    FROM LoanAccount la;
    """
    avg_balance_by_type_df = pd.read_sql(avg_balance_by_type_query, connection)

    # Query for loan amount distribution
    loan_amount_distribution_query = """
    SELECT LoanAmount
    FROM LoanAccount;
    """
    loan_amount_distribution_df = pd.read_sql(loan_amount_distribution_query, connection)

    # Query for Customer Demographics Analysis
    customer_age_query = """
    SELECT TIMESTAMPDIFF(YEAR, DateOfBirth, CURDATE()) AS Age
    FROM Customer;
    """
    customer_age_df = pd.read_sql(customer_age_query, connection)

    # Query for Fraud Detection Model Performance Analysis
    model_performance_query = """
    SELECT fdm.ModelVersion, COUNT(*) AS DetectedFrauds
    FROM Transaction t
    JOIN FraudDetectionModel fdm ON t.ModelVersionID = fdm.ModelVersion
    WHERE t.Status = 'Fraud'  -- Assuming 'Fraud' status indicates detected frauds
    GROUP BY fdm.ModelVersion
    ORDER BY fdm.ModelVersion;
    """
    model_performance_df = pd.read_sql(model_performance_query, connection)


    
    # Close the database connection
    connection.close()

    # Plotting the total transaction amount per day
    plt.figure(figsize=(14, 6))
    plt.plot(total_amount_per_day_df['Date'], total_amount_per_day_df['TotalAmount'], marker='o')
    plt.title('Total Transaction Amount Per Day')
    plt.xlabel('Date')
    plt.ylabel('Total Amount')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plotting the count of transactions per transaction type
    plt.figure(figsize=(14, 6))
    plt.bar(transaction_count_per_type_df['TransactionType'], transaction_count_per_type_df['TransactionCount'])
    plt.title('Transaction Count Per Type')
    plt.xlabel('Transaction Type')
    plt.ylabel('Transaction Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Visualization for total transaction amount by customer
    plt.figure(figsize=(14, 6))
    plt.bar(amount_by_customer_df['Name'], amount_by_customer_df['TotalAmount'])
    plt.title('Total Transaction Amount by Customer')
    plt.xlabel('Customer')
    plt.ylabel('Total Transaction Amount')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

    # Visualization for number of transactions by customer
    plt.figure(figsize=(14, 6))
    plt.bar(transactions_by_customer_df['Name'], transactions_by_customer_df['TransactionCount'])
    plt.title('Number of Transactions by Customer')
    plt.xlabel('Customer')
    plt.ylabel('Transaction Count')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

    # Visualization for average account balance by account type
    plt.figure(figsize=(14, 6))
    plt.bar(avg_balance_by_type_df['Type'], avg_balance_by_type_df['AvgBalance'])
    plt.title('Average Account Balance by Account Type')
    plt.xlabel('Account Type')
    plt.ylabel('Average Balance')
    plt.tight_layout()
    plt.show()

    # Visualization for loan amount distribution
    plt.figure(figsize=(14, 6))
    plt.hist(loan_amount_distribution_df['LoanAmount'], bins=20, color='green', edgecolor='black')
    plt.title('Loan Amount Distribution')
    plt.xlabel('Loan Amount')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

    # Visualization for Customer Demographics Analysis
    plt.figure(figsize=(14, 6))
    plt.hist(customer_age_df['Age'], bins=20, color='blue', edgecolor='black')
    plt.title('Customer Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Number of Customers')
    plt.tight_layout()
    plt.show()

    # Visualization for Fraud Detection Model Performance Analysis
    plt.figure(figsize=(14, 6))
    plt.bar(model_performance_df['ModelVersion'], model_performance_df['DetectedFrauds'])
    plt.title('Fraud Detection Model Performance')
    plt.xlabel('Model Version')
    plt.ylabel('Detected Frauds')
    plt.tight_layout()
    plt.show()

except Error as e:
    print(f"Error while connecting to MySQL: {e}")
