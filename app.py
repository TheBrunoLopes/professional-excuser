from random import randint
import uvicorn as uvicorn
from fastapi import FastAPI, Request
from excuses import excuses
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    excuse = excuses[randint(0, len(excuses) - 1)]
    return templates.TemplateResponse("index.html", {"request": request, "excuse": excuse})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
