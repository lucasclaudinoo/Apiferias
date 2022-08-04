from fastapi import FastAPI
import uvicorn 
from server.routes.user import router as UserRouter

app = FastAPI()

app.include_router(UserRouter, tags=["User"], prefix="/user")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8005, debug=True)
