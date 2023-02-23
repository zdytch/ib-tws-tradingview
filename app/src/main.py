from loguru import logger
from settings import DEBUG

logger.add(
    'logs/{time}.log',
    format='{time} {level} {message}',
    level='DEBUG',
    rotation='100 MB',
    retention='14 days',
    compression='zip',
)

if DEBUG:
    import debugpy

    debugpy.listen(('0.0.0.0', 5678))

    if DEBUG == 2:
        debugpy.wait_for_client()


if __name__ == '__main__':
    # Start here
    ...
