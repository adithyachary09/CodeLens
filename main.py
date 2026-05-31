from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from analyzer import analyze_code_complexity

app = FastAPI(title="CodeLens API")

# Setup Rate Limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request validation model with 10,000 character hard limit
class AnalyzeRequest(BaseModel):
    code: str = Field(..., max_length=10000)
    language: str = "auto"

@app.post("/analyze")
@limiter.limit("5/minute")
async def analyze_endpoint(request: Request, payload: AnalyzeRequest):
    if not payload.code.strip():
        raise HTTPException(status_code=400, detail="Code input cannot be empty.")
        
    result = analyze_code_complexity(payload.code, payload.language)
    
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
        
    return result