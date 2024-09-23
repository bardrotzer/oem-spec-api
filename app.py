from fastapi import FastAPI, File, UploadFile, Body

from services.vehicle_listing import get_vehicle_data

app = FastAPI()


@app.get("/")
async def root():
    return {"message": 'this is the root of the api'}


@app.post('/models')
async def models(model: str = Body(..., embed=True)):
    # read the image file
    prediction = get_vehicle_data(model)
    return prediction