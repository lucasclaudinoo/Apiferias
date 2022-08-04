from imp import reload
from fastapi import FastAPI
import uvicorn 
from server.routes.user import router as UserRouter

app = FastAPI()

app.include_router(UserRouter, tags=["User"], prefix="/user")

if __name__ == '__main__':
    uvicorn.run (app, host='127.0.0.1', port=8005, debug=True)
    print("running")