import uvicorn
from typing import Optional
from fastapi import FastAPI, Response, status, Request , HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/api/premuim_payement_gateway/",status_code=200)
async def premuim_payement(request:Request):
    # raise HTTPException(status_code=400, detail="Not valid transaction")
    response = status.HTTP_400_BAD_REQUEST
    return Response("Not", status_code=400)

@app.post("/api/expensive_payement_gateway/",status_code=200)
async def expensive_payement(request:Request):
    # json_param = await request.json()
    # print(json_param)
    response = status.HTTP_200_OK
    return {'response':response}

@app.post("/api/cheap_payement_gateway/",status_code=200)
async def cheap_payement(request:Request):
    # json_param = await request.json()
    response = status.HTTP_200_OK
    return {'response':response}