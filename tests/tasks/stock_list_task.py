import unittest
from dotenv import load_dotenv
from tasks.stock_list_task import StockListTask


class TestStockListTask(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()

    def test_run(self):
        stock_list_task = StockListTask()
        stock_list_task.run()


if __name__ == '__main__':
    unittest.main()
