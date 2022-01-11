import os
import platform
from plyer import notification


plt = platform.system()


def send(title: str, message: str) -> None:
    if plt == "Darwin":
        command = "osascript -e 'display notification " + \
                  f"\"{message}\" with title \"{title}\"' "
        os.system(command)
    elif plt == "Linux":
        command = f"notify-send \"{title}\" \"{message}\""
        os.system(command)
    elif plt == "Windows":
        notification.notify(
            title=title,
            message=message,
            app_icon=''
        )
