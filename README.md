# Database-System-for-Banking-Fraud-Detection-and-Analysis

**Real World Business Problem Definition:**

With the rapid advancement of technology and increasing online transactions, the modern banking system faces a twofold challenge. Firstly, it is imperative to maintain a stringent and proactive fraud detection system that can preemptively identify and combat fraudulent activities. Given the volume of daily transactions, this is no trivial feat. An unsuspected fraudulent transaction can lead to significant financial losses and damage the reputation of the financial institution.

Secondly, as customers' financial behaviors become more intricate, there's an emerging need to understand and interpret these patterns. By doing so, banking institutions can offer more tailored and efficient services, enhancing the user experience. Moreover, deciphering these financial patterns can also lead to offering valuable insights to customers, promoting intelligent financial behavior and deepening trust between the institution and its clients.

The proposed integrated system aims to address both these challenges, combining an advanced fraud detection mechanism with a financial insight module. This dual solution not only ensures the security of transactions but also provides a value-added service by granting customers a deeper understanding of their financial habits.

**Executive Summary:**

The Fraud Detection System project aimed to develop a comprehensive solution for identifying and managing fraudulent activities in financial transactions. The project was designed to safeguard customer accounts and uphold the integrity of financial operations. The primary goal of the study was to create a robust fraud detection framework using advanced data modeling techniques, enabling real-time identification and prevention of fraudulent activities. The project required the creation of a detailed data model, encompassing various entities such as customers, accounts, transactions, and fraud detection parameters. Using Enhanced Entity-Relationship (EER) and Unified Modeling Language (UML) diagrams, the team effectively mapped out the relationships, constraints, and cardinalities of these entities.

The relational model was implemented in MySQL, with comprehensive tables, primary and foreign keys, and relational constraints, ensuring data integrity and efficiency. The project also explored partial NoSQL implementation for broader applicability. Python was employed for data analysis and visualization, offering insights into transaction patterns, customer behaviors, and model performance. This facilitated data-driven decision-making and continuous improvement of the fraud detection model. The system successfully integrated multiple data sources, providing a holistic view of transactional activities. It demonstrated proficiency in detecting potential frauds, analyzing customer feedback, and understanding financial patterns.

Future enhancements could include integrating machine learning algorithms for predictive analysis and expanding the NoSQL implementation for greater scalability.

**Opportunity and Significance:**
In an era of digital finance, the surge in online transactions has escalated the incidence of financial fraud, posing a significant threat to both financial institutions and customers. Recognizing this, our study centers on developing a Fraud Detection System, aiming to mitigate these risks. The significance of this study lies in its potential to enhance transaction security, safeguard customer assets, and maintain the integrity of financial systems.

**The Problem:**
The primary challenge addressed by our study is the increasing prevalence and sophistication of financial fraud in digital transactions. Traditional systems often fail to detect advanced fraudulent schemes, leading to financial losses and compromised customer trust.

**The Goal:**
Our study's goal is to design and implement an effective Fraud Detection System using advanced data modeling and analytics. This system aims to identify and prevent fraudulent activities in real-time, thereby enhancing the security of financial transactions. The aim should also be reducing false positives as it can affect customer satisfaction.

**The Requirements:**
The project requires the construction of a comprehensive database encompassing various entities such as customers, accounts, transactions, and fraud detection models. It involves the application of Enhanced Entity-Relationship (EER) and Unified Modeling Language (UML) for data modeling, the implementation of a relational model in MySQL, data analysis, and visualization using Python, and the exploration of NoSQL implementations for scalability and flexibility.

**ER Diagram:**

<img width="997" alt="Screenshot 2024-01-08 at 2 00 55 PM" src="https://github.com/nayakatul/Database-System-for-Banking-Fraud-Detection-and-Analysis/assets/125909401/4025862d-73c9-44c8-9602-2cf279adee19">




**UML Diagram:**

<img width="1024" alt="Screenshot 2024-01-08 at 2 01 32 PM" src="https://github.com/nayakatul/Database-System-for-Banking-Fraud-Detection-and-Analysis/assets/125909401/464ff71e-06f2-4c34-853e-e670610bd52b">

**Mapping Conceptual Model to Relational Model:**

