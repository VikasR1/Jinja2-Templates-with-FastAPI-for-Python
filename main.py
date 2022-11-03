'''
''
prerequisite

pip install fastapi
pip install uvicorn
pip install Jinja2
pip install aiofiles
''
run the app with below command

uvicorn main:app --reload
'''
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

# for html templates
templates = Jinja2Templates(directory="templates")
# for static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
def hello_world():
    return {'message':'hello'}


# this root/ end point to render jinja2 template
@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})