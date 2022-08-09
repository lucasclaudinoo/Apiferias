from fastapi import FastAPI
import uvicorn 
from server.routes.user import router as UserRouter
from server.routes.admin import router as AdminRouter
from server.routes.ferias import router as FeriasRouter


app = FastAPI()

app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(AdminRouter, tags=["Admin"], prefix="/admin")
app.include_router(FeriasRouter, tags=["Ferias"], prefix="/ferias")


if __name__ == '__main__':
    uvicorn.run("app:app", port=8080, reload=True, access_log=False)
