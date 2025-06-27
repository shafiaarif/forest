from .base import BaseRouter
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from db import SupabaseConnection
from sql.mutation.insert_content import InsertContent



class PostRoutes(BaseRouter):
    def __init__(self):
        super().__init__()
        self.router.add_api_route("/InsertContent", self.Insert_Content, methods=["POST"])
    

    class InsertContent(BaseModel):
        id: Optional[UUID] = None
        slug: str
        title_en: Optional[str] = None
        title_ur: Optional[str] = None
        content_en: Optional[str] = None
        content_ur: Optional[str] = None
        image_path: Optional[str] = None

    def Insert_Content(self, request:InsertContent):
        client = SupabaseConnection.get_client()
        mutation_obj = InsertContent(client)
        try:
            result = mutation_obj.run(request.model_dump())
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    


