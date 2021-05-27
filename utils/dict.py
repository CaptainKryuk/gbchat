import time

MSG_TEMPLATE = {
    "action": "msg",
    "time": time.time(),
    "to": "account_name",
    "from": "account_name",
    "encoding": "utf-8",
    "message": "message"
}


PRESENSE = {
    "action": "presence",
    "time": time.time(),
    "type": "status",
    "user": {
        "account_name": "C0deMaver1ck",
        "status": "online"
    }
}

QUIT = {
    'action': 'quit'
}