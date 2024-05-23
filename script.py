import requests
from dotenv import load_dotenv
import os
from PIL import Image
import datetime
import ctypes

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
    img = img.resize((1920//3, 1080//3), Image.Resampling.LANCZOS)
    imgs.append(img)
  elif "hdurl" in i:
    img = Image.open(requests.get(i["hdurl"], stream=True).raw)
    img = img.resize((1920//3, 1080//3), Image.Resampling.LANCZOS)
    imgs.append(img)
  elif "url" in i:
    img = Image.open(requests.get(i["url"], stream=True).raw)
    img = img.resize((1920//3, 1080//3), Image.Resampling.LANCZOS)
    imgs.append(img)
  else:
    imgs.append(Image.new('RGB', (1920//3, 1080//3)))

finalImg = Image.new('RGB', (1920, 1080))
finalImg.paste(imgs[0], (0, 0))
finalImg.paste(imgs[1], (640, 0))
finalImg.paste(imgs[2], (1280, 0))

finalImg.paste(imgs[3], (0, 360))
finalImg.paste(imgs[4], (640, 360))
finalImg.paste(imgs[5], (1280, 360))

finalImg.paste(imgs[6], (0, 720))
finalImg.paste(imgs[7], (640, 720))
finalImg.paste(imgs[8], (1280, 720))

savePath = r"C:\Users\willi\Pictures\APOD Pics\collage.jpg"
if os.path.exists(savePath):
  os.remove(savePath)
finalImg.save(savePath)
ctypes.windll.user32.SystemParametersInfoW(20, 0, savePath , 0)