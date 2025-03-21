from fastapi import FastAPI, HTTPException, Body, APIRouter
from typing import Dict, Any
from pydantic import BaseModel
from braintrust import traced, start_span, init_logger, current_span
from .braintrust_config import initialize_braintrust

# Initialize Braintrust SDK
initialize_braintrust()
logger = init_logger(project="Issue Repros")

# Create FastAPI app instance
app = FastAPI(
    title="Basic FastAPI App",
    description="A simple FastAPI application with a POST route",
    version="0.1.0"
)

router = APIRouter(prefix="/test")

# Define request model
class ItemRequest(BaseModel):
    name: str
    description: str = None
    value: float
    is_active: bool = True

# Define response model
class ItemResponse(BaseModel):
    id: int
    name: str
    description: str = None
    value: float
    is_active: bool
    
# In-memory storage for demo purposes
items_db = {}
item_counter = 0

@traced
@app.get("/")
def read_root():
    """Root endpoint returning a welcome message"""
    with logger.start_span(name="read_root_custom"):
        current_span().end()
    return {"message": "Welcome to the Basic FastAPI App"}

@app.post("/items/", response_model=ItemResponse)
@traced
def create_item(item: ItemRequest):
    """
    Create a new item
    
    This endpoint accepts a POST request with item data and returns the created item
    with an assigned ID.
    """
    global item_counter
    
    # Increment the counter to generate a unique ID
    item_counter += 1
    
    # Create the new item with an ID
    new_item = {
        "id": item_counter,
        "name": item.name,
        "description": item.description,
        "value": item.value,
        "is_active": item.is_active
    }
    
    # Store the item in our "database"
    items_db[item_counter] = new_item
    
    # Return the created item
    return new_item

@traced
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Get an item by its ID
    
    This endpoint returns an item based on its ID or raises a 404 error if not found.
    """
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return items_db[item_id]

# Add more endpoints as needed 