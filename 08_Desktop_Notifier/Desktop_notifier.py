import time
from plyer import notification

while True:
    notification.notify(
        title='*** Take Rest ***',
        message='Take rest baby its important for you.......',
        timeout=5
    )
    time.sleep(10)

