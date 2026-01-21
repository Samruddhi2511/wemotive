import sys

print("Hello from virtual environment!")
print("Python executable:", sys.executable)
##################################################

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI with Uvicorn"}
