from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import traceback
import logging

logger = logging.getLogger(__name__)

class ErrorLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            print(f"\n{'='*60}")
            print(f"REQUEST: {request.method} {request.url.path}")
            print(f"{'='*60}")
            
            response = await call_next(request)
            
            print(f"RESPONSE STATUS: {response.status_code}")
            print(f"{'='*60}\n")
            
            return response
        except Exception as e:
            print(f"\n{'!'*60}")
            print(f"MIDDLEWARE CAUGHT EXCEPTION!")
            print(f"Error type: {type(e).__name__}")
            print(f"Error message: {str(e)}")
            print(f"Traceback:")
            traceback.print_exc()
            print(f"{'!'*60}\n")
            
            # Write to file
            with open("middleware_error.log", "w") as f:
                f.write(f"Error: {str(e)}\n")
                f.write(f"Error type: {type(e).__name__}\n")
                traceback.print_exc(file=f)
            
            raise
