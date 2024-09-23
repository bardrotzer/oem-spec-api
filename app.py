import uvicorn
from fastapi import FastAPI, File, UploadFile, Body

from services.vehicle_listing import get_vehicle_data

app = FastAPI()


@app.get("/")
async def root():
    return {"message": 'this is the root of the api'}

# this is where we post a models
# aka:
#   {
#    "model": "2022 Tesla Model S"
#   }
@app.post('/models')
async def models(model: str = Body(..., embed=True)):
    # read the image file
    prediction = get_vehicle_data(model)
    return prediction

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
