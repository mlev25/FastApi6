import os

from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from routers import users, auth

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

# # Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000",
]

# Allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router,  prefix="/auth",  tags=["Auth"])

@app.get("/")
def read_root():
    
    for route in app.routes:
        print(f"{route.path} → {route.name}")
    return {"message": "Welcome to the FastAPI backend!"}
