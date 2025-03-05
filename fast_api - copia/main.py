from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
def get_info():
    return {
        "name": "FastAPI parcial One",
        "description": "This is a sample FastAPI project.",
        "author": "Natalia Sabogal and Samuel Valencia",
        "Semester": "4",
        "Year": "2025-1",


    }