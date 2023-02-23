from schemas import TVWebhookData, OrderData, StockData, OrderType, Side
from ib_connector import IBConnector, IBConnectorError
from loguru import logger

_ibc = IBConnector()


async def handle_webhook(data: TVWebhookData) -> None:
    logger.debug(f'Received data from webhook: {data}')

    try:
        stock = StockData(symbol=data.symbol, exchange=data.exchange)
        order = OrderData(stock=stock, side=Side.BUY, type=OrderType.MARKET, size=1)

        await _ibc.submit_order(order)

    except IBConnectorError as error:
        logger.error(error)
