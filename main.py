from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
import uvicorn

app = FastAPI()
system = os.uname()

products = {
    "XD-12" : "Klawiatura FURY",
    "MOUSE-1" : "Myszka USB",
    "CPU-0" : "PRocesor"
}

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

@app.get("/product/{product_id}")
async def product_info(product_id: str):
    if product_id in products:
        opis = products[product_id]
    else:
        opis = f"Niestety nie ma towaru ({product_id})"
    return{
        "Podano": product_id,
        "Opis": opis
    }


uvicorn.run(app)

