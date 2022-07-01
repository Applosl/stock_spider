import unittest
from datetime import datetime
from dotenv import load_dotenv
from storages.stock import StockList, StockItemType


class TestStock(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()

    def test_save(self):
        i = StockItemType({
            'ts_code': '',
            'symbol': '',
            'area': '',
            'industry': '',
            'fullname': '',
            'enname': '',
            'cnspell': '',
            'market': '',
            'exchange': '',
            'curr_type': '',
            'list_status': '',
            'list_date': datetime.today(),
            'delist_date': datetime.today(),
            'is_hs': '',
            'create_at': datetime.now(),
        })
        stock_list = StockList()
        stock_list.save(i)


if __name__ == '__main__':
    unittest.main()
