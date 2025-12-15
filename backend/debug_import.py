import sys
import os
sys.path.append(os.getcwd())
try:
    from app.models import User
    print("Import successful")
except Exception as e:
    print(f"Import failed: {e}")
