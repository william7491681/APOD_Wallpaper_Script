from screeninfo import get_monitors # it uses poetry as a sub package and needs to be installed since it is an external lib
from pathlib import Path

for monitor in get_monitors:
    if monitor.is_primary:
        width = monitor.width
        height = monitor.height
        path = Path("C:\\Users\\willi\\Pictures\\APOD Pics\\collage.jpg"")

monitorWidth = width
monitorHeight = height
fileSavePath = path