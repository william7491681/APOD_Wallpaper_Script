import requests
from dotenv import load_dotenv
import os
from PIL import Image
import datetime
import ctypes
import json

with open("userDefinedVariables.json", "r") as userDefinedVariables:
  userDefinedVariables = json.load(userDefinedVariables)
  monitorWidth = userDefinedVariables['MONITOR_WIDTH']
  monitorHeight = userDefinedVariables['MONITOR_HEIGHT']
  fileSavePath = userDefinedVariables['FILE_SAVE_PATH']

today = datetime.datetime.now().strftime("%Y-%m-%d").replace("/", "-")
eightDaysAgo = (datetime.datetime.now() - datetime.timedelta(days=8)).strftime("%Y-%m-%d").replace("/", "-")

url = "https://api.nasa.gov/planetary/apod"
load_dotenv()
api_key = os.getenv("NASA_API_KEY")

params = {
  "api_key": api_key,
  "start_date": eightDaysAgo,
  "end_date": today,
  "thumbs": True
}

response = requests.get(url, params=params)
response: dict = response.json()

imgs = []
for i in response:
  if "thumbnail_url" in i:
    img = Image.open(requests.get(i["thumbnail_url"], stream=True).raw)
    img = img.resize((monitorWidth//3, monitorHeight//3), Image.Resampling.LANCZOS)
    imgs.append(img)
  elif "hdurl" in i:
    img = Image.open(requests.get(i["hdurl"], stream=True).raw)
    img = img.resize((monitorWidth//3, monitorHeight//3), Image.Resampling.LANCZOS)
    imgs.append(img)
  elif "url" in i:
    img = Image.open(requests.get(i["url"], stream=True).raw)
    img = img.resize((monitorWidth//3, monitorHeight//3), Image.Resampling.LANCZOS)
    imgs.append(img)
  else:
    imgs.append(Image.new('RGB', (monitorWidth//3, monitorHeight//3)))

finalImg = Image.new('RGB', (monitorWidth, monitorHeight))
finalImg.paste(imgs[0], (0, 0))
finalImg.paste(imgs[1], (640, 0))
finalImg.paste(imgs[2], (1280, 0))

finalImg.paste(imgs[3], (0, 360))
finalImg.paste(imgs[4], (640, 360))
finalImg.paste(imgs[5], (1280, 360))

finalImg.paste(imgs[6], (0, 720))
finalImg.paste(imgs[7], (640, 720))
finalImg.paste(imgs[8], (1280, 720))

if os.path.exists(fileSavePath):
  os.remove(fileSavePath)
finalImg.save(fileSavePath)
ctypes.windll.user32.SystemParametersInfoW(20, 0, fileSavePath , 0)