# CRUD FastAPI Application

This is a simple CRUD (Create, Read, Update, Delete) application built using FastAPI. The application provides a RESTful API for managing resources and demonstrates the use of FastAPI's features for building efficient and scalable web applications.

## Features

- **FastAPI**: High-performance Python framework for building APIs.
- **CRUD Operations**: Create, Read, Update, and Delete functionality for managing resources.
- **Validation**: Input validation using Pydantic models.
- **Interactive API Documentation**: Automatically generated Swagger UI and ReDoc.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn (ASGI server)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/valantoni/crud-fastapi.git
    cd crud-fastapi
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

2. Open your browser and navigate to:
    - Swagger UI: `http://127.0.0.1:8000/docs`
    - ReDoc: `http://127.0.0.1:8000/redoc`

## Project Structure

```
crud-fastapi/
app/
├── crud.py          # crud functions
├── models.py        # Pydantic models for data validation
├── routes.py        # API routes

database.py      # Database connection and operations
requirements.txt # Project dependencies
README.md        # Project documentation
main.py          # Endpoints
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Contact

For any inquiries, please contact [Toni Dev](mailto:classtonidev@gmail.com).  