# Flask CRUD Application

This is a simple Flask web application that allows you to perform CRUD (Create, Read, Update, Delete) operations on a list of persons stored in a PostgreSQL database.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- View a list of persons.
- View details of a specific person by ID.
- Create a new person.
- Update the information of an existing person by ID.
- Delete a person by ID.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- PostgreSQL database installed and configured.

## Getting Started

### Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/your-username/your-flask-crud-app.git
   ```

2. Change into the project directory:

   ```shell
   cd your-flask-crud-app
   ```

3. Create a virtual environment (optional but recommended):

   ```shell
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - On macOS and Linux:

     ```shell
     source venv/bin/activate
     ```

   - On Windows (PowerShell):

     ```shell
     .\venv\Scripts\Activate
     ```

5. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

### Configuration

1. Create a PostgreSQL database for your application.

2. Update the database connection details in `app.py`:

   ```python
   connection = psycopg2.connect(database="YourDatabaseName", host="localhost", user="YourUsername", password="YourPassword")
   ```

## Usage

1. Run the Flask application:

   ```shell
   python app.py
   ```

2. Access the application in your web browser at `http://localhost:5000`.

## API Endpoints

- `GET /`: View a list of all persons.
- `GET /person/<id>`: View details of a specific person by ID.
- `POST /create`: Create a new person.
- `POST /update/<id>`: Update the information of an existing person by ID.
- `POST /delete/<id>`: Delete a person by ID.

## Testing

You can use Postman or other API testing tools to test the CRUD functionality of the API. Refer to the API endpoints section above for details on how to use each endpoint.
