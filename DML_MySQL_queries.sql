use  Fraud_Detection_system;

SELECT ModelVersionID, COUNT(*) AS TotalTransactions, SUM(CASE WHEN Status = 'Flagged' THEN 1 ELSE 0 END) AS FlaggedTransactions
FROM Transaction
GROUP BY ModelVersionID
LIMIT 10;

SELECT AVG(LoanAmount) AS AverageLoanAmount, AVG(LoanTermMonths) AS AverageLoanTerm
FROM LoanAccount
LIMIT 10;

SELECT InsightType, COUNT(*) AS InsightCount, YEAR(DateGenerated) AS Year
FROM FinancialInsight
GROUP BY InsightType, Year
LIMIT 10;

SELECT 'Savings' AS AccountType, AVG(AccountBalance) AS AverageBalance
FROM Account JOIN SavingsAccount ON Account.AccountNumber = SavingsAccount.AccountNumber
UNION
SELECT 'Checking', AVG(AccountBalance)
FROM Account JOIN CheckingAccount ON Account.AccountNumber = CheckingAccount.AccountNumber
LIMIT 10;

SELECT IPAddress, DeviceID, COUNT(*) AS TransactionCount
FROM SecurityParameters JOIN Transaction ON SecurityParameters.TransactionID = Transaction.TransactionID
GROUP BY IPAddress, DeviceID
LIMIT 10;

SELECT YEAR(Date) AS Year, AVG(AccountBalance) AS AverageBalance
FROM Account JOIN Transaction ON Account.AccountNumber = Transaction.SourceAccount
GROUP BY Year
LIMIT 10;


SELECT TransactionID, Amount, FraudDetectionModel.Sensitivity
FROM Transaction JOIN FraudDetectionModel ON Transaction.ModelVersionID = FraudDetectionModel.ModelVersion
WHERE Amount > 200 AND FraudDetectionModel.Sensitivity > 0.7
LIMIT 10;


SELECT Type, COUNT(*) AS FeedbackCount
FROM CustFeedback
GROUP BY Type
LIMIT 10;

Select * from FraudDetectionModel;
Select * from Transaction;
Select * from SecurityParameters;
Select * from LoanAccount;
Select * from Account;
Select * from Customer;