🔹 Amazon EC2 (Elastic Compute Cloud)
✅ What it is: A virtual server in the cloud.
✅ Use Case: Hosting applications, websites, or running workloads.
✅ Key Features:

Scalable compute capacity (increase/decrease instances).
Different instance types optimized for computing, memory, or storage.
Auto Scaling for automatic resource adjustment.
✅ Example Question:
💬 How do you make an EC2 instance highly available?
💡 Answer: Use Auto Scaling Groups and Elastic Load Balancer (ELB) across multiple Availability Zones (AZs).


🔹 AWS Lambda
✅ What it is: A serverless compute service. Runs code without managing servers.
✅ Use Case: Running backend logic, processing API requests, event-driven tasks.
✅ Key Features:

Pay only for execution time.
Supports multiple languages (Python, Node.js, Java, etc.).
Integrates with S3, API Gateway, DynamoDB, and more.
✅ Example Question:
💬 How does AWS Lambda scale?
💡 Answer: AWS automatically scales Lambda by running multiple instances in parallel as needed.

🔹 Amazon S3 (Simple Storage Service)
✅ What it is: Object storage for any type of data (files, images, backups, etc.).
✅ Use Case: Storing website assets, logs, and backups.
✅ Key Features:

Highly durable (99.999999999% durability).
Versioning and lifecycle policies for data retention.
Security via IAM roles and bucket policies.
✅ Example Question:
💬 How can you make an S3 bucket publicly accessible?
💡 Answer: Update the Bucket Policy to allow public read access, but it's recommended to use CloudFront for secure content delivery.


🔹 Amazon RDS (Relational Database Service)
✅ What it is: Managed database service for MySQL, PostgreSQL, SQL Server, etc.
✅ Use Case: Running relational databases without manual maintenance.
✅ Key Features:

Automatic backups and replication.
Scaling and performance optimization.
Security via IAM and encryption.
✅ Example Question:
💬 How do you improve performance in RDS?
💡 Answer: Use Read Replicas for scaling read operations, Aurora Serverless for auto-scaling, and indexes for optimized queries.


🔹 Amazon API Gateway
✅ What it is: A fully managed API service for creating, deploying, and managing APIs.
✅ Use Case: Exposing RESTful and WebSocket APIs to clients.
✅ Key Features:

Integrates with Lambda, EC2, and other AWS services.
Supports authentication via IAM and Cognito.
API rate limiting and caching for performance.
✅ Example Question:
💬 How do you secure an API in API Gateway?
💡 Answer: Use IAM Roles, API Keys, Cognito, or JWT (OAuth2) for authentication and authorization.



🔹 AWS IAM (Identity and Access Management)
✅ What it is: Controls access to AWS resources securely.
✅ Use Case: Managing users, roles, and permissions in AWS.
✅ Key Features:

Policies to define access levels (e.g., read-only, admin).
Multi-Factor Authentication (MFA) for extra security.
Role-based access for services (e.g., allowing EC2 to access S3).
✅ Example Question:
💬 What is the principle of least privilege in IAM?
💡 Answer: Give only the permissions necessary for a user or service to perform its tasks.


🚀 Summary Table
AWS Service	Purpose	Key Feature
EC2	Cloud-based virtual server	Scalable compute power
Lambda	Serverless function execution	Auto-scaling and pay-per-use
S3	Object storage	Secure, highly durable storage
RDS	Managed relational databases	Auto backups and scaling
API Gateway	Manages and exposes APIs	Secure API integration
IAM	Access control and security	User, role, and permission management

