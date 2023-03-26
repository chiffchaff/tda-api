import json
from unittest import TestCase

from tda.orders.equities import equity_sell_trailing_stop_limit


class Test(TestCase):
    def test_equity_sell_trailing_stop_limit(self):
        symbol="@ABC"
        quantity=100
        trail_offset=10
        limit_price=120

        orderspec = equity_sell_trailing_stop_limit(symbol, quantity, trail_offset, limit_price)

        orderJson = json.dumps(orderspec.build(), indent=4)
        print("Buy Order :", orderJson)