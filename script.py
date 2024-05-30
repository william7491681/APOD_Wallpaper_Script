import requests
from dotenv import load_dotenv
import os
from PIL import Image
import datetime
import json

with open("userDefinedVariables.json", "r") as userDefinedVariables:
  userDefinedVariables = json.load(userDefinedVariables)
  monitorWidth = userDefinedVariables['MONITOR_WIDTH']
  monitorHeight = userDefinedVariables['MONITOR_HEIGHT']
  imageFolder = userDefinedVariables['IMAGE_FOLDER']

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

oneThirdWidth = monitorWidth//3
twoThirdsWidth = monitorWidth//3*2
oneThirdHeight = monitorHeight//3
twoThirdsHeight = monitorHeight//3*2

finalImg.paste(imgs[0], (0, 0))
finalImg.paste(imgs[1], (oneThirdWidth, 0))
finalImg.paste(imgs[2], (twoThirdsWidth, 0))

finalImg.paste(imgs[3], (0, oneThirdHeight))
finalImg.paste(imgs[4], (oneThirdWidth, oneThirdHeight))
finalImg.paste(imgs[5], (twoThirdsWidth, oneThirdHeight))

finalImg.paste(imgs[6], (0, twoThirdsHeight))
finalImg.paste(imgs[7], (oneThirdWidth, twoThirdsHeight))
finalImg.paste(imgs[8], (twoThirdsWidth, twoThirdsHeight))

if os.path.exists(f'{imageFolder}\collage.jpg'):
  os.remove(f'{imageFolder}\collage.jpg')
finalImg.save(f'{imageFolder}\collage.jpg')