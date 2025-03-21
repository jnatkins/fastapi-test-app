# Basic FastAPI Application

A simple FastAPI application with a POST route and Braintrust tracing.

## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up Braintrust:
   - Copy the example environment file:
     ```
     cp .env.example .env
     ```
   - Edit the `.env` file and add your Braintrust API key:
     ```
     BRAINTRUST_API_KEY=your_actual_api_key_here
     ```
   - You can get your API key from [Braintrust Dashboard](https://www.braintrust.dev/).

## Running the Application

Start the application with Uvicorn:

```
cd fastapi_basic_app
python run.py
```

The application will be available at http://127.0.0.1:8000

## API Documentation

FastAPI automatically generates interactive API documentation:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Available Endpoints

- `GET /`: Root endpoint returning a welcome message
- `POST /items/`: Create a new item (with Braintrust tracing)
- `GET /items/{item_id}`: Get an item by ID

## Example Request

To create a new item, send a POST request to `/items/` with the following JSON body:

```json
{
  "name": "Sample Item",
  "description": "This is a sample item",
  "value": 42.0,
  "is_active": true
}
```

## Braintrust Tracing

This application uses the Braintrust SDK to trace the execution of the `create_item` function. 
The tracing will:

1. Capture the input data sent to the endpoint
2. Record the execution of the function
3. Capture the output response
4. Send the data to your Braintrust project dashboard

You can view the trace data and insights in your Braintrust dashboard at https://app.braintrust.dev. 