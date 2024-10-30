# URL-Shortening-Service
This project consists of simple RESTful API that allows users to shorten long URLs. The API provides endpoints to create, retrieve, update, and delete short URLs. It also provides statistics on the number of times a short URL has been accessed.

## Project URL
You can find more information about the project at https://roadmap.sh/projects/url-shortening-service.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)

## Prerequisites
Before you begin, ensure you have the following installed on your machine:

- **Python**: Version 3.10 or higher
- **Pip**: Python package installer
- **MongoDB**: Database server

## Installation
Follow these steps to set up your environment for the URL shortening service.

### 1. Install Python
If you don't have Python installed, download and install the latest version (>= 3.10).

### 2. Install Virtual Environment
It is recommended to create and activate a virtual environment for your project to manage dependencies effectively.

### 3. Install MongoDB
MongoDB is a NoSQL database used for storing data in JSON-like documents. Download and install MongoDB on your machine.

## Configuration
Follow these steps to configure your application for the URL shortening service.

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Create a Database in MongoDB
Create a new database using either a graphical user interface (GUI) tool like MongoDB Compass or the MongoDB shell.

### 3. Add .env File
Create a `.env` file in the root directory of the project and add the following configuration variables:
```plaintext
MONGO_URI=<YOUR MONGO URI>
```

## Running the Application
Once you have everything set up, you can run the Flask application using the following command:
```bash
flask --app app run
```
This command will start the Flask development server, and you should see output indicating that the server is running.

Use the following endpoints to verify that the application is running correctly and connected to the database:

- Application Status: ```GET /application-status```
- Database Connection Status: ```GET /database-connection-status```

#### You can now use the API endpoints as described in the project documentation.
