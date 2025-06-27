from typing import Dict, Any
from sql import Mutation

class InsertContent(Mutation):
    """
    Insert a new application into the 'applications' table.
    Expects input_params with keys: candidate_id, job_id, resume_url, message
    """
    def get_mutation(self, input_params: Dict[str, Any]):
        data = {
            "slug": input_params["slug"],
            "title_en": input_params["title_en"],
            "title_ur": input_params["title_ur"],
            "content_en": input_params["content_en"],
            "content_ur": input_params["content_ur"],
            

        }
        return self.client.table("content").insert(data)
