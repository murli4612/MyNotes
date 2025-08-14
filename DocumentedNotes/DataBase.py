🔹 Basic SQL Questions
1️⃣ What is the difference between DELETE, TRUNCATE, and DROP?
2️⃣ What are the different types of joins in SQL? (INNER, LEFT, RIGHT, FULL OUTER)
3️⃣ What is the difference between WHERE and HAVING?
4️⃣ What are primary keys and foreign keys?
5️⃣ What is the difference between UNION and UNION ALL?

🔹 SQL Query Writing Questions
6️⃣ Find the second highest salary from an "employees" table.

SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees);

7️⃣ Retrieve the count of employees in each department.
SELECT department_id, COUNT(*) AS employee_count FROM employees GROUP BY department_id;


8️⃣ Find duplicate records in a table.


SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name HAVING COUNT(*) > 1;

9️⃣ Write a query to fetch the 3rd highest salary using LIMIT (MySQL/PostgreSQL).
SELECT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 2;

10️⃣ Find employees who joined in the last 6 months.
SELECT * FROM employees WHERE join_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH);


🔹 Advanced SQL Questions
1️⃣1️⃣ What is a CTE (Common Table Expression)? Write an example.

WITH EmployeeCTE AS (
    SELECT id, name, salary, department_id
    FROM employees
    WHERE salary > 50000
)
SELECT * FROM EmployeeCTE;

1️⃣2️⃣ What is the difference between a clustered and a non-clustered index?
1️⃣3️⃣ What are window functions? Explain with an example

SELECT name, salary, department, 
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS Rank
FROM employees;


1️⃣4️⃣ How do you optimize a slow SQL query? (Indexes, Query Execution Plan, Avoiding SELECT *, etc.)

1️⃣5️⃣ What is the difference between EXISTS and IN in SQL?


🔹 SQL Database Design & Normalization
1️⃣6️⃣ What is normalization? Explain different normal forms (1NF, 2NF, 3NF, BCNF).
1️⃣7️⃣ What is denormalization? When would you use it?
1️⃣8️⃣ What are transactions in SQL? Explain ACID properties.
1️⃣9️⃣ What is a deadlock in SQL, and how can you prevent it?
2️⃣0️⃣ What is the difference between OLTP and OLAP databases?



answer:

1️⃣ What is the difference between DELETE, TRUNCATE, and DROP?
Command	    Purpose                                     	Rollback Possible?	                                        Affects Structure?	         Performance

DELETE	Removes specific rows based on a condition	    ✅ Yes (if inside a transaction)	                            ❌ No	                        Slower (logs each row)
TRUNCATE	Removes all rows from a table	            ❌ No	                                                         ❌ No	                         Faster (minimal logging)
DROP	Deletes entire table (schema + data)	           ❌ No	                                                    ✅ Yes (removes structure)	    Fastest


2️⃣ What are the different types of joins in SQL?
Join Type	   Description                       	                                          Example
INNER JOIN	   Returns only matching rows from both tables	                                 SELECT * FROM A INNER JOIN B ON A.id = B.id;
LEFT JOIN	   Returns all rows from the left table and matching rows from the right	SELECT * FROM A LEFT JOIN B ON A.id = B.id;
RIGHT JOIN	     Returns all rows from the right table and matching rows from the left	SELECT * FROM A RIGHT JOIN B ON A.id = B.id;
FULL OUTER JOIN	 Returns all rows when there is a match in either table	                SELECT * FROM A FULL OUTER JOIN B ON A.id = B.id;


3️⃣ What is the difference between WHERE and HAVING?
WHERE is used before aggregation (GROUP BY) and filters individual rows.
HAVING is used after aggregation (GROUP BY) and filters grouped results.

SELECT department, COUNT(*) 
FROM employees 
WHERE salary > 50000  -- Filters individual rows before grouping
GROUP BY department
HAVING COUNT(*) > 5;  -- Filters groups after aggregation


