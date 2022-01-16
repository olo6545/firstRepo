from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
import uvicorn

app = FastAPI()
system = os.uname()



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/first")
async def good_function():
    html = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(html)


@app.get("/system")
async def systeminfo():
    return {
            "osname": system}


uvicorn.run(app)