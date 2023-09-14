## Table of Contents
1. [Introduction](#introduction)
2. [Setup Instructions](#setup-instructions)
3. [API Endpoints](#api-endpoints)
    - [GET /persons](#get-persons)
    - [GET /person/:id](#get-personid)
    - [PUT /update/:id](#put-updateid)
    - [DELETE /delete/:id](#delete-deleteid)
    - [POST /create](#post-create)
4. [Request/Response Formats](#requestresponse-formats)

---

## 1. Introduction <a name="introduction"></a>

Welcome to the documentation for the Flask API for managing persons in your database. This API allows you to perform CRUD (Create, Read, Update, Delete) operations on person records.

## 2. Setup Instructions <a name="setup-instructions"></a>

To set up and run the Flask API on your local environment, follow these steps:

1. Clone the repository:

   ```shell
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```shell
   cd <project_directory>
   ```

3. Create a virtual environment (optional but recommended):

   ```shell
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```shell
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```shell
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Set up the PostgreSQL database:
   - Create a PostgreSQL database and note down the connection URL.
   - Create a `.env` file in the project directory and set the `DATABASE_URL` environment variable with the database URL.

7. Run the Flask application:

   ```shell
   python your_flask_app.py
   ```

The API should now be running locally at `http://localhost:5000`.

## 3. API Endpoints <a name="api-endpoints"></a>

### GET /persons <a name="get-persons"></a>

- **Description:** Retrieve a list of all persons in the database.

- **HTTP Method:** `GET`

- **Response:**
  - Status Code: `200 OK`
  - Content Type: `application/json`
  - Body:

    ```json
    [
        {
            "id": 1,
            "name": "John Doe"
        },
        {
            "id": 2,
            "name": "Jane Smith"
        }
        // ... other persons
    ]
    ```

### GET /person/:id <a name="get-personid"></a>

- **Description:** Retrieve a specific person by their ID.

- **HTTP Method:** `GET`

- **URL Parameters:**
  - `id` (integer): The unique ID of the person.

- **Response:**
  - Status Code: `200 OK` if found, `404 Not Found` if not found.
  - Content Type: `application/json`
  - Body (if found):

    ```json
    {
        "id": 1,
        "name": "John Doe"
    }
    ```

  - Body (if not found):

    ```json
    {
        "message": "Person not found"
    }
    ```

### PUT /update/:id <a name="put-updateid"></a>

- **Description:** Update the name of a specific person by their ID.

- **HTTP Method:** `PUT`

- **URL Parameters:**
  - `id` (integer): The unique ID of the person to be updated.

- **Request Body:**
  - Content Type: `application/json`
  - Body:

    ```json
    {
        "name": "Updated Name"
    }
    ```

- **Response:**
  - Status Code: `200 OK`
  - Content Type: `application/json`
  - Body:

    ```json
    {
        "message": "Person updated successfully"
    }
    ```

### DELETE /delete/:id <a name="delete-deleteid"></a>

- **Description:** Delete a specific person by their ID.

- **HTTP Method:** `DELETE`

- **URL Parameters:**
  - `id` (integer): The unique ID of the person to be deleted.

- **Response:**
  - Status Code: `200 OK`
  - Content Type: `application/json`
  - Body:

    ```json
    {
        "message": "Person deleted successfully"
    }
    ```

### POST /create <a name="post-create"></a>

- **Description:** Create a new person in the database.

- **HTTP Method:** `POST`

- **Request Body:**
  - Content Type: `application/json`
  - Body:

    ```json
    {
        "name": "New Person Name"
    }
    ```

- **Response:**
  - Status Code: `200 OK`
  - Content Type: `application/json`
  - Body:

    ```json
    {
        "message": "Person created successfully",
        "id": 42
    }
    ```

## 4. Request/Response Formats <a name="requestresponse-formats"></a>

### Request Format

- **GET /persons:**
  - No request body is required.

- **GET /person/:id:**
  - No request body is required.

- **PUT /update/:id:**
  - Content Type: `application/json`
  - Body:

    ```json
    {
        "name": "Updated Name"
    }
    ```

- **DELETE /delete/:id:**
  - No request body is required.

- **POST /create:**
  - Content Type: `application/json`
  - Body:

    ```json
    {
        "name": "New Person Name"
    }
    ```

### Response Format

- All responses have a content type of `application/json`.
- Successful responses (status code `200 OK`) include a JSON response body with a `"message"` field.
- For GET requests, the JSON response may also include `"id"` and `"name"` fields.
- For error responses (status codes other than `200 OK`), the JSON response includes a `"message"` field describing the error.
