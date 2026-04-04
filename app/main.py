from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="K8s Security Demo API",
    description="FastAPI microservice on hardened K8s cluster",
    version="1.0.0"
)

class Item(BaseModel):
    id: int
    name: str
    description: str

items_db: List[Item] = [
    Item(id=1, name="Widget A", description="Secured widget in K8s"),
    Item(id=2, name="Widget B", description="RBAC-controlled resource"),
    Item(id=3, name="Widget C", description="NetworkPolicy-protected item"),
]

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "namespace": "prod",
        "security": "restricted",
        "rbac": "enabled",
        "network_policy": "default-deny",
        "pod_security": "restricted"
    }

@app.get("/items", response_model=List[Item])
async def get_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = next((i for i in items_db if i.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
