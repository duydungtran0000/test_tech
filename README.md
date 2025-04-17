## 🧪 Technical Test
Developed in Python 3 using the FastAPI framework.

### 🚀 How to Run

#### Create and activate a virtual environment
```
# Create the virtual environment
python3 -m venv env

# Activate it
source env/bin/activate        # On Linux/macOS
# OR
env\Scripts\activate           # On Windows
```

#### Install dependencies
```
pip install -r requirements.txt
```

#### Run the FastAPI app

```
uvicorn app.main:app --reload
```

### 🌐 How to Access the API
Once the server is running, open your browser and go to:
Swagger UI (API documentation): http://localhost:8000/docs
ReDoc (alternative documentation): http://localhost:8000/redoc