"""
stock_list_task
股票列表任务
"""
import os
import requests
from typing import List
from storages.stock import StockItemType, StockList
from tasks.task import Task
from datetime import datetime


def _to_stock_dict(item, fields):
    if len(fields) != len(item):
        return None
    di = {}
    for k, i in enumerate(fields):
        di[fields[k]] = item[k]
    return di


class StockListTask(Task):
    _name = 'stock_list'
    _token = os.getenv("TUSHARE_TOKEN", "")

    def run(self):
        session = requests.session()
        data = {
            'api_name': 'stock_basic',
            'token': self._token,
            'params': {
                "ts_code": "",
                "name": "",
                "exchange": "",
                "market": "",
                "is_hs": "",
                "list_status": "",
                "limit": 5000,
                "offset": 0
            },
            'fields': 'ts_code,symbol,name,area,industry,market,list_date,fullname,enname,cnspell,exchange,curr_type,list_status,delist_date,is_hs',
        }
        resp = session.post(url='http://api.tushare.pro', json=data, timeout=2)
        resp_data = resp.json()
        session.close()

        if resp_data['code'] != 0:
            return False

        fields = resp_data['data']['fields']
        total = len(resp_data['data']['items'])
        items = resp_data['data']['items']
        item_type_set = self._build_item(items, fields)
        self._save_db(item_type_set)

    def _build_item(self, items, fields):
        item_type_set = []
        for i in items:
            # 转换成dict
            di = _to_stock_dict(i, fields)
            if di is None:
                continue
            di['list_date'] = None if di['list_date'] is None else datetime.strptime(di['list_date'], '%Y%m%d').strftime('%Y-%m-%d')
            di['delist_date'] = None if di['delist_date'] is None else datetime.strptime(di['delist_date'], '%Y%m%d').strftime('%Y-%m-%d')
            item_type_set.append(StockItemType(di))
        return item_type_set

    def _save_db(self, item_type_set: List[StockItemType]):
        store = StockList()
        store.save_batch(item_type_set)
