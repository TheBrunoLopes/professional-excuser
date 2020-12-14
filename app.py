from random import randint
import uvicorn as uvicorn
from fastapi import FastAPI
from excuses import excuses

app = FastAPI()


@app.get("/")
def read_root():
    excuse = excuses[randint(0, len(excuses))]
    return f"Excuse: {excuse}"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
