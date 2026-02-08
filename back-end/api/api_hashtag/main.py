from fastapi import FastAPI

app = FastAPI()

import os

# caminho absoluto da pasta raiz do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# caminho da pasta routes
ROUTES_DIR = os.path.join(BASE_DIR, "routes")

# agora os imports funcionam
from routes.auth_routes import auth_router
from routes.order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)