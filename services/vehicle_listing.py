from pydantic import BaseModel, Field
from openai import OpenAI
from typing import List, Optional
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
# api_key = Secret.from_env_var("OPENAI_API_KEY")

# user_description = "Arne Jacobsen 3207 armstole er nypolstrede og lavet med brandyfarvet anilinlæder. Sædehøjden er 44 cm, og læderet har en naturlig og åndbar narv, der giver optimal siddekomfort."
# image_uuid = 'c51ba230-2702-47bb-a39e-c59b3bc696fe'

# instanciate the client
client = OpenAI(
  api_key = api_key
)

# set up some headers for the transport
headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}


class CarData(BaseModel):
    OEM: str
    Model: str
    Car_body_type: str
    Variant: str
    Fuel_type: str
    Antall_seter: int
    Battery_capacity: Optional[float]
    Range_WLTP: Optional[int]
    Acceleration_0_100_kmh: Optional[float]
    Charging_speed: Optional[float]
    Max_horsepower: Optional[int]
    Fuel_consumption: Optional[float]
    Width: int
    Height: int
    Length: int
    Cargo_capacity: Optional[float]
    Max_tow_weight: Optional[float]
    Vehicle_weight: Optional[float]
    Apple_CarPlay_Android_Auto: str


class CarDataList(BaseModel):
  trims: List[CarData]

# start building something new
def get_vehicle_data(model: str):
  # Create the completion using the OpenAi api
  completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini-2024-07-18",
    messages=[
      {
        "role": "system",
        "content": get_system_message()
      },
      {
        "role": "user",
        "content": [
          {"type": "text", "text": get_user_message(model)},
         
        ],
      }
    ],
    response_format=CarDataList
  )
  message = completion.choices[0].message

  if message.parsed:

  #  insert_tags(id, message.parsed.tags, message.parsed.description)
   return message.parsed

  else:
    print(message.refusal)


def get_system_message():
  msg = """This GPT is designed to help users gather detailed car specifications for Swedish websites. 
    It follows a specific search order: 
    first the OEM's Swedish website, 
    then the OEM's main international website, 
    and finally other external websites. 
    For EVs, it relies on ev-database.org as a reliable source. 
    The GPT takes a brand or model name and looks for and identifies the various trims for this model
    It uses the following template to gather and present the data 
    OEM: the brand name (Hyundai, Ford, Toyota), 
    Model: the name of the model (i30, Explorer, Rav 4),
    Car body type (Car_body_type): the type of car body (SUV, Sedan, Hatchback),
    Variant: the drivetrain variant of this model (Electric, classic, Plug-in hybrid),
    Fuel type: (Fuel_type) the type of fuel the car uses (Gasoline, Diesel, Electric),
    Antall seter: (Antall_seter) the number of seats in the car,
    Battery capacity (if applicable): (Battery_capacity) the capacity of the battery in kWh,
    Range (WTLP): (Range_WLTP) the range of the car in kilometers
    Acceleration 0 - 100 kmh: (Acceleration_0_100_kmh) the acceleration of the car from 0 to 100 km/h in seconds,
    Charging speed (if applicable): (Charging_speed) The speed of charging (kW/h),
    Max horsepower: (Max_horsepower) The max torque horsepower of the car,
    Fuel consumption (if applicable): (Fuel_consumption) the fuel consumption of the car in liters per 100 km,
    Width: the width of the car in mm,
    Height: the height of the car in mm,
    Length: the length of the car in mm,
    Cargo capacity: (Cargo_capacity) the cargo capacity of the car in liters,
    Max tow weight: (Max_tow_weight) the maximum weight the car can tow in kg,
    Vehicle weight: (Vehicle_weight) the weight of the car in kg,
    Apple CarPlay and Android Auto: (Apple_CarPlay_Android_Auto) the availability of Apple CarPlay or Android Auto in the car
    If any data points are uncertain, it will state so. The GPT prioritizes accuracy and thoroughness over speed."""
  
  return msg

def get_user_message(model):
  msg = f"""Find specs for {model} in Sweden."""
  return msg   
