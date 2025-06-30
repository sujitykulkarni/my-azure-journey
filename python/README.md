# FastAPI Greet API

## Requirements
- Python 3.12

## Setup
1. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API
Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```

## Usage
Visit [http://localhost:8000/greet](http://localhost:8000/greet) or use:
```bash
curl "http://localhost:8000/greet?name=YourName"
```

You should receive a JSON response like:
```json
{"message": "Hello, YourName!"}
``` 