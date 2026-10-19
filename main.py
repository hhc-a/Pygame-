from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "service": "Wordle API",
        "status": "running"
    }
    
@app.get("/health")
def health():
    return {"ok": True}

@app.get("/student")
def student():
    return {
        "student": "411200536",
        "week": 5,
        "completed": False
    }