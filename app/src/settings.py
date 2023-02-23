import os

DEBUG = int(os.getenv('DEBUG', 0))

WEBHOOK_TOKEN = os.getenv('WEBHOOK_TOKEN')
if not WEBHOOK_TOKEN:
    exit('Please set WEBHOOK_TOKEN')
