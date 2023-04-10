<h1>Address Book FAST API</h1>
This is a FAST API for managing a list of addresses. It allows you to add, update, delete, and retrieve addresses. You can also retrieve a list of all addresses or all addresses within a certain distance from a given location.

<h2>Getting Started</h2>
To get started with this project, you'll need to follow these steps:

<h3>Prerequisites</h3>
Before you can run this project, you'll need to have the following software installed:
Python 3.6 or higher
pip (the Python package manager)

<h3>Installing</h3>
1. Clone this repository to your local machine:
git clone https://github.com/Nikolay-x/Address-Book-FAST-API

2. Navigate to the project directory:
cd Address-Book-FAST-API

3. Install the project dependencies:
pip install -r requirements.txt

<h2>Running the API</h2>
To run the API, you'll need to start the server using the following command:
uvicorn main:app --reload
This will start the server and enable auto-reloading of the code whenever changes are made.

<h3>Using the API</h3>
The API can be accessed using the following endpoints:

- 'GET /all_addresses' - Retrieves a list of all addresses in the database.
- 'POST /addresses' - Adds a new address to the database.
- 'PUT /addresses/{id}' - Updates an existing address with the specified ID.
- 'DELETE /addresses/{id}' - Deletes an existing address with the specified ID.
- 'GET /addresses/{id}' - Retrieves the address with the specified ID.
- 'GET /addresses' - Retrieves a list of all addresses within a certain distance from a given location.

For more information on the parameters and responses for each endpoint, please refer to the API documentation.

<h3>FAST API Documentation</h3>
The FAST API documentation can be accessed by opening the following URL in your web browser:
http://localhost:8000/docs

This will open the Swagger UI, which provides detailed information about the API endpoints, including input parameters, output formats, and example requests and responses.