import time

from plyer import notification
while True:
    time.sleep(3)
    notification.notify(
        title="Mesaj",
        message="Deneme mesajı",
        app_icon="indir.ico",
        timeout=3
    )

