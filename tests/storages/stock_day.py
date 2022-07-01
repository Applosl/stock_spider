import unittest
from datetime import datetime
from dotenv import load_dotenv
from storages.stock_day import StockDay, StockDayItemType


class TestStock(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()

    def test_save(self):
        i = StockDayItemType({
            'ts_code': '',
            'trade_date': '2022-01-01',
            'open': 0.0,
            'high': 0.0,
            'low': 0.0,
            'close': 0.0,
            'pre_close': 0.0,
            'change': 0.0,
            'pct_chg': 0.0,
            'vol': 0.0,
            'amount': 0.0,
            'create_at': datetime.now(),
        })
        stock_day = StockDay()
        stock_day.save(i)


if __name__ == '__main__':
    unittest.main()
