from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import List, Optional
import uuid

app = FastAPI(title="Candidate Management API")

# Define the allowed statuses for validation
class StatusEnum(str, Enum):
    applied = "applied"
    interview = "interview"
    selected = "selected"
    rejected = "rejected"

# Model for creating a candidate (validates incoming data)
class CandidateCreate(BaseModel):
    name: str
    email: EmailStr  # Automatically ensures the email is valid
    skill: str
    status: StatusEnum  # Ensures status is one of the 4 allowed options

# Model for updating the status
class CandidateStatusUpdate(BaseModel):
    status: StatusEnum

# Model for returning a candidate (includes the generated ID)
class CandidateResponse(CandidateCreate):
    id: str

# In-memory "database" (a simple list for this exercise)
candidates_db = []

# 1. Create Candidate
@app.post("/candidates", response_model=CandidateResponse)
def create_candidate(candidate: CandidateCreate):
    new_candidate = candidate.model_dump() # Convert Pydantic model to dictionary
    new_candidate["id"] = str(uuid.uuid4()) # Generate a unique ID
    candidates_db.append(new_candidate)
    return new_candidate

# 2. Get All Candidates
@app.get("/candidates", response_model=List[CandidateResponse])
def get_candidates(status: Optional[StatusEnum] = Query(None, description="Filter by status")):
    # Optional: support filtering by status (query param)
    if status:
        filtered = [c for c in candidates_db if c["status"] == status]
        return filtered
    # Return list of all candidates
    return candidates_db

# 3. Update Candidate Status
@app.put("/candidates/{id}/status", response_model=CandidateResponse)
def update_candidate_status(id: str, status_update: CandidateStatusUpdate):
    for candidate in candidates_db:
        if candidate["id"] == id:
            candidate["status"] = status_update.status
            return candidate
    raise HTTPException(status_code=404, detail="Candidate not found")