# APOD_Wallpaper_Script
A script that takes the last 9 pictures of the day from NASA's APOD API, turns them into a 3x3 collage, and sets the collage as the lock screen and wallpaper on a Windows 10 computer.

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

## Current lock screen/wallpaper on May 23, 2023
![image](https://github.com/william7491681/APOD_Wallpaper_Script/assets/62858610/1fe1cefa-b2f7-48f8-aa12-bdabab1024dd)

## How to get Windows Task Scheduler to run this script automatically
Windows was a pain to deal with in general. I tried many different ways of getting the script to run automatically, and landed on this solution. For the sake of posterity I'll leave my specific configuration below:
* Open Task Scheduler and click the `Create Task` button
* On the `General` tab:
  * Click the `Change User or Group` button and type in your user account name in the bottom text box, then click the `Check Names` button and hit ok.
  * Select the radio button for only running the task when the user is logged in
* On the `Triggers` tab:
  * Create whatever triggers you want. For me, I am triggering it daily at 6:00PM.
* On the `Actions` tab:
  * Click the new button, and select `Start a Program` as the action from the dropdown menu at the top.
  * In the `Program/script` section, enter `powershell`
  * In the `Add Arguments` section, enter `-File` and then the path to the powershell script included in this repo (on my machine this is
  `-File C:\Users\willi\Documents\coding_projects\APOD_Wallpaper_Script\runScript.ps1`)
* If the script is not working for you, try the following:
  * Firstly, ensure that you did not make any changes other than the ones listed above
  * On the `Conditions` tab, uncheck the box that says `Start the task only if the computer is on AC power`. If on a laptop, this may be the reason why the script fails to run.