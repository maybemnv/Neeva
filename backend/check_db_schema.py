import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect

# Load environment variables
load_dotenv()
database_url = os.getenv("DATABASE_URL")

print(f"DEBUG: DATABASE_URL from .env: {database_url}")

if not database_url:
    print("ERROR: DATABASE_URL not found in .env")
    exit(1)

try:
    engine = create_engine(database_url)
    inspector = inspect(engine)
    
    if 'users' in inspector.get_table_names():
        print("Table 'users' exists.")
        columns = inspector.get_columns('users')
        column_names = [col['name'] for col in columns]
        print(f"Columns: {column_names}")
        
        if 'onboarding_completed' in column_names:
            print("SUCCESS: 'onboarding_completed' column found.")
        else:
            print("FAILURE: 'onboarding_completed' column NOT found.")
            
        if 'onboarding_data' in column_names:
             print("SUCCESS: 'onboarding_data' column found.")
        else:
             print("FAILURE: 'onboarding_data' column NOT found.")
    else:
        print("FAILURE: Table 'users' does not exist.")

except Exception as e:
    print(f"An error occurred: {e}")