4️⃣ What are primary keys and foreign keys?
Primary Key: A unique identifier for each row in a table (e.g., id column).
Foreign Key: A reference to a primary key in another table, maintaining relationships.
Example:
    
CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE Salaries (
    emp_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (emp_id) REFERENCES Employees(id)
);


5️⃣ What is the difference between UNION and UNION ALL?
Feature	UNION	UNION ALL
Removes Duplicates?	✅ Yes	❌ No
Performance	Slower (checks for duplicates)	Faster (direct merge)
Example	SELECT name FROM A UNION SELECT name FROM B;	SELECT name FROM A UNION ALL SELECT name FROM B;

🔹 SQL Query Writing Questions
6️⃣ Find the second highest salary from an "employees" table.

SELECT MAX(salary) 
FROM employees 
WHERE salary < (SELECT MAX(salary) FROM employees);


7️⃣ Retrieve the count of employees in each department.

SELECT department_id, COUNT(*) AS employee_count 
FROM employees 
GROUP BY department_id;

8️⃣ Find duplicate records in a table.
SELECT column_name, COUNT(*) 
FROM table_name 
GROUP BY column_name 
HAVING COUNT(*) > 1;


9️⃣ Write a query to fetch the 3rd highest salary using LIMIT.
SELECT salary 
FROM employees 
ORDER BY salary DESC 
LIMIT 1 OFFSET 2;



🔟 Find employees who joined in the last 6 months.
SELECT * FROM employees 
WHERE join_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH);


1️⃣1️⃣ What is a CTE (Common Table Expression)?
WITH EmployeeCTE AS (
    SELECT id, name, salary, department_id
    FROM employees
    WHERE salary > 50000
)
SELECT * FROM EmployeeCTE;

1️⃣2️⃣ What is the difference between a clustered and a non-clustered index?
Clustered Index: Sorts and stores data physically in the table. Only one per table.
Non-Clustered Index: Stores pointers to data, allowing multiple indexes on a table.

1️⃣3️⃣ What are window functions?
Used for calculations across a set of rows related to the current row.

SELECT name, salary, department, 
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS Rank
FROM employees;


1️⃣4️⃣ How do you optimize a slow SQL query?
✅ Use Indexes to speed up search queries.
✅ Use EXPLAIN to analyze query execution plans.
✅ Avoid SELECT *, fetch only required columns.
✅ Optimize JOINs and WHERE conditions.
✅ Use Partitioning and Caching.

1️⃣5️⃣ What is the difference between EXISTS and IN in SQL?
EXISTS: Stops searching as soon as a match is found (better for large datasets).
IN: Retrieves all matching values before processing (slower with large subqueries).


SELECT * FROM employees e
WHERE EXISTS (
    SELECT 1 FROM departments d WHERE e.department_id = d.id
);


🔹 SQL Database Design & Normalization
1️⃣6️⃣ What is normalization? Explain normal forms (1NF, 2NF, 3NF, BCNF).
1NF: Remove duplicate columns (Atomic values).
2NF: No partial dependencies (Every non-key column depends on the primary key).
3NF: No transitive dependencies (No column should depend on another non-key column).
BCNF: More strict than 3NF, ensures that every determinant is a candidate key.


1️⃣7️⃣ What is denormalization? When would you use it?
✅ Denormalization combines tables to reduce joins and improve query speed.
✅ Used in reporting databases where read performance is critical.


1️⃣8️⃣ What are transactions in SQL? Explain ACID properties.
✅ Atomicity: All operations complete or none do.
✅ Consistency: Data remains valid before/after transaction.
✅ Isolation: Transactions do not affect each other.
✅ Durability: Changes are permanent after commit.

1️⃣9️⃣ What is a deadlock in SQL, and how can you prevent it?
✅ Deadlock occurs when two transactions wait for each other’s resources indefinitely.
✅ Prevention Strategies:

Use short transactions.
Lock tables in the same order in all transactions.
Implement deadlock detection in the DB engine.


