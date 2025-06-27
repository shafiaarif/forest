from fastapi import HTTPException, Query as FastAPIQuery
# from db import SupabaseConnection
# from sql.query import GetUserByEmailAndRole, GetUserById, GetJobById, GetApplicationById, GetAllJobs, GetAllUsersWithDetails
from .base import BaseRouter


class GetRoutes(BaseRouter):
    def __init__(self):
        super().__init__()
        pass
