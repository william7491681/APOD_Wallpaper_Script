# APOD_Wallpaper_Script
A script that takes the last 9 pictures of the day from NASA's APOD API, turns them into a 3x3 collage, and sets the collage as the wallpaper on a Windows 10 computer.

## NASA API KEY
Go to https://api.nasa.gov/ to obtain an api key. The process is very simple. If you don't want to though, you can use the key `DEMO_KEY` in lieu of an actual api key.

e.g.
```
params = {
  "api_key": "DEMO_KEY",
  "start_date": eightDaysAgo,
  "end_date": today,
  "thumbs": True
}
```
At this point in time, the demo keys are rate limited to 30 requests per IP address per hour, and 50 requests per IP address per day.

## Current wallpaper on May 23, 2023
![image](https://github.com/william7491681/APOD_Wallpaper_Script/assets/62858610/1fe1cefa-b2f7-48f8-aa12-bdabab1024dd)

## How to get Windows Task Scheduler to run this script automatically
Task Scheduler was a pain to deal with in regards to the command `ctypes.windll.user32.SystemParametersInfoW(20, 0, savePath , 0)`. It seemed that everything would work except for that last line, which actually changes the wallpaper in Windows.
I eventually managed to get it working as intended, so for the sake of posterity I'll leave my specific configuration below:
* Open Task Scheduler and click the `Create Task` button
* On the `General` tab:
  * Click the `Change User or Group` button and type in `administrators` in the bottom text box, then click the `Check Names` button and hit ok.
  * Change the `Configure For` dropdown select to the Windows 10 option
* On the `Triggers` tab:
  * Create whatever triggers you want. For me, I am triggering it daily at 12:00PM, and at log on.
* On the `Actions` tab:
  * Click the new button, and select `Start a Program` as the action from the dropdown menu at the top.
  * In the `Program/script` section, enter the absolute path to the .bat file included in this repo (on my machine it is `C:\Users\willi\Documents\coding_projects\APOD_Wallpaper_Script\script.bat`)
* Troubleshooting:
  * If the script is not working for you, try the following:
    * On the `Conditions` tab, uncheck the box that says `Start the task only if the computer is on AC power`. If on a laptop, this may be the reason why the script fails to run.
    * On the `Actions` tab, edit the action that was set earlier to include the path to the folder containing the script in the `Start in` parameter (e.g. `C:\Users\willi\Documents\coding_projects\APOD_Wallpaper_Script`)