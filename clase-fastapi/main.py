from fastapi import FastAPI
from routers import users, productos

app = FastAPI()

app.include_router(users.router)
app.include_router(productos.router)

@app.get("/")
def read_root():
    mensaje = "Primer clase de FastAPI"
    return {"message": mensaje}
