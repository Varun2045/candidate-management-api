# Candidate Management API

A RESTful API built with FastAPI for managing job candidates through their application lifecycle.

## 🚀 Features

- **Create Candidates**: Add new candidates with name, email, skill, and application status
- **List Candidates**: Retrieve all candidates with optional status filtering
- **Update Status**: Update candidate application status (applied → interview → selected/rejected)
- **Data Validation**: Built-in email validation and status enum enforcement
- **Auto-generated IDs**: Unique UUIDs for each candidate

## 📋 API Endpoints

### POST /candidates
Create a new candidate.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "skill": "Python",
  "status": "applied"
}
```

**Response:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "John Doe",
  "email": "john@example.com",
  "skill": "Python",
  "status": "applied"
}
```

### GET /candidates
Get all candidates, optionally filtered by status.

**Query Parameters:**
- `status` (optional): Filter by status (`applied`, `interview`, `selected`, `rejected`)

**Response:**
```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "name": "John Doe",
    "email": "john@example.com",
    "skill": "Python",
    "status": "applied"
  }
]
```

### PUT /candidates/{id}/status
Update a candidate's status.

**Request Body:**
```json
{
  "status": "interview"
}
```

**Response:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "John Doe",
  "email": "john@example.com",
  "skill": "Python",
  "status": "interview"
}
```

## 🛠️ Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **UUID**: Unique identifier generation
- **Python 3.8+**: Core programming language

## 📦 Dependencies

- `fastapi==0.135.3`
- `pydantic==2.12.5`
- `email-validator==2.3.0`
- `uvicorn==0.42.0`

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd candidate_api
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the API

1. **Start the server**
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**
   - API Documentation: http://127.0.0.1:8000/docs
   - Interactive API: http://127.0.0.1:8000/redoc
   - Base URL: http://127.0.0.1:8000

## 📊 Status Flow

Candidates can move through the following status stages:

```
applied → interview → selected/rejected
```

**Valid Status Values:**
- `applied`: Candidate has submitted their application
- `interview`: Candidate is scheduled for or undergoing interviews
- `selected`: Candidate has been offered and accepted the position
- `rejected`: Candidate has been declined for the position

## 🧪 Testing the API

### Using curl

**Create a candidate:**
```bash
curl -X POST "http://127.0.0.1:8000/candidates" \
     -H "Content-Type: application/json" \
     -d '{"name": "Jane Smith", "email": "jane@example.com", "skill": "JavaScript", "status": "applied"}'
```

**Get all candidates:**
```bash
curl -X GET "http://127.0.0.1:8000/candidates"
```

**Filter by status:**
```bash
curl -X GET "http://127.0.0.1:8000/candidates?status=applied"
```

**Update candidate status:**
```bash
curl -X PUT "http://127.0.0.1:8000/candidates/{candidate_id}/status" \
     -H "Content-Type: application/json" \
     -d '{"status": "interview"}'
```

### Using Python requests

```python
import requests

# Create candidate
response = requests.post("http://127.0.0.1:8000/candidates", 
                        json={"name": "Alice Johnson", "email": "alice@example.com", 
                              "skill": "React", "status": "applied"})
print(response.json())

# Get all candidates
response = requests.get("http://127.0.0.1:8000/candidates")
print(response.json())
```

## 📝 Data Models

### CandidateCreate
- `name` (str): Candidate's full name
- `email` (EmailStr): Valid email address
- `skill` (str): Primary skill or technology
- `status` (StatusEnum): Application status

### CandidateStatusUpdate
- `status` (StatusEnum): New application status

### CandidateResponse
- `id` (str): Auto-generated UUID
- `name` (str): Candidate's full name
- `email` (EmailStr): Valid email address
- `skill` (str): Primary skill or technology
- `status` (StatusEnum): Application status

## 🔧 Configuration

The API runs with the following default settings:
- Host: `127.0.0.1`
- Port: `8000`
- Auto-reload: Enabled (for development)

To customize:
```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```


**Note**: This API uses an in-memory database for demonstration purposes. Data will be lost when the server restarts. For production use, integrate with a persistent database.
