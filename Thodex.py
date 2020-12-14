import hashlib
import requests
import time
import websocket
import urllib.parse
import json


class ThodexClient:
    API_SERVER = 'https://api.thodex.com/{}'
    SOCKET_SERVER = 'wss://wspub.thodex.com:443'
    SOCKET_SUBSCRIBE_TYPES = ['deals', 'price', 'state']

    def __init__(self, *args):
        if len(args) == 2:
            self.api_key = args[0]
            self.api_secret = args[1]
        self.__subscribes = self.SOCKET_SUBSCRIBE_TYPES

    def get_subscribes(self):
        return self.__subscribes

    def set_subscribes(self, subscribes: list):
        self.__subscribes = subscribes

    def server_time(self):
        return self.execute({'url': 'v1/public/time'})

    def markets(self):
        return self.execute({'url': 'v1/public/markets'})

    def market_status(self, market: str):
        return self.execute({
            'url': 'v1/public/market-status',
            'payload': {
                'market': market
            }
        })

    def market_summary(self):
        return self.execute({
            'url': 'v1/public/market-summary',
        })

    def market_history(self, market: str, last_id: int = 0):
        return self.execute({
            'url': 'v1/public/market-history',
            'payload': {
                'market': market,
                'last_id': last_id
            }

        })

    def order_depth(self, market: str, limit: int = 0):
        return self.execute({
            'url': 'v1/public/order-depth',
            'payload': {
                'market': market,
                'limit': limit
            }
        })

    def get_open_orders(self, market: str, offset: int = 0, limit: int = 0):
        return self.execute({
            'url': 'v1/market/open-orders',
            'payload': {
                'market': market,
                'offset': offset,
                'limit': limit
            }
        }, True)

    def get_order_history(self, market: str, offset: int = 0, limit: int = 0):
        payload = {'market': market}
        if offset:
            payload['offset'] = offset
        if limit:
            payload['limit'] = limit
        return self.execute({
            'url': 'v1/market/order-history',
            'payload': payload
        }, True)

    def buy_limit(self, market: str, price: float, amount: float):
        """
            amount: amount must be STOCK
        """
        return self.execute({
            'url': 'v1/market/buy-limit',
            'payload': {
                'market': market,
                'amount': amount,
                'price': price
            }
        }, True, True)

    def buy_market(self, market: str, amount: float):
        """
            amount: amount must be MONEY
        """
        return self.execute({
            'url': 'v1/market/buy',
            'payload': {
                'market': market,
                'amount': amount,
            }
        }, True, True)

    def sell_limit(self, market: str, price: float, amount: float):
        """
            amount: amount must be STOCK
        """
        return self.execute({
            'url': 'v1/market/sell-limit',
            'payload': {
                'market': market,
                'amount': amount,
                'price': price
            }
        }, True, True)

    def sell_market(self, market: str, amount: float):
        """
            amount: amount must be STOCK
        """
        return self.execute({
            'url': 'v1/market/sell',
            'payload': {
                'market': market,
                'amount': amount,
            }
        }, True, True)

    def cancel_order(self, market: str, order_id: int):
        return self.execute({
            'url': 'v1/market/cancel',
            'payload': {
                'market': market,
                'order_id': order_id,
            }
        }, True, True)

    def get_balance(self, assets: str = ''):
        payload = dict()
        if assets:
            payload['assets'] = assets
        return self.execute({
            'url': 'v1/account/balance',
            'payload': payload
        }, True)

    def execute(self, request, auth=False, post=False):
        headers = {'User-Agent': 'Thodex/Python'}
        try:
            payload = request['payload']
        except:
            payload = dict()

        if auth:
            payload['tonce'] = int(time.time())
            payload['apikey'] = self.api_key
            headers['Authorization'] = self.encode(payload)

        if post:
            response = requests.post(self.API_SERVER.format(request['url']), headers=headers, data=payload)
        else:
            response = requests.get(self.API_SERVER.format(request['url']), headers=headers, params=payload)
        return response.json()

    def encode(self, payload):
        params = dict()
        for key in sorted(payload):
            params[key] = payload[key]
        params['secret'] = self.api_secret
        return hashlib.sha256(urllib.parse.urlencode(params).encode()).hexdigest()

    def socket_reader(self, markets: list = [], subscribe_types: list = []):
        if len(subscribe_types) > 0:
            self.set_subscribes(subscribe_types)

        ws = websocket.WebSocketApp(self.SOCKET_SERVER, on_message=self.on_message)
        ws.on_open = lambda ws: self.on_open(self, ws, markets)
        ws.run_forever()

    @staticmethod
    def on_open(this: object, ws, markets: list):
        ws.send(json.dumps({'method': 'state.unsubscribe', 'params': [], 'id': 0}))

        for subscribe in this.get_subscribes():
            if subscribe in this.SOCKET_SUBSCRIBE_TYPES:
                subscribe_data = {'method': "{}.subscribe".format(subscribe), 'params': markets, 'id': 0}
                ws.send(json.dumps(subscribe_data))
