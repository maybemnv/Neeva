import sys
import os
from sqlalchemy.orm import Session

# Add the current directory to sys.path to make app importable
sys.path.append(os.getcwd())

try:
    from app.core.database import get_db, engine
    print("Successfully imported get_db and engine.")
    
    # Try to connect
    with engine.connect() as connection:
        print("Successfully connected to the database via engine.")
        
    # Try to get a session
    db_gen = get_db()
    db = next(db_gen)
    print("Successfully created a database session.")
    
    # Try a simple query
    from sqlalchemy import text
    result = db.execute(text("SELECT 1"))
    print(f"Query result: {result.scalar()}")
    
    db.close()
    print("Connection test passed.")

except Exception as e:
    print(f"Connection test failed: {e}")
    import traceback
    traceback.print_exc()
