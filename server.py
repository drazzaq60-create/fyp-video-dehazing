"""
server.py

FastAPI server placeholder for cloud-based live video dehazing.
The DVD model and real-time processing will be added later.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "Server is running",
        "message": "DVD dehazing API placeholder"
    }
