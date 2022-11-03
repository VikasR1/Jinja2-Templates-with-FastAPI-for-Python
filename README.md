# Jinja2-Templates-with-FastAPI-for-Python

## This tutorial is for doing template inheritance and for creating a web application using FastAPI and jinja 2 templates.
- Steps1: - Install the prerequisites

  - •	Set up FastAPI app and create a virtual environment and activate it
  - •	Install FastAPI with commands pip install fastapi
  - •	Install uvicorn with command pip install uvicorn
  
## Steps2: - Setting a hello world API using FAST API
    - •	Create an app file using the command in terminal touch main.py
    - •	Import fast the requirements like fast api and uvicorn
    - •	import uvicorn
    - •	from fastapi import FastAPI
    
    
## Steps3: - Create an App instance
    - •	app = FastAPI()
    - •	@app.get('/')
    - •	def hello_world():
    - •	    return {'message':'hello'}
    
   
## Steps4: - Create a templates folder in the project directory
    - •	Create a templates folder in the same directory
    - •	We will keep HTML files in this template folder
    

## Steps5: - Start making use of this template
    - •	Go back to main.py file and install jinja2 template pip install Jinja2
    - •	Import the HTTP Responses and jinja2templates
    - •	from fastapi.responses import HTMLResponse
    - •	from fastapi.templating import Jinja2Templates
    - •	then create an instance of Jinja2 template passing in the templates directory we created earlier
    - •	app = FastAPI()
    - •	templates = Jinja2Templates(directory="templates")


## Steps6: - Add another root to render the template
  - •	add another root just like this
      - •	@app.get('/')
      - •	def hello_world():
      - •	    return {'message':'hello'}
      - •	# this root/ end point to render jinja2 template
      - •	@app.get("/items/{id}", response_class=HTMLResponse)
      - •	async def read_item(request: Request, id: str):
      - •	    return templates.TemplateResponse("item.html", {"request": request, "id": id})
      - •	Run the server to see the result by uvicorn main:app –reload


## Steps7: - Handle static files
    - •	Static files like css, js files
    - •	First, we need to install aiofiles using pip install aiofiles
    - •	Create a static folder in same directory, add css file and image in it 
    - •	Go to main.py and mount/ import static files there like this
        - •	from fastapi.staticfiles import StaticFiles
    - •	then create an instance to mount static files
          - •	app = FastAPI()
          - •	# for html templates
          - •	templates = Jinja2Templates(directory="templates")
          - •	# for static files
          - •	app.mount("/static", StaticFiles(directory="static"), name="static")
          
    - •	it will make static files available to use
    - •	finally, run the server to see your first app with template 
    - •	type this command in terminal uvicorn main:app –reload


