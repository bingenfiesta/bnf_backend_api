import json

from src.utils.constants import Collections
from src.models.slot_model import Slot
from src.core.db_operations import slot_operations
from src.exceptions.db_operation_errors import InputValidationFailedError


class FakeConnection:
    def __init__(self):
        self._storage = []

    def get_records(self, skip_count=0, page_size=10, filter={}):
        return self._storage[skip_count: skip_count + page_size]

    def insert_record(self, insertion_data: dict):
        return "fake-slot-id"

    def get_record(self, id: str):
        for d in self._storage:
            if d.get('ID') == id or d.get('_id') == id:
                return d
        return None

    def delete_record(self, id: str):
        for d in self._storage:
            if d.get('ID') == id or d.get('_id') == id:
                d['delete'] = True
                return 1
        return 0

    def update_record(self, id: str, updates: dict):
        for d in self._storage:
            if d.get('ID') == id or d.get('_id') == id:
                d.update(updates)
                return 1
        return 0


def test_get_slots_list_and_add(monkeypatch):
    fake = FakeConnection()
    fake._storage.append({
        "ID": "s1",
        "name": "Morning",
        "start": 1000,
        "end": 2000,
        "price": 100.0,
        "theatre_id": "1",
        "applied_coupon": None,
        "delete": False,
    })

    monkeypatch.setattr(Collections.slots, 'connection', fake)

    result_json = slot_operations.get_slots_list()
    data = json.loads(result_json)
    assert 'slots' in data
    assert len(data['slots']) == 1

    # add invalid slot (start >= end)
    bad_slot = Slot(ID='s2', name='Bad', start=2000, end=1000, price=50, theatre_id='1', applied_coupon='')
    try:
        slot_operations.add_new_slot(bad_slot)
        assert False
    except InputValidationFailedError:
        pass

    # add valid slot
    good_slot = Slot(ID='s3', name='Good', start=100, end=200, price=50, theatre_id='1', applied_coupon='')
    new_id = slot_operations.add_new_slot(good_slot)
    assert new_id == 'fake-slot-id'
