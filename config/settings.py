from dotenv import load_dotenv
import os

# Load .env.local
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env.local'))

SUPABASE_CONFIG = {
    "url": os.getenv("SUPABASE_URL"),
    "anon_key": os.getenv("SUPABASE_ANON_KEY"),
    "service_role_key": os.getenv("SUPABASE_SERVICE_ROLE_KEY"),
    "database_url": os.getenv("DATABASE_URL"),
}
