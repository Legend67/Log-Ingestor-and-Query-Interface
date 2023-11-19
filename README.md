# Log Ingestor

Welcome to the Log Ingestor project! This simple Flask application allows you to ingest logs and query them based on various parameters.

## Table of Contents

- [How to Run the Project](#how-to-run-the-project)
- [System Design](#system-design)
- [Features Implemented](#features-implemented)
- [Identified Issues](#identified-issues)

## How to Run the Project

### 1. Install Dependencies
Ensure you have Flask installed. If not, run:

```bash
pip install flask
```
### 2. Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/Legend67/Log-Ingestor-and-Query-Interface.git
cd log-ingestor
```

### 3. Run the Application
Execute the following command to run the Flask application:

```bash
Copy code
python log_ingestor.py
```
The application will run on http://127.0.0.1:3000/.

## System Design
This Log Ingestor is a simple Flask application designed to handle log ingestion and querying. It uses an in-memory list (logs) to store ingested logs. Each log entry is a JSON object containing various fields.

### Features Implemented
### 1. Ingest Logs
Endpoint: /ingest
Method: POST
Example:
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"level\": \"error\", \"message\": \"Failed to connect to DB\", \"resourceId\": \"server-1234\", \"timestamp\": \"2023-09-15T08:00:00Z\", \"traceId\": \"abc-xyz-123\", \"spanId\": \"span-456\", \"commit\": \"5e5342f\", \"metadata\": {\"parentResourceId\": \"server-0987\"}}" http://127.0.0.1:3000/ingest
```
### 2. Query Logs
Endpoint: /query
Method: GET
Example:
```bash
curl "http://127.0.0.1:3000/query?level=error"
```
### Identified Issues
The system currently uses in-memory storage (logs list), which means logs are lost when the application is restarted.
There is no validation or sanitation of incoming log data, making the system susceptible to invalid or malicious input.
