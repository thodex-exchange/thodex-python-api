import json
from Thodex import ThodexClient


class ThodexSocketMessage(ThodexClient):
    @staticmethod
    def on_message(ws, message: str):
        message = json.loads(message)
        if message['method']:
            message['method'] = message['method'].split(".")[0]
            thodex_message(ws, message)


def thodex_message(ws, message: dict):
    """
        If you want to close the socket connection.
        You can call 'ws.close()' anywhere in this function.
    """
    if message['method'] == 'deals':
        print('deals Params', message['params'], sep=" => ", end="\n\n")
    elif message['method'] == 'price':
        print('price Params', message['params'], sep=" => ", end="\n\n")
    elif message['method'] == 'state':
        print('state Params', message['params'], sep=" => ", end="\n\n")
    # ws.close()


"""
    #  (optional) apikey and secret are not required for the socket connection.
    thdx = ThodexSocketMessage("apikey", "secret")
"""
thdx = ThodexSocketMessage()

markets = ['BTCTRY', 'ETHTRY', 'LTCTRY', "DASHTRY", "ETCTRY", "HOTTRY", "XRPTRY"]
thdx.socket_reader(markets)
