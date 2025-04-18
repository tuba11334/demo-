from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Full Stack FastAPI App</title>
    </head>
    <body>
        <h1>Welcome to the Full Stack FastAPI App</h1>
        <p>This is a simple full stack Python application using FastAPI.</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/api/data", response_class=JSONResponse)
async def get_data():
    return {"message": "Hello from the FastAPI API!"}
