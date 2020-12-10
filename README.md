# Thodex Python Api
Python library for the Thodex API designed to be easy to use.

## Installation
```
Type "python setup.py install" or "pip install thodex" to install.
```

## Public Methods
##### server_time
###### Success-Response:
```json
{
    "error": null,
    "result": {
        "time": 1581505952,
        "timestamp": "2020-02-12 11:12:32"
    }
}
```
---
##### markets
###### Success-Response:
```json
{
    "error": null,
    "result": [
        {
            "keyname": "BTCTRY",
            "stock_keyname": "BTC",
            "money_keyname": "TRY",
            "stock_fullname": "Bitcoin",
            "money_fullname": "Türk Lirası",
            "stock_display": "BTC",
            "money_display": "TRY",
            "stock_prec": 8,
            "money_prec": 2,
            "min_amount": "0.0001",
            "maintenance": "NO",
            "maintenance_note": null
        }
    ]
}
```
---
##### market_status
###### Success-Response:
```json
{
    "error": null,
    "result": {
        "volume": "0",
        "high": "0",
        "open": "0",
        "period": 86400,
        "low": "0",
        "last": "53030.3",
        "deal": "0",
        "close": "0"
    }
}
```
---
##### market_summary
###### Success-Response:
```json
{
    "error": null,
    "result": [
        {
            "name": "BTCTRY",
            "ask_count": 1,
            "ask_amount": "1.56666",
            "bid_count": 4,
            "bid_amount": "5.56952"
        }
    ]
}
```
---
##### market_history
###### Success-Response:
```json
{
    "error": null,
    "result": [
        {
            "type": "sell",
            "id": 215302,
            "amount": "1.04508",
            "time": 1572852982.845166,
            "price": "53030.3"
        },
        {
            "type": "buy",
            "id": 215301,
            "amount": "1",
            "time": 1572608264.622277,
            "price": "40000"
        }
    ]
}
```
---
##### order_depth
###### Success-Response:
```json
{
    "error": null,
    "result": {
        "asks": [
            [
                "53035.65",
                "1.56666"
            ]
        ],
        "bids": [
            [
                "53030.3",
                "0.21112"
            ],
            [
                "52950.01",
                "1.77865"
            ],
            [
                "52948.24",
                "1.99221"
            ],
            [
                "52814.19",
                "1.58754"
            ]
        ]
    }
}
```
## Authenticated Methods
##### get_open_orders
###### Success-Response:
```json
{
    "errors": null,
    "result": {
        "limit": 50,
        "offset": 0,
        "total": 1,
        "records": [
            {
                "id": 703626,
                "market": "BTCTRY",
                "source": "api",
                "type": 1,
                "side": 1,
                "ctime": 1575458715.920797,
                "mtime": 1575458715.920797,
                "price": "12340",
                "amount": "0.3",
                "taker_fee": "0",
                "maker_fee": "0",
                "left": "0.3",
                "deal_stock": "0",
                "deal_money": "0",
                "deal_fee": "0"
            }
        ]
    }
}
```
---
##### get_order_history
###### Success-Response:
```json
{
    "errors": null,
    "result": {
        "offset": 0,
        "limit": 50,
        "records": [
            {
                "time": 1572432266.2779,
                "id": 215024,
                "side": 2,
                "role": 1,
                "price": "10",
                "amount": "1",
                "deal": "10",
                "fee": "0",
                "deal_order_id": 591041,
                "market": "BTCTRY"
            },
            {
                "time": 1572028345.815899,
                "id": 214827,
                "side": 2,
                "role": 2,
                "price": "20",
                "amount": "0.001",
                "deal": "0.02",
                "fee": "0",
                "deal_order_id": 590464,
                "market": "BTCTRY"
            }
        ]
    }
}
```
---
##### buy_limit
###### Success-Response:
```json
{
    "errors": null,
    "result": {
        "id": 703619,
        "market": "BTCTRY",
        "source": "api",
        "type": 1,
        "side": 2,
        "ctime": 1575456329.437614,
        "mtime": 1575456329.437624,
        "price": "12340",
        "amount": "0.001",
        "taker_fee": "0",
        "maker_fee": "0",
        "left": "0e-8",
        "deal_stock": "0.001",
        "deal_money": "12.34",
        "deal_fee": "0e-12"
    }
}
```
---
##### buy_market
###### Success-Response:
```json
{
    "errors": null,
    "result": {
        "id": 703625,
        "market": "BTCTRY",
        "source": "api",
        "type": 2,
        "side": 2,
        "ctime": 1575458371.988324,
        "mtime": 1575458371.988339,
        "price": "0",
        "amount": "100",
        "taker_fee": "0",
        "maker_fee": "0",
        "left": "0.0000952",
        "deal_stock": "0.00810372",
        "deal_money": "99.9999048",
        "deal_fee": "0e-12"
    }
}
```
---
##### sell_limit
###### Success-Response:
```json
{
    "errors": null,
    "result": {
        "id": 703626,
        "market": "BTCTRY",
        "source": "api",
        "type": 1,
        "side": 1,
        "ctime": 1575458715.920797,
        "mtime": 1575458715.920797,
        "price": "12340",
        "amount": "0.3",
        "taker_fee": "0",
        "maker_fee": "0",
        "left": "0.3",
        "deal_stock": "0",
        "deal_money": "0",
        "deal_fee": "0"
    }
}
```
---
##### sell_market
###### Success-Response:
```json
{
    "errors": null,
    "result": {
        "id": 703627,
        "market": "BTCTRY",
        "source": "api",
        "type": 2,
        "side": 1,
        "ctime": 1575458989.680405,
        "mtime": 1575458989.681919,
        "price": "0",
        "amount": "0.3",
        "taker_fee": "0",
        "maker_fee": "0",
        "left": "0e-8",
        "deal_stock": "0.3",
        "deal_money": "3645",
        "deal_fee": "0e-14"
    }
}
```
---
##### cancel_order
###### Success-Response:
```json
{
    "errors": null,
    "result": []
}
```
---
##### get_balance
###### Success-Response:
```json
{
    "error": null,
    "result": {
        "TRY": {
            "available": "0.0038",
            "freeze": "0"
        },
        "BTC": {
            "available": "0",
            "freeze": "0"
        },
        "ETH": {
            "available": "0",
            "freeze": "0"
        },
    }
}
```
---

