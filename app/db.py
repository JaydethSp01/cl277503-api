import os
import psycopg

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    conn = psycopg.connect(DATABASE_URL)
else:
    # Fallback to in-memory storage for development
    conn = None