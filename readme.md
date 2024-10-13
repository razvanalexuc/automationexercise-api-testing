# AutomationExercise API Testing

This project contains automated tests for the AutomationExercise API using Python and the `requests` library. The tests are designed to verify various API endpoints and ensure they behave as expected.

In addition to automated tests, manual testing of the API endpoints has been performed using Postman. The Postman collection and environment files are included in the `Manual_Postman` directory. These files can be imported into Postman to manually test the API endpoints.

## Table of Contents

- [Project Description](#project-description)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Manual Testing with Postman](#manual-testing-with-postman)
- [Contributing](#contributing)

## Project Description

The project includes automated tests for the following API endpoints:

- **`POST /api/verifyLogin`**: Verifies login with valid and invalid details.
  - **Valid Login**: Tests the login functionality with valid email and password.
  - **Invalid Login**: Tests the login functionality with missing or incorrect email/password.

- **`DELETE /api/verifyLogin`**: Verifies that the DELETE method is not allowed on the login endpoint.
  - **Method Not Allowed**: Ensures that a DELETE request to the login endpoint returns a 405 status code.

- **`POST /api/productsList`**: Retrieves the list of products.
  - **Get All Products**: Tests the retrieval of all products using a POST request.

- **`POST /api/searchProduct`**: Searches for a product by name.
  - **Search Product**: Tests the search functionality by providing a product name.

- **`POST /api/createAccount`**: Creates a new user account.
  - **Create Account**: Tests the account creation functionality with valid user details.

- **`POST /api/deleteAccount`**: Deletes an existing user account.
  - **Delete Account**: Tests the account deletion functionality with valid user credentials.

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/automationexercise-api-testing.git
    cd automationexercise-api-testing
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the tests, you need to have the `pytest` framework installed. You can run the tests using the following command:

```sh
pytest
```
## Running Tests

The tests are located in the `Automation_Pytest` directory. Each test file contains tests for specific API endpoints.

To run a specific test file, use the following command:
```sh
pytest Automation_Pytest/test_POST_Operations.py
```

You can also generate a detailed report by using the -v (verbose) option:
```sh
pytest -v
```

## Manual Testing with Postman

In addition to automated tests, manual testing of the API endpoints has been performed using Postman. The Postman collection and environment files are included in the `Manual_Postman` directory. These files can be imported into Postman to manually test the API endpoints.

### Steps to Import Postman Collection

1. Open Postman.
2. Click on the `Import` button in the top-left corner.
3. Select the `Manual_Postman` directory and choose the collection file (`*.postman_collection.json`).
4. Click on `Import` to add the collection to your Postman workspace.

### Running Requests in Postman

1. Select the imported collection from the left sidebar.
2. Choose the desired request from the collection.
3. Ensure the correct environment is selected from the environment dropdown in the top-right corner.
4. Click on the `Send` button to execute the request and view the response.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. **Fork the Repository**: Click on the `Fork` button at the top right of this page to create a copy of this repository in your GitHub account.

2. **Clone the Repository**: Clone the forked repository to your local machine using the following command:
    ```sh
    git clone https://github.com/razvanalexuc/automationexercise-api-testing.git
    cd automationexercise-api-testing
    ```

3. **Create a New Branch**: Create a new branch for your feature or bugfix:
    ```sh
    git checkout -b feature-or-bugfix-name
    ```

4. **Make Changes**: Make your changes to the codebase.

5. **Commit Changes**: Commit your changes with a descriptive commit message:
    ```sh
    git add .
    git commit -m "Description of the feature or bugfix"
    ```

6. **Push Changes**: Push your changes to your forked repository:
    ```sh
    git push origin feature-or-bugfix-name
    ```

7. **Create a Pull Request**: Go to the original repository on GitHub and create a pull request from your forked repository. Provide a clear description of your changes and why they should be merged.