import json

from src.utils.constants import Collections
from src.models.theatre_model import Theatre
from src.core.db_operations import theatre_operations
from src.exceptions.db_operation_errors import InputValidationFailedError


class FakeConnection:
    def __init__(self):
        self._storage = []

    def get_records(self, skip_count=0, page_size=10, filter={}):
        return self._storage[skip_count: skip_count + page_size]

    def insert_record(self, insertion_data: dict):
        # mimic pymongo inserted id
        return "fakeid123"

    def get_record(self, id: str):
        for d in self._storage:
            if d.get('ID') == id or d.get('_id') == id:
                return d
        return None

    def delete_record(self, id: str):
        # soft delete: mark delete True and return modified_count=1
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


def test_get_complete_theatre_list(monkeypatch):
    fake = FakeConnection()
    fake._storage.append({
        "ID": "1",
        "name": "Test Theatre",
        "description": "desc",
        "location": "loc",
        "capacity": 50,
        "image": "img",
        "video": "vid",
        "base_price_per_hr": 100.0,
        "price_per_person": 10.0,
        "delete": False,
    })

    monkeypatch.setattr(Collections.theater, 'connection', fake)

    result_json = theatre_operations.get_complete_theatre_list()
    data = json.loads(result_json)
    assert 'theaters' in data
    assert len(data['theaters']) == 1
    assert data['theaters'][0]['name'] == 'Test Theatre'


def test_add_new_theatre_and_validation(monkeypatch):
    fake = FakeConnection()
    monkeypatch.setattr(Collections.theater, 'connection', fake)

    # invalid capacity should raise
    t_invalid = Theatre(
        ID='2', name='T2', description='', location='L', capacity=0,
        image='', video='', base_price_per_hr=10, price_per_person=5, delete=False
    )
    try:
        theatre_operations.add_new_theatre(t_invalid)
        assert False, "Expected InputValidationFailedError"
    except InputValidationFailedError:
        pass

    # valid theatre should return fake id
    t = Theatre(
        ID='3', name='T3', description='d', location='L', capacity=10,
        image='', video='', base_price_per_hr=50, price_per_person=5, delete=False
    )
    new_id = theatre_operations.add_new_theatre(t)
    assert new_id == 'fakeid123'
