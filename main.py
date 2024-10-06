import uvicorn
import sys

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from app.routes import loginRoute, forgotPasswordRoute, registerRoute, dashboardRoute
from app.routes import assetInfoRoute, vcRoute, coverianceRoute, expectedReturnRoute, rebalancingRoute
from app.config import productionConfig as productionConfig
from app.config import developmentConfig as developmentConfig
from pydantic import ValidationError
from app.utils.error import validation_exception_handler, http_exception_handler, global_exception_handler

def create_app():
    
    app = FastAPI()
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(dashboardRoute.router)
    app.include_router(assetInfoRoute.router)
    app.include_router(coverianceRoute.router)
    app.include_router(rebalancingRoute.router)
    app.include_router(expectedReturnRoute.router)
    app.include_router(loginRoute.router)
    app.include_router(forgotPasswordRoute.router)
    app.include_router(registerRoute.router)
    app.include_router(vcRoute.router)

    app.add_exception_handler(ValidationError, validation_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)
    
    # Allows CORS middleware
    origins = ["*"]
    
    # origins = [
    #     "frontend-app.yourdomain.com",
    #     "frontend-app2.yourdomain.com:7000"
    # ]
    
    # Setting Middleware`
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(
        SessionMiddleware,
        secret_key="afadeed7e5ae8b3c88855f11f24b54de2d8feaa1c0ed7fd0aaefa7143e03054a",
        session_cookie="roboadvisor",  # 세션 쿠키 이름
        max_age=1800,  # 세션 만료 시간 (초)
        same_site="strict",  # 쿠키 SameSite 속성
        https_only=True,  # HTTPS 전용 쿠키
    )

    return app

app = create_app()

if __name__ == "__main__":
    env = sys.argv[1] if len(sys.argv) > 2 else 'dev'
    if env == 'dev':
        app.config = developmentConfig
    elif env == 'prod':
        app.config = productionConfig
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)