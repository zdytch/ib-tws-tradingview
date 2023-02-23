import uvicorn
from fastapi import FastAPI, HTTPException
from schemas import TVWebhookData
from logic import handle_webhook
from loguru import logger
from settings import WEBHOOK_TOKEN, DEBUG

_kwargs = {} if DEBUG else {'openapi_url': None, 'docs_url': None, 'redoc_url': None}
_app = FastAPI(**_kwargs)


@_app.post('/webhook')
async def tradingview_webhook(schema: TVWebhookData):
    if schema.token == WEBHOOK_TOKEN:
        await handle_webhook(schema)

    else:
        logger.info('Wrong webhook token')

        raise HTTPException(status_code=401)


def run():
    uvicorn.run(_app, host='0.0.0.0')
