import json

from src.utils.constants import Collections
from src.models.booking_details_model import Booking
from src.core.db_operations import booking_operations
from src.exceptions.db_operation_errors import InputValidationFailedError


class FakeConnection:
    def __init__(self):
        self._storage = []

    def get_records(self, skip_count=0, page_size=10, filter={}):
        return self._storage[skip_count: skip_count + page_size]

    def insert_record(self, insertion_data: dict):
        return "fake-booking-id"

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


def test_get_bookings_list_and_add(monkeypatch):
    fake = FakeConnection()
    fake._storage.append({
        "ID": "b1",
        "name_of_person": "Alice",
        "contact": 9876543210,
        "total_price": 200.0,
        "theatre_id": "1",
        "slot_id": "s1",
        "number_of_people": 2,
        "addons": [],
        "addon_options": [],
        "decoration_id": None,
        "note": "",
        "advance_payment": 0.0,
        "coupon_id": None,
        "booking_status": "confirmed",
        "booking_date": 123456,
        "email": "a@b.com",
        "discount_price": 0.0,
        "billing_status": "paid",
        "communication_status": "sent",
        "txn_ids": [],
        "delete": False,
    })

    monkeypatch.setattr(Collections.bookings, 'connection', fake)

    result_json = booking_operations.get_bookings_list()
    data = json.loads(result_json)
    assert 'bookings' in data
    assert len(data['bookings']) == 1

    # invalid contact
    bad = Booking(
        ID='b2', name_of_person='Bob', contact=123, total_price=100.0, theatre_id='1', slot_id='s1',
        number_of_people=1, addons=[], addon_options=[], decoration_id=None, note='', advance_payment=0.0,
        coupon_id=None, booking_status='pending', booking_date=1, email='x@y.com', discount_price=0.0,
        billing_status='unpaid', communication_status='none', txn_ids=[]
    )
    try:
        booking_operations.add_new_booking(bad)
        assert False
    except InputValidationFailedError:
        pass

    # valid booking
    good = Booking(
        ID='b3', name_of_person='Carol', contact=9876543210, total_price=150.0, theatre_id='1', slot_id='s1',
        number_of_people=3, addons=[], addon_options=[], decoration_id=None, note='', advance_payment=0.0,
        coupon_id=None, booking_status='pending', booking_date=1, email='c@d.com', discount_price=0.0,
        billing_status='unpaid', communication_status='none', txn_ids=[]
    )
    new_id = booking_operations.add_new_booking(good)
    assert new_id == 'fake-booking-id'
