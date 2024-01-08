CREATE DATABASE Fraud_Detection_System;
use Fraud_Detection_System;

CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    ContactDetails VARCHAR(255) NOT NULL
);

CREATE TABLE Account (
    AccountNumber INT PRIMARY KEY,
    Type VARCHAR(50) NOT NULL,
    AccountBalance DECIMAL(10, 2) NOT NULL,
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE FraudDetectionModel (
    ModelVersion INT PRIMARY KEY,
    LastTrainedDate DATE NOT NULL,
    Sensitivity DECIMAL(5, 2),
    AlertLevel VARCHAR(50)
);


CREATE TABLE Transaction (
    TransactionID INT PRIMARY KEY,
    Amount DECIMAL(10, 2) NOT NULL,
    Date DATE NOT NULL,
    SourceAccount INT,
    DestinationAccount INT,
    TransactionType VARCHAR(50) NOT NULL,
    MerchantDetails VARCHAR(255),
    Status VARCHAR(50) NOT NULL,
    ModelVersionID INT, -- New foreign key column
    FOREIGN KEY (SourceAccount) REFERENCES Account(AccountNumber),
    FOREIGN KEY (DestinationAccount) REFERENCES Account(AccountNumber),
    FOREIGN KEY (ModelVersionID) REFERENCES FraudDetectionModel(ModelVersion) -- New foreign key reference
);


CREATE TABLE SecurityParameters (
    ParameterID INT PRIMARY KEY,
    IPAddress VARCHAR(15),
    DeviceID VARCHAR(255),
    TransactionID INT NOT NULL,
    FOREIGN KEY (TransactionID) REFERENCES Transaction(TransactionID)
);

CREATE TABLE CustFeedback (
    FeedbackID INT PRIMARY KEY,
    Description TEXT,
    CustomerID INT,
    TransactionID INT,
    InsightID INT,
    Type VARCHAR(50) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (TransactionID) REFERENCES Transaction(TransactionID),
    FOREIGN KEY (InsightID) REFERENCES FinancialInsight(InsightID)
    -- Add a foreign key reference for InsightID if necessary
);

CREATE TABLE FinancialInsight (
    InsightID INT PRIMARY KEY,
    CustomerID INT NOT NULL,
    TransactionPatterns TEXT,
    InsightType VARCHAR(50) NOT NULL,
    InsightDetail TEXT,
    DateGenerated DATE NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE SavingsAccount (
    AccountNumber INT PRIMARY KEY,
    InterestRate DECIMAL(5, 2),
    MinimumBalanceRequirement DECIMAL(10, 2),
    FOREIGN KEY (AccountNumber) REFERENCES Account(AccountNumber)
);


CREATE TABLE CheckingAccount (
    AccountNumber INT PRIMARY KEY,
    OverdraftLimit DECIMAL(10, 2),
    ATMWithdrawalLimit DECIMAL(10, 2),
    FOREIGN KEY (AccountNumber) REFERENCES Account(AccountNumber)
);


CREATE TABLE LoanAccount (
    AccountNumber INT PRIMARY KEY,
    LoanAmount DECIMAL(10, 2) NOT NULL,
    InterestRate DECIMAL(5, 3) NOT NULL,
    LoanTermMonths INT NOT NULL,
    FOREIGN KEY (AccountNumber) REFERENCES Account(AccountNumber)
);


CREATE TABLE CustFeedbackFinancialInsight (
    FeedbackID INT,
    InsightID INT,
    PRIMARY KEY (FeedbackID, InsightID),
    FOREIGN KEY (FeedbackID) REFERENCES CustFeedback(FeedbackID),
    FOREIGN KEY (InsightID) REFERENCES FinancialInsight(InsightID)
);

CREATE TABLE TransactionFinancialInsight (
    TransactionID INT,
    InsightID INT,
    PRIMARY KEY (TransactionID, InsightID),
    FOREIGN KEY (TransactionID) REFERENCES Transaction(TransactionID),
    FOREIGN KEY (InsightID) REFERENCES FinancialInsight(InsightID)
);