2️⃣0️⃣ What is the difference between OLTP and OLAP databases?
Feature	OLTP (Online Transaction Processing)	OLAP (Online Analytical Processing)
Use Case	Real-time transactions	Data analysis & reporting
Data Type	Current operational data	Historical & aggregated data
Example	Banking, E-commerce	Business Intelligence, Data Warehousing

Here are different ways to find the second highest salary in SQL:
    
    
    1️⃣ Using LIMIT and OFFSET (MySQL, PostgreSQL)
    SELECT salary 
FROM employees 
ORDER BY salary DESC 
LIMIT 1 OFFSET 1;

✅ Explanation:

Orders salaries in descending order.
OFFSET 1 skips the highest salary.
LIMIT 1 fetches only the second highest salary.



2️⃣ Using MAX() with a Subquery (Works in all SQL databases)

SELECT MAX(salary) 
FROM employees 
WHERE salary < (SELECT MAX(salary) FROM employees);



✅ Explanation:

First MAX(salary) gets the highest salary.
Second MAX(salary) finds the highest salary excluding the top salary (i.e., second highest).

3️⃣ Using DISTINCT with ORDER BY (Handles duplicate salaries)

SELECT DISTINCT salary 
FROM employees 
ORDER BY salary DESC 
LIMIT 1 OFFSET 1;


✅ Explanation:

DISTINCT removes duplicate salaries.
Orders in descending order and fetches the second unique highest salary.


4️⃣ Using DENSE_RANK() (Works in SQL Server, PostgreSQL, Oracle, MySQL 8+)

SELECT salary 
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk 
    FROM employees
) ranked_salaries 
WHERE rnk = 2;


✅ Explanation:

DENSE_RANK() assigns a ranking to salaries.
Filters out the row where rank = 2 (i.e., second highest salary).


5️⃣ Using ROW_NUMBER() (For exact second highest, ignoring duplicates)

SELECT salary 
FROM (
    SELECT salary, ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn 
    FROM employees
) ranked 
WHERE rn = 2;



✅ Difference:

ROW_NUMBER() ensures unique row numbers, so it won’t return duplicates.

💡 Which Method to Use?
Method	Best Use Case
LIMIT OFFSET	Simple & fast for small datasets (MySQL, PostgreSQL)
MAX() with Subquery	Works on all SQL databases
DISTINCT ORDER BY	Handles duplicate salaries
DENSE_RANK()	Returns all records sharing 2nd rank (handles ties)
ROW_NUMBER()	Ensures a single second-highest salary (ignores ties)

It looks like you're asking about the WHERE and HAVING clauses in SQL. Here's a quick breakdown:

1. WHERE Clause
Used to filter records before grouping (i.e., it applies to individual rows).
Works with SELECT, UPDATE, DELETE queries.

Example
SELECT * FROM employees
WHERE salary > 50000;

2. HAVING Clause
Used to filter records after grouping (i.e., it applies to groups created by GROUP BY).
Works only with aggregate functions like COUNT(), SUM(), AVG(), etc.

Example

SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;



Key Difference
WHERE filters before aggregation.
HAVING filters after aggregation.

ACID Properties in Databases
ACID stands for Atomicity, Consistency, Isolation, and Durability—these properties ensure reliable database transactions.

Atomicity (All or Nothing)

A transaction is fully completed or not executed at all.
If one part of a transaction fails, the entire transaction is rolled back.
Example:

BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT; -- Ensures both updates succeed or fail together


Consistency (Valid State)

A transaction brings the database from one valid state to another.
Ensures constraints (e.g., foreign keys, data types) are maintained.
Example: If transferring money, the total balance across accounts should remain consistent.

Isolation (Independent Transactions)

Ensures that concurrent transactions don’t interfere with each other.
Isolation levels include:
Read Uncommitted
Read Committed
Repeatable Read
Serializable

Durability (Permanent Changes)

Once a transaction is committed, changes are permanently saved.
Even if a system crashes, committed data is not lost.
Example: Databases use write-ahead logs (WAL) to recover data after a crash.





