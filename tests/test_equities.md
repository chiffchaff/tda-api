
### [test_equity_sell_trailing_stop_limit](./test_equities.py)

```markdown
        symbol="@ABC"
        quantity=100
        trail_offset=10
        limit_price=120
```
```json
{
    "session": "NORMAL",
    "duration": "DAY",
    "orderType": "TRAILING_STOP",
    "quantity": 100,
    "stopPriceLinkBasis": "MARK",
    "stopPriceLinkType": "PERCENT",
    "stopPriceOffset": 10.0,
    "stopType": "MARK",
    "price": "120.00",
    "orderLegCollection": [
        {
            "instruction": "SELL",
            "instrument": {
                "assetType": "EQUITY",
                "symbol": "@ABC"
            },
            "quantity": 100
        }
    ],
    "orderStrategyType": "SINGLE"
}

```