from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(title="my first notification",message="u did it",timeout=3,toast=True)
        break