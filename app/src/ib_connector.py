from typing import Callable
from asyncio import TimeoutError
from functools import wraps
from ib_insync import IB, Contract, Trade, Order, Stock
from schemas import OrderData, StockData, OrderType
from loguru import logger


class IBConnectorError(Exception):
    pass


def connection_required(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        try:
            if not self._ib.isConnected():
                await self._ib.connectAsync('host.docker.internal', 7497, 0)

            return await func(self, *args, **kwargs)

        except (ConnectionError, ConnectionRefusedError, TimeoutError) as error:
            logger.debug(error)

            self._ib.disconnect()

            raise IBConnectorError(
                'Cannot connect to IB. Please check if the IB application is properly set up and running'
            )

    return wrapper


class IBConnector:
    def __init__(self):
        self._ib: IB = IB()
        self._ib.errorEvent += self._error_callback
        self._ib.connectedEvent += self._connected_callback
        self._ib.disconnectedEvent += self._disconnected_callback
        self._ib.orderStatusEvent += self._order_callback

    @connection_required
    async def submit_order(self, data: OrderData) -> None:
        contract = self._ib_stock(data.stock)
        order_id = self._ib.client.getReqId()
        ib_order = self._order_to_ib(data, order_id)

        self._ib.placeOrder(contract, ib_order)

    async def _error_callback(
        self, req_id: int, code: int, message: str, contract: Contract | None
    ) -> None:
        logger.debug(f'{req_id} {code} {message} {contract if contract else ""}')

    async def _connected_callback(self) -> None:
        logger.debug('IB connected')

    async def _disconnected_callback(self) -> None:
        logger.debug('IB disconnected')

    async def _order_callback(self, ib_trade: Trade) -> None:
        logger.debug(f'IB order changed: {ib_trade}')

    def _ib_stock(self, stock: StockData) -> Stock:
        return Stock(stock.symbol, f'SMART:{stock.exchange.value}', 'USD')

    def _order_to_ib(self, order: OrderData, order_id: int) -> Order:
        ib_order = Order()
        ib_order.orderId = order_id
        ib_order.action = order.side.value
        ib_order.orderType = order.type.value
        ib_order.totalQuantity = float(order.size)
        ib_order.tif = 'DAY'

        if order.type == OrderType.LIMIT:
            ib_order.lmtPrice = float(order.price)

        elif order.type == OrderType.STOP:
            ib_order.auxPrice = float(order.price)

        return ib_order