## Errors
##### Http Errors
    HTTP/1.1 404 Not Found
```json
 {
   "error":{
      "code":404,
      "message":null
   },
   "result":null
}
```
##### API Errors
    HTTP/1.1 406 Not Acceptable
```json
{
   "error":{
      "code":620,
      "message":"registration failed"
   },
   "result":null
}
```

##### Validation Errors
    HTTP/1.1 406 Not Acceptable
```json
{
   "error":{
      "code":619,
      "message":"The asset field is required."
   },
   "result":{
      "validation":{
         "asset":[
            "The asset field is required."
         ]
      }
   }
}
```

#### List of Error Messages

##### Http Errors:

Code | Message
--- | --- 
401 | Unauthorized
404 | Not Found
406 | Not Acceptable
500 | Internal Server Error

##### Api Errors
Code | Message
--- | ---
429 | Too many request
600 | Api key required
601 | Api key no valid
604 | User not found
605 | Below min level
606 | Invalid credentials
607 | Account disabled
608 | White list unauthorized ip
609 | Authorization token required
610 | Authorization token mismatch
611 | Invalid tonce
612 | Market limit order creation failed
613 | Market order creation failed
614 | Market order cancelation failed
619 | Parameters validation failed
630 | Amount must exceed transfer fee
634 | Wallet not found
639 | Only https connections allowed
641 | Wallet creation failed
651 | Transfer failed please contact us
652 | The amount must exceed minimum transfer limit
657 | Location lock
658 | Invalid captcha
659 | White list toggle failed
660 | White list add new failed
661 | White list delete failed
673 | Selected nationality denied asset