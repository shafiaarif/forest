from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.post_points import PostRoutes
from api.get_points import GetRoutes
# description only to distinguish
app = FastAPI(
    title="Backend API",
    description="This is the backend API for my QRscan project")

# origins allowed
origins = [
    "http://localhost:8000",
]

# Add CORSMiddleware to allow requests from allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,
    allow_methods=["*"],    # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],    # Allows all headers
)

#registering routes
app.include_router(PostRoutes().get_router())
app.include_router(GetRoutes().get_router())