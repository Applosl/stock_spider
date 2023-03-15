import unittest
from dotenv import load_dotenv
from tasks.stock_day_task import StockDailyTask


class TestStockListTask(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        self.ts_code_set = [
            "000001.SZ",
        ]

    def test_run(self):
        stock_daily_task = StockDailyTask()
        for ts_code in self.ts_code_set:
            print(ts_code)
            stock_daily_task.set_args({'ts_code': ts_code})
            stock_daily_task.run()


if __name__ == '__main__':
    unittest.main()