In the Fraud Detection System project, the EER and UML conceptual models were translated into a relational database structure as follows:
Customer Table holds customer information with CustomerID as the primary key. It includes essential details like name, address, date of birth, and contact information, with a constraint that these fields cannot be null.
 
Account Table is linked to the Customer table via CustomerID as a foreign key. It uniquely identifies each account with AccountNumber as the primary key and includes account type and balance.

Transaction Table captures transaction details, identified by TransactionID. It includes foreign keys to the Account table for both source and destination accounts, and a foreign key to the FraudDetectionModel table, ensuring each transaction is associated with a specific fraud detection model version.
FraudDetectionModel Table stores data on different versions of the fraud detection models, with ModelVersion as the primary key and attributes like last trained date, sensitivity, and alert level.
Additional tables like SecurityParameters, CustFeedback, FinancialInsight, and account type-specific tables (SavingsAccount, CheckingAccount, LoanAccount) are integrated with appropriate primary and foreign keys, ensuring a comprehensive and interconnected database structure.

**Implementation of Relation Model via MySQL and NoSQL:**

**MySQL Implementation:**

The relational model has been implemented in MySQL, a process that involved creating tables as per the defined schema and populating them with data. This setup reflects the relationships and constraints specified in the EER and UML diagrams, ensuring data integrity and efficient retrieval. SQL DDL scripts were used to create tables for entities like Customer, Account, Transaction, etc., and to establish the necessary foreign key relationships. The database has been populated with relevant dummy data, providing a rich dataset for analysis and demonstration.

**NoSQL Implementation:**

A partial implementation of the relational model has also been explored in NoSQL to showcase the adaptability of the system in different database environments. This involved translating a subset of the MySQL tables into a NoSQL format, typically in a document- based database like MongoDB. This exercise demonstrates how the relational model can be adapted to a schema-less environment, which can be beneficial for certain types of data queries and analyses. We exported the data in JSON from MySQL workbench and used MongoDB Atlas and MongoDB Compass to import the data to MongoDB.

Both implementations play a crucial role in demonstrating the versatility and robustness of the Fraud Detection System in handling complex data relationships across different database systems.


**Database Access via R or Python:**

In the Fraud Detection System project, Python was utilized to access and analyze the MySQL database. This involved establishing a connection to the database, executing various SQL queries, and using pandas for data manipulation. The analysis covered aspects like total transaction amounts per day, transaction counts by type, and customer- specific transaction details. Additionally, matplotlib was employed for visualizations, including plots and histograms, to depict transaction trends, loan amount distributions, and customer demographics. This approach demonstrated efficient database interaction and data-driven insights, essential for the system's functionality.

Below are some of the visualizations generated using Python.

The below graph illustrates the average account balances categorized by account type: Savings, Checking, and Loan. It shows that Loan accounts have a significantly higher average balance compared to Savings and Checking accounts.

![Picture1](https://github.com/nayakatul/Database-System-for-Banking-Fraud-Detection-and-Analysis/assets/125909401/d4eb8503-2148-4b30-8ce7-1420bd724da0)

The next graph displays the age distribution of customers. It indicates that the majority of customers fall within the 35 to 45 age range, with peaks in the distribution suggesting that certain age groups are more prevalent than others within the customer base.

![Picture2](https://github.com/nayakatul/Database-System-for-Banking-Fraud-Detection-and-Analysis/assets/125909401/48522d17-6b66-4761-8ae6-8d06866baa15)

**Summary and recommendation:**

The Fraud Detection System project successfully designed a relational database in MySQL and partially in NoSQL, modeling complex data structures for fraud detection. Python was used for database interaction, data analysis, and visualization, providing valuable insights into transaction patterns and fraud detection efficacy.

**Advantages:**
-	Robust data modeling and relational structure.
-	Effective fraud detection and analysis capabilities.
-	Versatile Python integration for data manipulation and visualization.

**Shortcomings:**
•	Potential scalability challenges with increasing data volume.
•	Limited implementation in NoSQL.

**Recommendations:**
•	Explore advanced analytics and machine learning for predictive fraud detection.
•	Expand NoSQL implementation for scalability and flexibility.
•	Continuously update the fraud detection model to adapt to evolving fraud tactics.
•	Summarize your use case study. Access the advantages and shortcomings and make recommendations.






